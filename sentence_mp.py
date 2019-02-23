import pymongo
import random
#import json
import nltk
import multiprocessing as mp
from threading import Thread

global ans
def change(sent):
    sent=str(sent)
    sent=list(sent)
    x=''.join(sent)
    return x

client=pymongo.MongoClient()
db=client.avas
m=0

#Function verbo handles verb scoring
def verbo(verb):
    for i in range(len(verb)):
            ID=db.verbo.find({"verb":verb[i]},{"_id":0,"verb":0})
            n=db.verbo.find({"verb":verb[i]},{"_id":0,"verb":0}).count()
            for j in range(n):
                a=int(ID[j]["id"])
                m=db.scores.find({"id":a},{"_id":0,"verb":0}).count()
                if m==0:
                    db.scores.insert({"id":a,"score":25})
                else:
                    s=db.scores.find({"id":a},{"_id":0,"id":0})
                    s=int(s[0]["score"])
                    db.scores.update({"id":a},{"id":a,"score":s+25})

#Function nouno handles noun scoring
def nouno(noun):
    for i in range(len(noun)):
            ID=db.nouno.find({"noun":noun[i]},{"_id":0,"noun":0})
            n=db.nouno.find({"noun":noun[i]},{"_id":0,"noun":0}).count()
            for j in range(n):
                a=int(ID[j]["id"])
                m=db.scores.find({"id":a},{"_id":0,"noun":0}).count()
                if m==0:
                    db.scores.insert({"id":a,"score":30})
                else:
                    s=db.scores.find({"id":a},{"_id":0,"id":0})
                    s=int(s[0]["score"])
                    db.scores.update({"id":a},{"id":a,"score":s+30})

#Function adjo handles adjective scoring
def adjo(adj):
    for i in range(len(adj)):
            ID=db.adjo.find({"adj":adj[i]},{"_id":0,"adj":0})
            n=db.adjo.find({"adj":adj[i]},{"_id":0,"adj":0}).count()
            for j in range(n):
                a=int(ID[j]["id"])
                m=db.scores.find({"id":a},{"_id":0,"adj":0}).count()
                if m==0:
                    db.scores.insert({"id":a,"score":20})
                else:
                    s=db.scores.find({"id":a},{"_id":0,"id":0})
                    s=int(s[0]["score"])
                    db.scores.update({"id":a},{"id":a,"score":s+20})

#Function advo handles adverb scoring
def advo(adv):
    for i in range(len(adv)):
            ID=db.advo.find({"adv":adv[i]},{"_id":0,"adv":0})
            n=db.advo.find({"adv":adv[i]},{"_id":0,"adv":0}).count()
            for j in range(n):
                a=int(ID[j]["id"])
                m=db.scores.find({"id":a},{"_id":0,"adv":0}).count()
                if m==0:
                    db.scores.insert({"id":a,"score":15})
                else:
                    s=db.scores.find({"id":a},{"_id":0,"id":0})
                    s=int(s[0]["score"])
                    db.scores.update({"id":a},{"id":a,"score":s+15})

#Function subo handles subject scoring
def subo(sub):
    for i in range(len(sub)):
            ID=db.subo.find({"sub":sub[i]},{"_id":0,"sub":0})
            n=db.subo.find({"sub":sub[i]},{"_id":0,"sub":0}).count()
            for j in range(n):
                a=int(ID[j]["id"])
                m=db.scores.find({"id":a},{"_id":0,"sub":0}).count()
                if m==0:
                    db.scores.insert({"id":a,"score":5})
                else:
                    s=db.scores.find({"id":a},{"_id":0,"id":0})
                    s=int(s[0]["score"])
                    db.scores.update({"id":a},{"id":a,"score":s+5})

def stringch():
    sentence=str(input())
    sentence=list(sentence)
    for i in sentence:
        if i=='?':
            sentence.remove('?')
    sentence[0]=sentence[0].upper()
    sentence=''.join(sentence)
    word=list(sentence)
    tokens=nltk.word_tokenize(sentence)
    tagged=nltk.pos_tag(tokens)
    verb=[]                         
    noun=[]
    adj=[]
    adv=[]
    sub=[]
    ad=0
    n=0
    v=0
    av=0
    su=0
    
    for i in range(len(tagged)):
        if tagged[i][1] == 'VBZ' or tagged[i][1] == 'VBD' or tagged[i][1] == 'VBG' or tagged[i][1] == 'VBN' or tagged[i][1] == 'VBP' or tagged[i][1] == 'VB' :
            subject='verb'
            temp=change(tagged[i][0])
            verb.append(temp)
            v=v+1
        elif tagged[i][1] == 'NN' or tagged[i][1] == 'NNS' or tagged[i][1] == 'NNP' or tagged[i][1] == 'NNPS':
            subject='noun'
            temp=change(tagged[i][0])
            noun.append(temp)
            n=n+1
        elif tagged[i][1]=='IN':
            subject='preposition'
        elif tagged[i][1]=='TO':
            subject='to'
            temp=change(tagged[i][0])
            sub.append(temp)
            su=su+1
        elif tagged[i][1]=='JJ' or tagged[i][1]=='JJR' or tagged[i][1]=='JJS':
            subject='adjective'
            temp=change(tagged[i][0])
            adj.append(temp)
            ad=ad+1
        elif tagged[i][1]=='RB' or tagged[i][1]=='RBR' or tagged[i][1]=='RBS':
            subject='adverb'
            temp=change(tagged[i][0])
            adv.append(temp)
            av=av+1
        elif tagged[i][1]=='WP' or tagged[i][1]=='WRB' :
            subject='pronoun'
    
    #print(x)
    for i in range(len(verb)):
        verb[i]=verb[i].replace('"',"'")
    for i in range(len(noun)):
        noun[i]=noun[i].replace('"',"'")
    for i in range(len(adj)):
        adj[i]=adj[i].replace('"',"'")
    for i in range(len(adv)):
        adv[i]=adv[i].replace('"',"'")
    for i in range(len(sub)):
        sub[i]=sub[i].replace('"',"'")
    #print(verb)
    #print(noun)
    #print(adj)

    #if v==0 and ad==0 and av==0 and n==0 and su==0:
        #print("I dont understand")
    if v!=0 or ad!=0 or av!=0 or n!=0 or su!=0:
        #Distributing task into threads
        #t1 executes verbo fn
        t1 = Thread(target=verbo, args=(verb,))

        #t2 executes nouno fn
        t2 = Thread(target=nouno, args=(noun,))

        #t3 executes adjo fn
        t3 = Thread(target=adjo, args=(adj,))

        #t4 executes advo fn
        t4 = Thread(target=advo, args=(adv,))

        #t5 executes subo fn
        t5 = Thread(target=subo, args=(sub,))

        t1.start()
        print("Thread 1 sarted executing verbo")
        t2.start()
        print("Thread 2 sarted executing nouno")
        t3.start()
        print("Thread 3 sarted executing adjo")
        t4.start()
        print("Thread 4 sarted executing advo")
        t5.start()
        print("Thread 5 sarted executing sub")
        
        t1.join()
        print("Thread 1 terminated")
        t2.join()
        print("Thread 2 terminated")
        t3.join()
        print("Thread 3 terminated")
        t4.join()
        print("Thread 4 terminated")
        t5.join()
        print("Thread 5 terminated")

        
        ans_id=db.scores.find({},{"_id":0}).sort([("score",-1)])
        a=int(ans_id[0]["id"])
        ans=db.answer.find({"id":a},{"_id":0,"id":0})
        ans=ans[0]["ans"]

        
        print(ans)
        #speech(ans)
        db.scores.drop()

while(1):
   stringch() 


