import db_connector as dbc;

class Answer:
    def __init__(self):
        self.answer_id=0
        self.question_id=0
        self.answer_description=""
        self.is_correct=False
        pass
  
    def insertAnswer(self):
        if self.answer_description.strip()=="" or self.question_id<=0:
            msg="Please insert valid data"
        else:
            cursor=dbc.dbCon.cursor()
            sql="INSERT INTO answers (question_id,answer_description,is_correct) VALUES ("+str(self.question_id)+",'"+str(self.answer_description)+"',"+str(self.is_correct)+")"
            #val=str(self.question_description)
            cursor.execute(sql)         
            msg=cursor.rowcount, "record inserted."
            dbc.dbCon.commit();
        return msg 

    def getAnswers(self):
        if self.question_id<=0:
            msg="Please select question"
        else:
            cursor=dbc.dbCon.cursor()
            #sql="SELECT * FROM questions WHERE question_id<>1 AND question_description like '%"+str(self.question_description)+"%'"
            sql="SELECT * FROM answers WHERE answer_id<>0 AND question_id="+self.question_id+""
            cursor.execute(sql)         
            result=cursor.fetchall()
            dbc.dbCon.close();            
        return result 
        