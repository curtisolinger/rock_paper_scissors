import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

graphic = [rock, paper, scissors]

while True:
  try:
    choice0 = int(input("What do you choose? Type 0 for rock, 1 for paper, or 2 for Scissors.\n"))
  except ValueError:
    print("Invalid input")
  else:
    if choice0 in range(3):
      break
    else:
      print("Invalid input")


print(graphic[choice0])
if graphic[choice0] == rock:
  print("You choose a rock,")
elif graphic[choice0] == paper:
  print("You choose paper,")
else:
  print("You choose scissors,")


choice1 = random.choice(graphic)
print(choice1)
if choice1 == rock:
  print("and the computer choose a rock.", end=" ")
elif choice1 == paper:
  print("and the computer choose paper.", end=" ")
else:
  print("and the comnputer choose scissors.", end=" ")


if graphic[choice0] == choice1:
  print("It's a tie")
elif graphic[choice0] == rock and choice1 != scissors:
  print("You lose!")
elif graphic[choice0] == paper and choice1 != rock:
  print("You lose!")
elif graphic[choice0] == scissors and choice1 != paper:
  print("You lose!")
else:
  print("You win!")