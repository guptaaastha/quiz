from questions_with_answers import questions

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if(answer==question.answer):
            score+=1
    print("You got " + str(score)+" out of " + str(len(questions)) + " right")

run_test(questions)
