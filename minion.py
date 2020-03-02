#!/usr/local/bin/python3

import re

def score(words,string):
    myscore=0
    for word in words:
        myscore = myscore + words[word] 
    return(myscore)      

def getwords(mystring):
    vowels = ["A","E","I","O","U"]
    klist={}
    slist={}
    for wordlen in range(1,len(mystring)+1):
        word=""
        for startindex in range(len(mystring)):
            if (startindex + wordlen > len(mystring)):
                continue
            word = mystring[startindex:startindex+wordlen]
            #print(word)
            if word[0] in vowels:
                try:
                    klist[word] = klist[word] + 1
                except:
                    klist[word] = 1
            else:
                try:
                    slist[word] = slist[word] + 1
                except:
                    slist[word] = 1
    return(klist,slist)

def minion_game(string):
    kevinwords,stuartwords=getwords(string)
    stuartscore=score(stuartwords,string)
    kevinscore=score(kevinwords,string)
    #print (kevinwords)
    #print (kevinscore)
    #print (stuartwords)
    #print (stuartscore)
    if ((string == "") or (stuartscore == kevinscore)):
        print("Draw")
        return
    if (stuartscore > kevinscore):
        print ("Stuart " + str(stuartscore))
    else:
        print ("Kevin " + str(kevinscore))

if __name__ == '__main__':
    s = input()
    minion_game(s)
