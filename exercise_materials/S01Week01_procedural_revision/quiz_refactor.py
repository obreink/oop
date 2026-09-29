questions = [
    {"question": "What is 2 + 2?", "answer": "4"},
    {"question": "What colour is the sky?", "answer": "blue"},
    {"question": "How many days are in a week?", "answer": "7"}
]
score = 0
for question in questions:
    print(question["question"])
    answer = input("Your answer: ")

    if answer.lower() == question["answer"].lower():
        print("Correct!")
        score = score + 1
    else:
        print("Incorrect!")

print("You scored", score, "out of", len(questions))