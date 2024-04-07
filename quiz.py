questions_and_options = [
    ("What is the correct way to create a function in Python?", ["function myFunc():", "def myFunc():", "create myFunc()", "function: myFunc()", "new Function myFunc()"]),
    ("What do you type to print something in Python?", ["echo", "print", "say", "write", "output"]),
    ("Which one is a Python list?", ["{1, 2, 3}", "1, 2, 3", "[1, 2, 3]", '{"one":1, "two":2}', "1 2 3"]),
    ("What symbol is used to add comments in Python?", ["//", "<!-- -->", "/* */", "#", "--"]),
    ("If you want to repeat something 5 times, what Python code do you use?", ["repeat(5):", "for i in 5:", "for i in range(5):", "while 5:", "do 5 times:"])
]

correct_answers = [2, 2, 3, 4, 3]
score = 0
print("Welcome to the Quiz!")
for i, (question, options) in enumerate(questions_and_options):
    print(f"\nQuestion {i+1}: {question}")
    for idx, option in enumerate(options):
        print(f"{idx+1}. {option}")
    user_answer = int(input("Enter your answer (1-5): "))
    if user_answer == correct_answers[i]:
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
print(f"\nYou scored {score} out of {len(questions_and_options)}.")