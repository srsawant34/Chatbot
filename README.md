# Chatbot
Retrieval based chatbot uses MongoDB database to find the most appropriate answer using scoring algorithm. The scoring is dependent on the weights of word type like subject,noun,verb etc.

Requirements - 
1. Python 
2. MongoDB, pymongo
3. NLTK

Each question have a id with respective word and answer. The tables are advo, adjo, nouno, subo, verbo and answer. Since the chatbot memory is database we have to feed the data to the database. To feed the database run the feed.py file after the mongodb client is running. Then give input the number of questions you want to insert, and question and answer respectively.
 
Chatbot Workflow :
1. Run the sentence.py (sentence_mp.py is multithreaded implementation of the same).First it connects to the database avas.
2. Takes question as input
3. Tokenization of words and tagging is done.
4. After identifying the type of word it is then searched with the respective table.
5. The score table gets updated for each id , and the scores are as follows :- verb = 25, nouns = 30, adjective = 20, adverb = 15, subject = 5.
6. The id having the highest score is used to find the answer from answer table and it is displayed.

Note-The chatbot have good accuracy if the feeded has all combination for word for forming the question. And you can not view the score table as it is created and destroyed for each question asked.
