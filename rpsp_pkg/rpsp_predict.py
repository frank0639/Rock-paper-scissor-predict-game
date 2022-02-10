health = 250
player_hp = health
rock_dmg = 30
paper_dmg = 50
scissor_dmg = 20

wins = 0

def predict(cpu_pick, player_choice):
    global wins
    global player_hp

    player_choice = "predict"
    cpu_choice = cpu_pick
    print( " you picked .... predict")
    print( " Opponent picked ...." , cpu_choice )
    if cpu_choice == "predict":                                       #outcome for Predict
        print( "... Succefful Prediction!  ")
        print(" Your health increased by 70")
        player_hp += 70
        print("your health is now: ", player_hp)
        wins += 1
        print("wins: ", wins)
    elif player_choice == "predict" and cpu_choice == "paper":
        print(" ... Failed Prediction!  \n")
        player_hp -= 2 * paper_dmg
        if player_hp <= 0:
            player_hp = 0

            while True:
                print("GAME OVER! ")                                      #Game Over
                print("your total wins are: ", wins)
                new_game = str.lower(input("do you want to play again?  yes or no : "))
                if new_game == "yes":
                    player_hp = health
                    wins = 0
                    break
                elif new_game == "no":
                    print("Goodbye! ")
                    quit()
                else:
                    print("Invalide option, please type 'yes' or 'no' :  \n")
                    continue
        print("your health is now: ", player_hp)

    elif player_choice == "predict" and cpu_choice == "rock":
        print(" ... Failed Prediction!  \n")
        player_hp -=2 * rock_dmg
        if player_hp <= 0:
            player_hp = 0

            while True:
                print("GAME OVER! ")                                      #Game Over
                print("your total wins are: ", wins)
                new_game = str.lower(input("do you want to play again?  yes or no : "))
                if new_game == "yes":
                    player_hp = health
                    wins = 0
                    break
                elif new_game == "no":
                    print("Goodbye! ")
                    quit()
                else:
                    print("Invalide option, please type 'yes' or 'no' :  \n")
                    continue
        print("your health is now: ", player_hp)

    elif player_choice == "predict" and cpu_choice == "scissor":
        print(" ... Failed Prediction!  \n")
        player_hp -= 2 * scissor_dmg
        if player_hp <= 0:
            player_hp = 0

            while True:
                print("GAME OVER! ")                                      #Game Over
                print("your total wins are: ", wins)
                new_game = str.lower(input("do you want to play again?  yes or no : "))
                if new_game == "yes":
                    player_hp = health
                    wins = 0
                    break
                elif new_game == "no":
                    print("Goodbye! ")
                    quit()
                else:
                    print("Invalide option, please type 'yes' or 'no' :  \n")
                    continue
        print("your health is now: ", player_hp)