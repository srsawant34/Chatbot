import pymongo
import nltk
def change(sent):
    sent=str(sent)
    sent=list(sent)
    x=''.join(sent)
    return x

client=pymongo.MongoClient()
db=client.avas

m=0

c=db.answer.count()

print("Enter number of questions")
z=int(input())
for i in range(z):
    print("Enter the quest")
    sentence=str(input())
    sentence=list(sentence)
    for i in sentence:
        if i=='?':
            sentence.remove('?')
    sentence[0 ]=sentence[0].upper()
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


    print("verb are")
    print(verb)
    print("adj")
    print(adj)
    print("noun")
    print(noun)
    print("adverb")
    print(adv)
    print("sub")
    print(sub)


    for i in range(v):
        db.verbo.insert({"id":c,"verb":verb[i]})

    for i in range(ad):
        db.adjo.insert({"id":c,"adj":adj[i]})   


    for i in range(n):
        db.nouno.insert({"id":c,"noun":noun[i]})

  
    for i in range(av):
        db.advo.insert({"id":c,"adv":adv[i]})

    for i in range(su):
        db.subo.insert({"id":c,"sub":sub[i]})

    print("write the correct answer")
    answ=str(input())
    db.answer.insert({"id":c,"ans":answ})
    c=c+1



