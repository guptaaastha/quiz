from Question import Question
from questions import question_prompts
from answers import answers

questions = []

for prompt,answer in zip(question_prompts,answers) :
    questions.append(Question(prompt,answer))
