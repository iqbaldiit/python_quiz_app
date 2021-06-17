from global_enum import UserType
import question
import answer
import user

adminQuestion=question.Question();
adminQuestion.question_description="What is cloud Computing?"
print(adminQuestion.insertQuestion())

# adminAnswer=answer.Answer()
# adminAnswer.question_id=11
# adminAnswer.answer_description="D"
# adminAnswer.is_correct=False
# print(adminAnswer.insertAnswer())

# adminUser=user.User()
# adminUser.user_id=1
# adminUser.user_name="masud"
# adminUser.password="123456"
# adminUser.user_type="1"
#print(adminUser.insertUser())
#as=list(adminUser.getUser())