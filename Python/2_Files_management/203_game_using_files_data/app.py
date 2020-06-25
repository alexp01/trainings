
# https://www.udemy.com/course/the-complete-python-course/learn/quiz/4902684#questions

questions_file = open('questions.txt', 'r')
list_of_questions = [line.strip() for line in questions_file.readlines()]
print(list_of_questions)
questions_file.close()

nr_of_good_answers = 0
for list in list_of_questions:
    question, solution = list.split('=')
    answer = input(f'Question : {question} =_')
    if answer == solution:
        nr_of_good_answers += 1

results_file = open ('results.txt', 'w')
results_file.write(f'The corect nr of good answers is {nr_of_good_answers} out of {len(list_of_questions)}')
results_file.close()