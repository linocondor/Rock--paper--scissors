import random
import figures_rps

print("Rock, Paper, or Scissors")
user = int(input("Type 0 for Rock, 1 for Paper and 2 for Scissors"))

machine = random.randint(0,2)

if user == 0:
    print("You choose rock")
    print(figures_rps.figures[0])
    if machine == 0:
        print("Machine choose rock")
        print(figures_rps.figures[0])
        print("It's a draw")
    elif machine == 1 :
        print("Machine choose paper")
        print(figures_rps.figures[1])
        print("Machine win")
    elif machine == 2 :
        print("Machine choose scissors")
        print(figures_rps.figures[2])
        print("You win")
elif user == 1 :
    print("You choose paper")
    print(figures_rps.figures[1])
    if machine == 0:
        print("Machine choose rock")
        print(figures_rps.figures[0])
        print("You win")
    elif machine == 1 :
        print("Machine choose paper")
        print(figures_rps.figures[1])
        print("It's a draw")
    elif machine == 2 :
        print("Machine choose scissors")
        print(figures_rps.figures[2])
        print("Machine win")
elif user == 2 :
    print("You choose scissor")
    print(figures_rps.figures[2])
    if machine == 0:
        print("Machine choose rock")
        print(figures_rps.figures[0])
        print("Machine win")
    elif machine == 1 :
        print("Machine choose paper")
        print(figures_rps.figures[1])
        print("You win")
    elif machine == 2 :
        print("Machine choose scissors")
        print(figures_rps.figures[2])
        print("It's a Draw")

