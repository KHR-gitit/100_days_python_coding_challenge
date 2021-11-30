#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

let_pass = ""
let_counter = 0
for let in letters:
  if let_counter < nr_letters:
    ran_num = random.randint(1, len(letters))
    let_pass += letters[ran_num]
    let_counter += 1

sym_pass = ""
sym_counter = 0
for let in symbols:
  if sym_counter < nr_symbols:
    ran_num = random.randint(1, len(symbols))
    sym_pass += symbols[ran_num]
    sym_counter += 1

num_pass = ""
num_counter = 0
for let in symbols:
  if num_counter < nr_numbers:
    ran_num = random.randint(1, len(numbers))
    num_pass += numbers[ran_num]
    num_counter += 1


eazy_new_pass = let_pass + sym_pass + num_pass
print(eazy_new_pass)
     

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P


hard_level_pass = ''.join(random.sample(eazy_new_pass, len(eazy_new_pass)))


print(hard_level_pass)