
print("===================================")
print("          PYTHON QUIZ GAME")
print("===================================")

score = 0

# Question 1
print("\n1. Python kis type ki language hai?")
print("A. Programming Language")
print("B. Operating System")
print("C. Browser")
print("D. Database")

answer = input("Enter your answer: ").upper()

if answer == "A":
    print("Correct! ✅")
    score += 1
else:
    print("Wrong! ❌")


# Question 2
print("\n2. Python file ka extension kya hota hai?")
print("A. .java")
print("B. .py")
print("C. .html")
print("D. .sql")

answer = input("Enter your answer: ").upper()

if answer == "B":
    print("Correct! ✅")
    score += 1
else:
    print("Wrong! ❌")


# Question 3
print("\n3. Python mein output ke liye kya use hota hai?")
print("A. input()")
print("B. print()")
print("C. output()")
print("D. display()")

answer = input("Enter your answer: ").upper()

if answer == "B":
    print("Correct! ✅")
    score += 1
else:
    print("Wrong! ❌")


# Question 4
print("\n4. Python mein comment ke liye kya use hota hai?")
print("A. //")
print("B. <!-- -->")
print("C. #")
print("D. **")

answer = input("Enter your answer: ").upper()

if answer == "C":
    print("Correct! ✅")
    score += 1
else:
    print("Wrong! ❌")


# Question 5
print("\n5. Python mein list banane ke liye kya use hota hai?")
print("A. ()")
print("B. {}")
print("C. []")
print("D. <>")

answer = input("Enter your answer: ").upper()

if answer == "C":
    print("Correct! ✅")
    score += 1
else:
    print("Wrong! ❌")


# Final Result
print("\n===================================")
print("             RESULT")
print("===================================")

print("Your Score:", score, "/ 5")

if score == 5:
    print("Excellent! 🏆")

elif score >= 3:
    print("Good Job! 👍")

else:
    print("Keep Practicing! 💪")
