import os
import sqlite3

#Check to see if the database files do not exist
if os.path.isfile('topics.db') is False:
    def DBcreation():
        topics_db = sqlite3.connect('topics.db')       #Creates a connection to the database file
        cursor = topics_db.cursor()                    #Cursor object is called up using this variable
        cursor.execute('''                   
        CREATE TABLE IF NOT EXISTS weather(
        wordID INTEGER PRIMARY KEY,
        words TEXT NOT NULL);
        ''')                                                #Creates the table if it does not exist in the database    
        topics_db.commit()
        cursor.execute('''  
        CREATE TABLE IF NOT EXISTS sport(
        wordID INTEGER PRIMARY KEY,
        words TEXT NOT NULL);
                ''')                                                #Creates the table if it does not exist in the database    
        topics_db.commit()
        cursor.execute('''  
        CREATE TABLE IF NOT EXISTS games(
        wordID INTEGER PRIMARY KEY,
        words TEXT NOT NULL);
                ''')                                                #Creates the table if it does not exist in the database    
        topics_db.commit()
        cursor.execute('''  
        CREATE TABLE IF NOT EXISTS music(
        wordID INTEGER PRIMARY KEY,
        words TEXT NOT NULL);
        ''')                                                #Creates the table if it does not exist in the database    
        topics_db.commit()                                  #Commits the statements, which saves changes made
        topics_db.close()
    
    DBcreation()

topics_db = sqlite3.connect('topics.db')       
cursor = topics_db.cursor()
sentence = input('lets talk about something! ' )
#path = ('C:/University/4006CEM(programming Project)/Topics')
#os.chdir(path)
#dir_path = os.path.dirname(path)
#for root ,dirs, files, in os.walk(dir_path):
#    for file in files:
#        if file.endswith('.txt'):
            #print(file)
#            topic = '{}'.format(file)
#            name = open(file)
#            topic = list((name.read().split(',')))
weather  = 0
sentence_list = list(sentence.split(" "))
cursor.execute('SELECT words FROM weather')
verify = [row[0] for row in cursor]
print(verify)

for i in sentence_list:
    if i in verify:
        weather  += 1
        print(weather)

    

#sport  = 0
#sentence_list = list(sentence.split(" "))
#for i in sentence_list:
#    print (i)
#    if i in topic:
#        sport  = sport+1
#        #print(counter)

#games  = 0
#sentence_list = list(sentence.split(" "))
#for i in sentence_list:
#    print (i)
#    if i in topic:
#        games  = games+1
        #print(counter)
       
