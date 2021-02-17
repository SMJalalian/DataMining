import pandas as pd
import matplotlib.pyplot as plt

from sklearn import metrics
from sklearn.svm import LinearSVC
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix
from sklearn.naive_bayes import MultinomialNB
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_predict
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer





def compareAllModels(features, labels ):
    models = [
        MultinomialNB(),
        RandomForestClassifier(n_estimators=200, max_depth=5, random_state=0),
        LogisticRegression(random_state=0),
        LinearSVC(),
    ]

    CV = 5
    cv_df = pd.DataFrame(index=range(CV * len(models)))

    entries = []
    for model in models:
      model_name = model.__class__.__name__
      accuracies = cross_val_score(model, features, labels, scoring='accuracy', cv=CV)
      for fold_idx, accuracy in enumerate(accuracies):
        entries.append((model_name, fold_idx, accuracy))    
    cv_df = pd.DataFrame(entries, columns=['model_name', 'fold_idx', 'accuracy'])

    import seaborn as sns
    sns.boxplot(x='model_name', y='accuracy', data=cv_df)
    sns.stripplot(x='model_name', y='accuracy', data=cv_df, 
                  size=8, jitter=True, edgecolor="gray", linewidth=2)
    plt.show()

    mean_accuracy = cv_df.groupby('model_name').accuracy.mean()
    std_accuracy = cv_df.groupby('model_name').accuracy.std()

    acc = pd.concat([mean_accuracy, std_accuracy], axis= 1, 
              ignore_index=True)
    acc.columns = ['Mean Accuracy', 'Standard deviation']   
#*****************************************************************************************************
def generateMultinuminalNB(sampleDataframe):
    tfidf_transformer = TfidfTransformer()
    count_vect = CountVectorizer()

    X_input = sampleDataframe['comment'] # Collection of documents
    y_input = sampleDataframe['Label'] # Target or the labels
    X_train, X_test, y_train, y_test = train_test_split(X_input, y_input, test_size=0.8, random_state = 1)
    X_train_counts = count_vect.fit_transform(X_train)
    X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)

    NB_Model = MultinomialNB().fit(X_train_tfidf, y_train)

    X, y = make_classification(n_samples=2000, n_features=20, n_informative=10, n_classes=11, random_state=0)
    estimator = GaussianNB()
    y_pred = cross_val_predict(estimator, X, y, cv=10)

    print("\n\n*********  MultinominalNB Model Classification Report  ***********\n\n")
    print(metrics.classification_report(y, y_pred))

    # One example Pridiction by MultinomialNB Model.....
    exampleComment = "کالا بسیار خوب و عالی هست .. به همه توصیه می کنم"
    print("\n\n(Multinomial) Naive Bayes Labeling  .... \n\n")
    print("Comment: " , exampleComment)
    print("Related emoji: ", NB_Model.predict(count_vect.transform([exampleComment])))
#*****************************************************************************************************
def generateLinearSVC( tfidf, sampleDataframe, features, labels, GetConfusionMatrix = False, category_id_df = "" , id_to_category = "" ):
    
    X_train, X_test, y_train, y_test,indices_train,indices_test = train_test_split(features, 
                                                               labels, 
                                                               sampleDataframe.index, test_size=0.8, 
                                                               random_state=1)
    SVCModel = LinearSVC()
    SVCModel.fit(X_train, y_train)
    y_pred = SVCModel.predict(X_test)

    print("\n\n********* Linear SVC Model Classification Report ***********\n\n")
    print(metrics.classification_report(y_test, y_pred, target_names= sampleDataframe['Label'].unique()))

    # One example Pridiction by Linear SVC Model.....
    exampleComment = "کالا بسیار خوب و عالی هست .. به همه توصیه می کنم"
    print("\n\n Linear SVC Model Labeling  .... \n\n")
    print("Comment: " , exampleComment)
    print("Related emoji: ", getSVCPrediction(tfidf, sampleDataframe, exampleComment) )

    if GetConfusionMatrix :
      getConfusionMatrix(category_id_df, id_to_category, y_pred)
#*****************************************************************************************************
def generateRandomForest( tfidf, sampleDataframe, features, labels, GetConfusionMatrix = False, category_id_df = "" , id_to_category = "" ):

  X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size = 0.8, random_state = 21)
                                                            
                                                               
  scaler = StandardScaler()
  X_train = scaler.fit_transform(X_train)
  X_test = scaler.transform(X_test)

  ForestModel = RandomForestClassifier(n_estimators=200, max_depth=5, random_state=0)
  ForestModel.fit(X_train, y_train)

  y_pred = ForestModel.predict(X_test)

  print("\n\n*********  RandomForest Model Classification Report ***********\n\n")
  print(metrics.classification_report(y_test, y_pred, target_names= sampleDataframe['Label'].unique()))

  # One example Pridiction by RandomForest Model.....
  exampleComment = "کالا بسیار خوب و عالی هست .. به همه توصیه می کنم"
  print("\n\n RandomForest Model Labeling  .... \n\n")
  print("Comment: " , exampleComment)
  print("Related emoji: ", getSVCPrediction(tfidf, sampleDataframe, exampleComment) )

  if GetConfusionMatrix :
    getConfusionMatrix(category_id_df, id_to_category, y_pred)
#*****************************************************************************************************
def generateRegression( tfidf, sampleDataframe, features, labels, GetConfusionMatrix = False, category_id_df = "" , id_to_category = "" ):
    
    X_train, X_test, y_train, y_test,indices_train,indices_test = train_test_split(features, 
                                                               labels, 
                                                               sampleDataframe.index, test_size=0.8, 
                                                               random_state=1)
    RegMdel = RegressionModel()
    SVCModel.fit(X_train, y_train)
    y_pred = SVCModel.predict(X_test)

    print("\n\n********* Linear SVC Model Classification Report ***********\n\n")
    print(metrics.classification_report(y_test, y_pred, target_names= sampleDataframe['Label'].unique()))
#*****************************************************************************************************
def getSVCPrediction( tfidf,  sampleDataframe, newComment):

    X_input = sampleDataframe['comment'] # Collection of documents
    y_input = sampleDataframe['Label'] # Target or the labels
    X_train, X_test, y_train, y_test = train_test_split(X_input, y_input, 
                                                        test_size=0.8,
                                                        random_state = 0)

    fitted_vectorizer = tfidf.fit(X_train)
    tfidf_vectorizer_vectors = fitted_vectorizer.transform(X_train)

    model = LinearSVC().fit(tfidf_vectorizer_vectors, y_train)

    return model.predict(fitted_vectorizer.transform([newComment]))
#*****************************************************************************************************
def ReplaceClassifier(diabetes):
  if diabetes == True:
    diabetes='1'
  else:
    diabetes='0'
  return diabetes
#*****************************************************************************************************
def getConfusionMatrix( sampleDataframe, features, labels, category_id_df, id_to_category, y_pred):
  X_train, X_test, y_train, y_test, indices_train, indices_test = train_test_split(features, labels, sampleDataframe.index, test_size=0.8, random_state=0)
  conf_mat = confusion_matrix(y_test, y_pred)
  for predicted in category_id_df.category_id:
    for actual in category_id_df.category_id:
      if predicted != actual and conf_mat[actual, predicted] >= 20:
        print("'{}' predicted as '{}' : {} examples.".format(id_to_category[actual], 
                                                              id_to_category[predicted], 
                                                              conf_mat[actual, predicted]))  