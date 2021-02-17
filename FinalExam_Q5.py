from Packages.Global import loadLabledData , EmojiInformation , Load_Hazm_Normalization
from Packages.TFIDF import findCorrelatedTerms , generateTFIDF_Vectorizer
from Packages.LearningModel import compareAllModels , generateMultinuminalNB , generateSVC

# loading data
myDataFrame = loadLabledData("Datasets/Labeled_Comments.csv")

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
generateSVC( tfidf, myDataFrame, features, labels , False, category_id_df, id_to_category)


