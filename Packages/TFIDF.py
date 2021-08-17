from sklearn.feature_selection import chi2
from sklearn.feature_extraction.text import TfidfVectorizer

import numpy as np

def findCorrelatedTerms( tfidf, features, labels, categoryList, numberOfTrems ):
    N = numberOfTrems
    for Label, category_id in sorted(categoryList.items()):
      features_chi2 = chi2(features, labels == category_id)
      indices = np.argsort(features_chi2[0])
      feature_names = np.array(tfidf.get_feature_names())[indices]
      unigrams = [v for v in reversed(feature_names) if len(v.split(' ')) == 1][:N]
      bigrams = [v for v in reversed(feature_names) if len(v.split(' ')) == 2][:N]
      print("# '{}':".format(Label))
      print("  . Top unigrams:\n       . {}".format('\n       . '.join(unigrams)))
      print("  . Top bigrams:\n       . {}".format('\n       . '.join(bigrams)))
#***************************************************  
def generateTFIDF_Vectorizer (_setLowerCase, _preprocessor, _tokenizer, _ngram_range, _stop_words ):
  tfidf = TfidfVectorizer(lowercase=_setLowerCase, 
                        preprocessor=_preprocessor, 
                        tokenizer=_tokenizer,
                        ngram_range=_ngram_range,
                        stop_words=_stop_words)
  return tfidf                  