from global_enum import UserType
import db_connector as dbc;

class User:
    def __init__(self):
        self.user_id=0
        self.user_name=""
        self.email=""
        self.password=""
        self.user_type=UserType.Candidate
        
  
    def insertUser(self):
        cursor=dbc.dbCon.cursor()
        sql="INSERT INTO users (user_id,user_name,email,password,user_type) VALUES ("+str(self.user_id)+","+str(self.user_name)+","+str(self.email)+","+str(self.password)+","+str(int(self.user_type))+")"
        #val=str(self.question_description)
        cursor.execute(sql)         
        msg=cursor.rowcount, "record inserted."
        dbc.dbCon.commit();
        return msg 

    def getUser(self):
        cursor=dbc.dbCon.cursor()        
        sql="SELECT * FROM users WHERE user_id="+str(self.user_id)+" AND password="+str(self.password)+""
        cursor.execute(sql)         
        result=cursor.fetchall()
        dbc.dbCon.close();            
        return result 
 