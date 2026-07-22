# Create a programme capable of displaying the questions to the user in KBC 
# Use the concpets of Lists , indexing to display the answer , Loops if you want to display the question one by one 
# Also display the final amount the person is taking hone after playing 

# List of questions
questions = [
    "Who is known as the 'Father of the Nation' in India?",
    "Which planet is known as the Red Planet?",
    "What is the capital of Japan?",
    "Which is the largest ocean on Earth?",
    "In which year did India gain independence?"
]

# List of options for each question (each element is itself a list)
options = [
    ["Jawaharlal Nehru", "Mahatma Gandhi", "Subhas Chandra Bose", "Sardar Patel"],
    ["Earth", "Venus", "Mars", "Jupiter"],
    ["Seoul", "Beijing", "Tokyo", "Bangkok"],
    ["Atlantic", "Indian", "Arctic", "Pacific"],
    ["1945", "1946", "1947", "1948"]
]

# List of correct answers
correct_answers = ["B", "C", "C", "D", "C"]

# List of prize money for each question
prize_money = [1000, 2000, 5000, 10000, 20000]

# List to keep the letter labels for options
labels = ["A", "B", "C", "D"]

print("=" * 50)
print("WELCOME TO KAUN BANEGA CROREPATI - QUIZ GAME")
print("=" * 50)

name = input("Enter your name: ")
print("\nGood luck, " + name + "! Let's begin.\n")

money_won = 0

# Loop through each question using its index
for i in range(len(questions)):

    if still_playing == True:
        print("-" * 50)
        print("Question " + str(i + 1) + " for Rs. " + str(prize_money[i]))
        print(questions[i])

        # Loop through the options list for this question and print them
        for j in range(len(options[i])):
            print(labels[j] + ". " + options[i][j])

        answer = input("Your answer (A/B/C/D): ")
        answer = answer.upper()

        if answer == correct_answers[i]:
            print("Correct answer!")
            money_won = prize_money[i]
            print("Total money won so far: Rs. " + str(money_won))
        else:
            print("Wrong answer!")
            print("The correct answer was: " + correct_answers[i])
            still_playing = False

# After the loop ends, show the final result
print("=" * 50)
print("GAME OVER, " + name + "!")

if still_playing == True:
    print("Congratulations! You answered all questions correctly!")

print("Final amount you are taking home: Rs. " + str(money_won))
print("=" * 50)