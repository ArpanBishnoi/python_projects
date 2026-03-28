from mcq import Question
question_prompt = [
     'Whats the colour of banana ? \n a)yellow , b)orange , c)pink , d)blue ,\n\n' ,
     'Whats the colour of apple ? \n a)pink , b)red , c)blue ,\n\n ' , 
     'Whats the colour of orange ? \n a)blur , b)orange , c)white ,\n\n '  
          ]
questions = [
     Question(question_prompt[0],'a') ,
     Question(question_prompt[1],'b'),
     Question(question_prompt[2],'b'),
     ] 


def run_test (questions):
    score = 0
    for question in questions:     
         answer = input(question.prompt).strip().lower()
         print(f'DEBUG: You typed '+ answer + ' , Correct is '+ question.answer)
         print(f'DEBUG: Are they equal?{answer == question.answer}')
         if answer == question.answer:
             score = score+1
    print( 'Your score is ' + str(score) + ' / ' + str(len(questions)) + '!!!')
run_test(questions)