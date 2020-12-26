#
class TextProcessing():
    def __init__ (self, docName , doctext):
        self.DoccumentName = docName
        self.Context = doctext
        self.AllSentence = sentenceTokenization(self.Context)
        self.PurifiedSentences = RemoveJunkyWords(self.AllSentence)

        self.AllWords = wordTokenization(self.PurifiedSentences)
        self.AllWordsCount = len(self.AllWords)

        self.PurifiedWords = RemoveStopWords(self.AllWords)
        self.PurifiedWordsCount = len(self.PurifiedWords)

        self.UniqueWords = set(self.PurifiedWords)
        self.UniqueWordCount = len(self.UniqueWords)

        self.WordCloudText = Get_WordCloudText(self.UniqueWords)
# **************** Read Files from Directory ****************
def Read_All_Files ( path ):
    import os
    allFiles = os.listdir(path)
    DataSet = {}
    for input in allFiles:
        filePath = path + input
        f = open(filePath , "r")
        DataSet.update({input : f })
    return DataSet
#**************** Sentence Tokenization ****************
def sentenceTokenization ( context ):
    return context.split('. ')
#**************** Sentence Tokenization ****************
def wordTokenization ( purifiedSentences ):
    output = []
    for sen in purifiedSentences:
        words = sen.strip().split(' ')
        for w in words:
            output.append(str.strip(w))
    return output
#**************** Remove Numbers and Tags ****************
def RemoveJunkyWords ( tokenizedSentences ):
    import re
    regex = re.compile('[^a-zA-Z]')
    output = []
    for sentence in tokenizedSentences:
        temp = regex.sub(' ', sentence)
        output.append(temp)
    return output
#**************** Remove Stop Works ****************   
def RemoveStopWords (allWords ):
    stopwords = ["", "vs" , "i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]
    output = []
    for word in allWords:
        if str.lower(word)  not in stopwords and len(word) > 1:
            output.append(word)
    return output
#**************** Calculate Number of Repeatition ****************
def Get_RepeatitionOfWords (allwords, allUniqueWords ):
    import operator
    output = {}
    for word in allUniqueWords:
        repeat = (list(allwords)).count(word)
        output.update({word : repeat})
    return output
#**************** Generate Word Cloud Input Text **************** 
def Get_WordCloudText (allUniqueWords ):
    output = ''
    for word in allUniqueWords:
        output  = output + word + " "
    return output
#**************** Show Word Cloud ****************   
def Generate_WordCloud ( textOpject ):
    from wordcloud import WordCloud
    import matplotlib.pyplot as plt
    wordcloud = WordCloud(width = 500, height = 500, 
                background_color ='white', 
                min_font_size = 8).generate(textOpject.WordCloudText) 
    plt.figure(figsize = (6, 6), facecolor = None) 
    plt.figtext  = textOpject.DoccumentName
    plt.imshow(wordcloud) 
    plt.axis("off") 
    plt.tight_layout(pad = 0) 
    plt.show() 