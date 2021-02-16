from Packages.Global import loadLabledData , loadRawData , EmojiInformation , Load_Hazm_Normalization
from Packages.TFIDF import findCorrelatedTerms , generateTFIDF_Vectorizer
from Packages.LearningModel import compareAllModels , generateMultinuminalNB , generateSVC

# loading data
myDataFrame = loadLabledData("C:\\Datasets\\Labeled_Comments.xlsx")
RawComments = loadRawData("C:\\Datasets\\All_Comments_Min.xlsx")

# Show Emoji Information
EmojiInformation (myDataFrame)

# add a col to data frame
myDataFrame['category_id'] = myDataFrame['Label'].factorize()[0]

# Create some dictonaries and dataframe for future use
category_id_df = myDataFrame[['Label', 'category_id']].sort_values('category_id')
category_to_id = dict(category_id_df.values)
id_to_category = dict(category_id_df[['category_id', 'Label']].values)

normalizer , tokenizer , tokens , S_Words = Load_Hazm_Normalization()

# Generate TFIDF Vectorize
tfidf = generateTFIDF_Vectorizer(False, normalizer.normalize, tokens, (1, 2), S_Words  )

#Transform each complaint into a vector
comments = myDataFrame.comment
features = tfidf.fit_transform(comments).toarray()
labels = myDataFrame.category_id

#Compair All Models ( MultinomialNB, LinearSVC, RandomForestClassifier, LogisticRegression )
compareAllModels(features,labels)

# Finding the three most correlated terms with each of the product categories
findCorrelatedTerms(tfidf, features, labels, category_to_id, 3)

# ************************** Multinomial NB ***************************
generateMultinuminalNB(myDataFrame)

# ************************** LinearSVC ***************************
generateSVC( tfidf, myDataFrame, features, labels , True, category_id_df, id_to_category)

# ************************** Set Label For all Comments ***************************
from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split
import pandas as pd

X_input = myDataFrame['comment'] # Collection of documents
y_input = myDataFrame['Label'] # Target or the labels
X_train, X_test, y_train, y_test = train_test_split(X_input, y_input, 
                                                    test_size=0.25,
                                                    random_state = 0)

fitted_vectorizer = tfidf.fit(X_train)
tfidf_vectorizer_vectors = fitted_vectorizer.transform(X_train)

SVCModel = LinearSVC().fit(tfidf_vectorizer_vectors, y_train)

#Output1 = pd.DataFrame(columns=['comment', 'Label'])
#Output_Dic = {}
f = open('myfile.csv', 'w',encoding='utf8')
for index, row in RawComments.iterrows():
    PridictedLabel = SVCModel.predict(fitted_vectorizer.transform([row.comment]))
    #Output_Dic.update({row.comment : PridictedLabel[0]})
    #Output1.append({'comment': row.comment, 'Label': PridictedLabel[0]},True)
    f.write(PridictedLabel[0])
    f.write('\t\t')
    f.write(row.comment)
    f.write('\n')
f.close()