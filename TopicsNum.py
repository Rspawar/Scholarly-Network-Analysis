import csv
import pandas as pd
import matplotlib.pyplot as plt
import tom_lib.utils as ut
from tom_lib.nlp.topic_model import NonNegativeMatrixFactorization
from tom_lib.structure.corpus import Corpus
from tom_lib.visualization.visualization import Visualization
import numpy as np
import os
import os.path
from timeit import default_timer as timer
import nltk
nltk.download('stopwords')



global num_topics
num_topics = 10
num_words = 10
global word_list
word_list = {}
documents = {}

#-----------------------------------------------------------------------------------------------------------------------------
def MakeCompatibleCsv():

    if(os.path.isfile("Papers.csv")):
        os.remove("Papers.csv")
        print("File Removed!")

    ls = []
    st = 'id' + '\t' + 'title' + '\t' + 'text' + '\t' + 'author' + '\t' + 'date'
    # st=st.encode('utf-8')
    ls.append([st])
    with open("Papers.csv", 'w', encoding="utf-8", newline='') as csvfile:
        wr = csv.writer(csvfile, quoting=csv.QUOTE_NONE, escapechar='\\')
        wr.writerows(ls)

#-----------------------------------------------------------------------------------------------------------------------------

def ReadMainCsvFile():
    global documents
    i = 0

    file = open("CvsFileName.txt", "r")
    fileContent = file.read()
    with open(fileContent, encoding="utf-8") as csvfile:
        csvreader = csv.reader(csvfile, quoting=csv.QUOTE_ALL, escapechar='\\', delimiter=',', quotechar='"')
        csvreader = csv.reader(( x.replace('\0', '') for x in csvfile), delimiter=',')
        for row in csvreader:
            if(row):
                # doc.append(row[0]) #Key
                # doc.append(row[1])#Title
                # doc.append(row[15])#text
                # doc.append(row[3])#author
                # doc.append(row[2])#Year
                # doc.append(row[9])#affiliation
                # doc.append(row[14])#Url
                if (row[0] == ''):
                    row[0] = ' '
                if (row[1] == ''):
                    row[1] = ' '
                if (row[15] == ''):
                    row[15] = ' '
                if (row[2] == ''):
                    row[2] = ' '
                if (row[9] == ''):
                    row[9] = ' '


                lst = [row[0], row[1].replace('np.nan', ' '), row[15].replace('np.nan', ' '), row[3].replace('np.nan', ' '),
                       row[2].replace('np.nan', ' ')]
                l_new = ['missing' if x is np.nan else x for x in lst]
                #documents.append(l_new)
                with open('Papers.csv','a',encoding="UTF8") as fd:
                    #wre = csv.writer(fd)
                    documents[i]=l_new[0]
                    st = str(l_new[0]) + '\t' + str(l_new[1]) + '\t' + str(l_new[2]) + '\t' + str(l_new[3]) + '\t' + str(l_new[4])
                    lst=([st])
                    fd.write(st+"\n")
                i = i + 1

#------------------------------------------------------------------------------------------------------------------------------------
def MakeGlobalTopics(topic_model):
    wordLst = ''
    for topic_id in range(0, num_topics):
        for weighted_word in topic_model.top_words(topic_id, num_words):
            if (len(wordLst) > 0):
                wordLst = wordLst + ' ' + str(weighted_word[0])
            else:
                wordLst = wordLst + str(weighted_word[0])
        word_list[topic_id] = wordLst
        wordLst = ''

    ls = []
    st = 'Topic_Id' + '\t' + 'TopicWords'
    ls.append([st])
    st = ''
    with open('GlobalTopicsWithName.csv', 'w', encoding='UTF8', newline='') as csvfile:
        wr = csv.writer(csvfile)
        for k in sorted(word_list.keys()):
            st = str(k) + '\t' + str(word_list[k])
            ls.append([st])
        wr.writerows(ls)
#-----------------------------------------------------------------------------------------------------------------------------------------
def WritrTopicsWithPaperID():
    topicsDic=[]
    global documents
    for k, v in word_list.items():
        strDocID = topic_model.documents_for_topic(k)
        for i in range(0, len(strDocID) - 1):
            topicsDic.append(str(k) + '\t' + str(documents[strDocID[i]]))

    ls = []
    st = 'Topic_Id' + '\t' + 'PaperID'
    # st=st.encode('utf-8')
    ls.append([st])
    st = ''
    with open('TopicIDPaperID.csv', 'w', encoding='UTF8', newline='') as csvfile:
        wr = csv.writer(csvfile)
        for k in range(0, len(topicsDic) - 1):
            st = topicsDic[k]
            ls.append([st])
        wr.writerows(ls)
#----------------------------------------------------------------------------------------------------------------------------------
def WriteTopicPerYear(corpus,topic_model):
    for i in range(0, 2019):
        fileDic = {}
        frequencyDic = {}
        docIdsDic = {}
        ids = corpus.doc_ids(i)
        for j in range(0, num_topics):
            if (topic_model.topic_frequency(j, date=i)):
                topicStr = word_list[j]
                topicStr = topicStr.replace(" ", "")
                fileDic[j] = topicStr
                frequencyDic[j] = topic_model.topic_frequency(j, date=i)


                """docList = []
                for doc_id in ids:
                    most_likely_topic = topic_model.most_likely_topic_for_document(doc_id)
                    if most_likely_topic == j:
                        docList.append(doc_id)
                docIdsDic[j] = docList"""

        ls = []
        st = 'Topic_Id' + '\t' + 'YearlyTopic_Frequency'
        ls.append([st])
        if (len(fileDic) > 0):
            with open('years\\' + str(i) + '.' + 'csv', 'w', encoding='utf-8', newline='') as csvfile:
                wr = csv.writer(csvfile, quoting=csv.QUOTE_NONE, escapechar='\\')
                for k, v in fileDic.items():
                    #strDic = "|".join(str(x) for x in docIdsDic[k])
                    st = str(k) + '\t' + str(frequencyDic[k])
                    ls.append([st])
                wr.writerows(ls)
#--------------------------------------------------------------------------------------------------------------------------------
def MakeVisualizationFile():
    topicsDic = {}
    with open('GlobalTopicsWithName.csv', encoding="utf-8") as csvfile:
        csvreader = csv.reader(csvfile, delimiter='\t')
        next(csvreader, None)
        for row in csvreader:
            if (row):
                topicsDic[row[0]] = row[1]

    GlobalDic1 = []
    for k, v in topicsDic.items():
        topicValue = topicsDic[k]
        docStr = set()
        yearList = []
        for root, dirs, files in os.walk(r'years/'):
            for name in files:
                with open('years/' + name, 'r', encoding="UTF8") as csvfile:
                    csvreader = csv.reader(csvfile, delimiter='\t', quoting=csv.QUOTE_NONE, escapechar='\\')
                    for row in csvreader:
                        if (row[0] == k):
                            GlobalDic1.append(row[0] + '\t' + name.replace('.csv', '') + '\t' + row[1])

    ls = []
    st = 'Topic_ID' +  '\t' + 'Year' + '\t' + 'Frequency'
    ls.append([st])
    st = ''
    with open('plotCSV.csv', 'w', encoding='utf-8', newline='') as csvfile:
        wr = csv.writer(csvfile)
        for k in range(len(GlobalDic1)):
            st = str(GlobalDic1[k])
            ls.append([st])
        wr.writerows(ls)
#--------------------------------------------------------------------------------------------------------------------------------
def Createplot():
    df = pd.read_csv('plotCSV.csv', delimiter='\t')

    ax0 = df.plot(kind='scatter',
                  x='Year',
                  y='Topic_ID',
                  figsize=(14, 8),
                  alpha=0.5,  # transparency
                  color='blue',
                  s=df['Frequency'] * 1000 + 10,  # pass in weights
                  )

    plt.title('Topic Evolution over the years')
    plt.ylabel('Topic_ID')
    plt.xlabel('Years')
    plt.savefig('topicevolution.png')
    plt.show()

#--------------------------------------------------------------------------------------------------------------------------------
start = timer()
print("Creating Papers.csv....")
MakeCompatibleCsv()
ReadMainCsvFile()
print("Initializing corpus....")
corpus = Corpus(source_file_path='Papers.csv',
                language='english',  # language for stop words
                vectorization='tfidf',  # 'tf' (term-frequency) or 'tfidf' (term-frequency inverse-document-frequency)
                n_gram=3,
                max_relative_frequency=0.8,  # ignore words which relative frequency is > than max_relative_frequency
                min_absolute_frequency=4) # ignore words which absolute frequency is < than min_absolute_frequency


print('corpus size:', corpus.size)
print('vocabulary size:', len(corpus.vocabulary))
#print('Vector representation of document 0:\n', corpus.vector_for_document(0))
# Instantiate a topic model
print('Instantiate a topic model...')
topic_model = NonNegativeMatrixFactorization(corpus)
topic_model.infer_topics(num_topics)
ut.save_topic_model(topic_model, 'output/NMF_30topics.tom')

print('Finding global Topics...')
print('Writing GlobalTopics with the name we assigned them plus topicWords:.....')
print('The name of the file is "GlobalTopicsWithName.csv"')
MakeGlobalTopics(topic_model)
print('Writing Topics with their related PaperID:.....')
print('The name of the file is "TopicIDPaperID.csv"')
WritrTopicsWithPaperID()
print('wrting topics per year...')
WriteTopicPerYear(corpus,topic_model)
print('Creating file for visualization called "PlotCsv.csv"')
MakeVisualizationFile()
print('Creating plot...')
Createplot()


try:
    viz = Visualization(topic_model)
    print('Printing plot for distribution of words per topics...')
    for k, v in word_list.items():
        viz.plot_word_distribution(k, nb_words=num_words, file_path='output/word_distribution'+str(k)+'.png')

    """print('Printing plot for finding optimal number of topics...')
    viz.plot_greene_metric(min_num_topics=5,
                           max_num_topics=50,
                           tao=10, step=1,
                           top_n_words=num_words)"""


except (Exception, ArithmeticError) as e:
    template = "An exception of type {0} occurred. Arguments:\n{1!r}"
    message = template.format(type(e).__name__, e.args)
    print(message)


end = timer()
print("Process completed, duration: %.2f seconds" % (end - start))


