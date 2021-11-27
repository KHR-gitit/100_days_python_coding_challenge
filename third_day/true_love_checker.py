# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

# 🚨 Don't change the code above 👆

#Write your code below this line 👇

both_name = (name1 + name2).lower()

true_count = 0

true_count += both_name.count("t")
true_count += both_name.count("r")
true_count += both_name.count("u")
true_count += both_name.count("e")


love_count = 0

love_count += both_name.count("l")
love_count += both_name.count("o")
love_count += both_name.count("v")
love_count += both_name.count("e")

final_score = int(str(true_count) + str(love_count))

if final_score < 10 or final_score > 90:
  print(f"Your score is {final_score}, you go together like coke and mentos.")
elif final_score > 40 and final_score < 50:
  print(f"Your score is {final_score}, you are alright together.")
else:
  print(f"Your score is {final_score}.")