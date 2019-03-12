
# first writing a question array.
# then create a question class.
# create another array for questions using question object.
# define a function to conduct the quiz.
# call the function


from question_class import Question

question_array = [
    "\nWhat is the color of Apple\n(a) Orange\n(b) Red\n(c)Green\n\n",
    "\nWhat is the color of Banana\n(a) Orange\n(b) Yellow\n(c)Green\n\n",
    "\nWhat is the color of Strawberry\n(a) Orange\n(b) Red\n(c)Green\n\n",
]

Questions = [
    Question(question_array[0], "b"),
    Question(question_array[1], "b"),
    Question(question_array[2], "b")
]


def run_test(Questions):
    score = 0
    for question in Questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1

    print ("You got "+ str(score)+" out of "+str(len(Questions))+" correct")


run_test(Questions)