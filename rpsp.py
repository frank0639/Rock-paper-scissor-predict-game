import random
from rpsp_pkg import rpsp_rock
from rpsp_pkg import rpsp_paper
from rpsp_pkg import rpsp_scissor
from rpsp_pkg import rpsp_predict


wins = 0 
health = 250
player_hp = health


def game():
    global wins
    global player_hp
    print("\n Your health is: ", player_hp)

    while True:

        cpu_options = ("rock" , "paper" , "scissor" , "predict")
        cpu_pick = random.choice(cpu_options)

        print(" Rock, Paper, Scissor, PREDICT! \n")

        print("1) Rock ")
        print("2) Paper ")
        print("3) Scissor ")
        print("4) Predict ")
        print("5) Quit ")

        player_choice = str.lower(input(" Choose an option : "))              #player chosing among: "Rock, Paper, Scissor, or Predict"
        if player_choice == "1" or player_choice == "rock":
            rpsp_rock.rock(cpu_pick, player_choice)
        elif player_choice == "2" or player_choice == "paper":                # Paper starts
            rpsp_paper.paper(cpu_pick, player_choice)
        elif player_choice == "3" or player_choice == "scissor":
            rpsp_scissor.scissor(cpu_pick, player_choice)
        elif player_choice == "4" or player_choice == "predict":
            rpsp_predict.predict(cpu_pick, player_choice)
        elif player_choice == "5" or player_choice == "quit":
                print("Thank You For Playing   --  Goodbye!  --")
                quit()
        else:
            print("Invalide option, please select '1 - 5' \n")
            continue

game()
