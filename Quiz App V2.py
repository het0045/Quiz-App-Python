print("=== Welcome To Quiz App ===")
print("Answer by typing A,,B,C or D")
print()


questions = [
{
    "question" : "What is the capital of India?",
    "options" : ["A. Mumbai","B. Delhi","C. Chennai", "D. Kolkata"],
    "answer" : "B"
},
{
    "question" : "2 + 2 = ?",
    "options" : ["A. 3","B. 4","C. 5","D. 6"],
    "answer" : "B"
},
{
    "question" : "Python was created by ?",
    "options" : ["A. Guido van Rossum","B. Elon Musk","C. James Gosling", "D. Bill Gates"],
    "answer" : "A"
}
]    

score = 0
for i,question in enumerate(questions, start = 1):

    print(f" \nQuestion{i}")
    print(question["question"])
    print("-" * 30)

    for option in question["options"] :  
        print(option)

    user_answer = input("Enter Your Answer: ").upper() 

    while user_answer not in ["A","B","C","D"]:
        print("Invalid Choice!")
        user_answer = input("Enter Your Answer: ").upper()

    if user_answer == question["answer"]:
     print("Correct!")
     score += 1
    else:
     print("Wrong!")
     print("The Correct Answer Is :", question["answer"] )

print(f"\nFinal Score :{score}/{len(questions)}")

if score == len(questions):
   print("Outstanding! Perfect Score!🏆")
elif score >= 2:
   print("Good Job!👍")
else:
   print("Keep Practicing!💪")