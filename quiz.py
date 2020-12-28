from questions_with_answers import questions

import time
start_time = time.time()

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if(answer==question.answer):
            score+=1
    print("You got " + str(score)+" out of " + str(len(questions)) + " right")
    time_taken = round(time.time() - start_time,2)
    print("Time taken to attempt the quiz: " + str(time_taken) + " seconds")
    print("Time taken to answer one question: "+ str(round(time_taken/len(questions),2)) + " seconds")

run_test(questions)