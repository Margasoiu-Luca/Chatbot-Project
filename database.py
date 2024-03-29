import sqlite3
import os

#Check to see if the database files do not exist
if os.path.isfile('userinfo.db') is False:
    #Creates the staff login database 
    userinfo_db = sqlite3.connect('userinfo.db')  #Creates a connection to the database file
    cursor = userinfo_db.cursor()                    #Cursor object is called up using this variable
    cursor.execute('''                   
    CREATE TABLE IF NOT EXISTS logindetails(
    userID INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    firstname TEXT NOT NULL,
    lastname TEXT NOT NULL);
    ''')                                                #Creates the table if it does not exist in the database    

    cursor.execute('''                   
    CREATE TABLE IF NOT EXISTS extrainfo(
    ID INTEGER PRIMARY KEY,
    twitter TEXT NOT NULL, 
    favteam TEXT NOT NULL,
    favplayer TEXT NOT NULL,
    FOREIGN KEY(ID) REFERENCES logindetails(userID));
    ''')
    
    userinfo_db.commit()                                #Commits the statements, which saves changes made
    userinfo_db.close()                                 #Closes the database  

def start():
    login = 0
    user_info_db = sqlite3.connect('userinfo.db')
    cursor = user_info_db.cursor()
    startup = input("are you a new user?  (y/n): ")
    if startup == 'y':
        newusername = input('Please enter a new username: ')
        newpassword = input('Please enter a new password: ')
        newfirstname = input('Please enter a new first name: ')
        newlastname = input('Please enter a new last name: ')
        TwitterHandle = input('Please enter your Twitter Handle: ')
        FavTeam = input('Please enter your favourite team: ')
        FavPlayer = input('Please enter your favourite player: ')
        if len(newusername) == False or len(newpassword)== False or len(newfirstname)== False or len(newlastname)== False or len(TwitterHandle)== False or len(FavTeam)== False or len(FavPlayer)== False:
            print("Please fill in all boxes. Start Again.")
            start()
        else:
            if newfirstname.isalpha() is False or newlastname.isalpha() is False:    
                print("First Name and Last Name must be characters. Start Again")
                start()
            else:
                #Checks to see if user input matches data in database  
                cursor.execute(('SELECT username FROM logindetails WHERE username=?'),[newusername])
                exists=cursor.fetchone()  
                if exists:
                    print("Username already exists. Start Again.")
                else:
                    cursor.execute('''INSERT INTO logindetails(username,password,firstname,lastname)
                                   VALUES(?,?,?,?)''',[newusername,newpassword,newfirstname,newlastname])
                    cursor.execute('''INSERT INTO extrainfo(twitter,favteam,favplayer)
                                   VALUES(?,?,?)''',[TwitterHandle,FavTeam,FavPlayer])
                    user_info_db.commit()
                    print("New User Created")
                    print("Welcome",newfirstname,newlastname)
                    print("Your favourite team is:",FavTeam)
                    print("Your favourite player is:",FavPlayer)
                    cursor.execute(('SELECT userID FROM logindetails WHERE username=?'),[newusername])
                    log=cursor.fetchone()
                    login = log
                    print("userid",login)
        
                
    elif startup == 'n':
        print("Please Log In!")
        username = input("Username: ")
        password = input("Password: ")
        user_info_db = sqlite3.connect('userinfo.db')
        cursor = user_info_db.cursor()
        cursor.execute(('SELECT * FROM logindetails WHERE username = ? AND password = ?'),[username,password]) 
        verify=cursor.fetchall()
        if verify:
            for i in verify:
                name = (i[3],i[4])
                print("Welcome",name)
                cursor.execute(('SELECT userID FROM logindetails WHERE username=?'),[username])
                log=cursor.fetchone()
                login = log
                print("userid",login)
                
                
                
        else:
            print('Denied')
    else:
        print('That input is not recognised')
        start()
start()

