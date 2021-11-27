# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if year % 4:
  print("Not leap year.")
else:
  if year % 100:
    print("Leap year.")
  else:
    if year % 400:
      print("Not leap year.")
    else:
      print("Leap year.")

