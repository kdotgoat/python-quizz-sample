from question import Question


questions_prompt = [
    "What is the capital city of Kenya?\n(a)Kampala\n(b)Nairobi\n(c)Dodoma",
    "When did Kenya gain independence?\n(a)1953\n(b)1888\n(c)1963",
    "Largest body organ?\n(a)Skin\n(b)Liver\n(c)Lungs"
]


questions = [
    Question(questions_prompt[0], "b"),
    Question(questions_prompt[1], "c"),
    Question(questions_prompt[2], "a"),
]


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1  # Corrected the increment operator
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")  # Fixed concatenation

run_test(questions)
