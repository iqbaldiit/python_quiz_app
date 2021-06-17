import db_connector as dbc;

class Question:
    def __init__(self):
        self.quistion_id=0
        self.question_description=""

    def getQuestion(self):
        return str(self.quistion_id)+": "+self.question_description
    
    def insertQuestion(self):
        if self.question_description.strip()=="":
            msg="Please insert valid data"
        else:
            cursor=dbc.dbCon.cursor()
            sql="INSERT INTO questions (question_description) VALUES ('"+str(self.question_description)+"')" 
            #val=str(self.question_description)
            cursor.execute(sql)         
            msg=cursor.rowcount, "record inserted."
            dbc.dbCon.commit();
            #dbc.dbCon.close();
        return msg 

    def getQuestions(self):
        if self.question_description.strip()=="":
            msg="Please insert valid data"
        else:
            cursor=dbc.dbCon.cursor()
            #sql="SELECT * FROM questions WHERE question_id<>1 AND question_description like '%"+str(self.question_description)+"%'"
            sql="SELECT * FROM questions WHERE question_id<>0 "
            cursor.execute(sql)         
            result=cursor.fetchall()
            dbc.dbCon.close();            
        return result 
        



