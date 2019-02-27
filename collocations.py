"""
This is a program that displays the top 20 collocations in the attached file called Collocations.. The program is run as follows:

$python collocations.py Collocations <measure> , where measure can either be pmi or chi-square or chi

The program displays the top 20 collocations, along with their score

"""


import collections
import nltk
import re
import numpy as np
import math
import sys



unigramList=[]
bigramList=[]
chiSquareScores=[]
pmiScores=[]
collocations_file=open(sys.argv[1],"r")

#removing special characters from the dataset and placing each word into a list
collocations_dataset=collocations_file.read().split()
collocations_dataset=[item for item in collocations_dataset if re.search("[A-Za-z0-9]",item.split()[0]) ]
unigramCounter=collections.Counter(collocations_dataset)
bigrams=nltk.bigrams(collocations_dataset)
bigramList=[item for item in bigrams]
bigramCounter=collections.Counter(bigramList)
unigramList=[item for item in collocations_dataset]


#function that calculates the Chi Square measure for each bigram
def ChiSquare(bigram):
   word1=bigram[0]
   word2=bigram[1]
   totalUnigramCount=len(unigramList)
   
 
   bothWordsCount=bigramCounter[word1,word2]
   leftWordOnlyCount=unigramCounter[word1]-bothWordsCount
   rightWordOnlyCount=unigramCounter[word2]-bothWordsCount
   neitherWordCount=(len(bigramList)-bothWordsCount-leftWordOnlyCount-rightWordOnlyCount)
   
  
   



   

 
   EfirstRowFirstColumn=(((bothWordsCount+leftWordOnlyCount)/totalUnigramCount)*((bothWordsCount+rightWordOnlyCount)/totalUnigramCount)*totalUnigramCount)
   EfirstRowSecondColumn=(((neitherWordCount+rightWordOnlyCount)/totalUnigramCount)*((bothWordsCount+rightWordOnlyCount)/totalUnigramCount)*totalUnigramCount)
   EsecondRowFirstColumn=(((bothWordsCount+leftWordOnlyCount)/totalUnigramCount)*((neitherWordCount+leftWordOnlyCount)/totalUnigramCount)*totalUnigramCount)
   EsecondRowSecondColumn=(((rightWordOnlyCount+neitherWordCount)/totalUnigramCount)*((neitherWordCount+leftWordOnlyCount)/totalUnigramCount)*totalUnigramCount)
   
   
   chi=((math.pow(bothWordsCount-EfirstRowFirstColumn,2)/EfirstRowFirstColumn)
   +(math.pow(rightWordOnlyCount-EfirstRowSecondColumn,2)/EfirstRowSecondColumn)
   +(math.pow(leftWordOnlyCount-EsecondRowFirstColumn,2)/EsecondRowFirstColumn)+
   +(math.pow(neitherWordCount-EsecondRowSecondColumn,2)/EsecondRowSecondColumn))
   
   
   


   return round(chi,2)
 
 
#function that returns the PMI score of each bigram   
def PMI(bigram):
    totalBigramCount=len(bigramList)
    totalUnigramCount=len(unigramList)
    bigramCount=bigramCounter[bigram]
    
    pBigram=bigramCount/totalBigramCount
    
    pWord1=unigramCounter[bigram[0]]/totalUnigramCount
    
    pWord2=unigramCounter[bigram[1]]/totalUnigramCount
  
    pmi=(math.log(pBigram/(pWord1*pWord2)))
 
     

    return round(pmi,2)



#Displaying the results to the console
def printResults(resultList):
        print("\t\t\t Bigram \t\t\t  Score")
        print("--------------------------------------------------------------------------")
        for item in resultList[0:20] :
            bigram=bigramList[bigramList.index(item[1])]
            firstWord=bigram[0]
            secondWord=bigram[1]
            print(resultList.index(item)+1,"\t\t",bigramList[bigramList.index(item[1])],"\t\t\t",item[0],"\t\t\t")
#           
            
            

   






if(sys.argv[2]=="chi-square" or sys.argv[2]== "chi" or sys.argv[2]=="chisquare"):
    chiSquareScores=[[ChiSquare(item),item] for item in bigramCounter]
    chiSquareScores.sort(reverse=True,key=lambda k:(k[0],k[0]))
    printResults(chiSquareScores)
    
elif (sys.argv[2]=="PMI" or sys.argv[2]== "pmi"):
      pmiScores=[[PMI(item),item] for item in bigramCounter]
      pmiScores.sort(reverse=True,key=lambda k:(k[0],k[0]))
      printResults(pmiScores)
    
    





