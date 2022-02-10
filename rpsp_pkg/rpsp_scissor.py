health = 250
player_hp = health
rock_dmg = 30
predict_dmg = 35

wins = 0

def scissor(cpu_pick, player_choice):
    global wins
    global player_hp

    player_choice = "scissor"
    cpu_choice = cpu_pick
    print( " you picked .... scissor")
    print( " Opponent picked ...." , cpu_choice )
    if cpu_choice == "scissor":                                          #outcome for Rock
        print( "... Its a Tie! ")
        print( "Your health is still: " , player_hp)
    elif player_choice == "scissor" and cpu_choice == "paper":
        print(" ... You Won the Round  \n")
        print( "Your health is still: " , player_hp)
        wins += 1 
        print("wins: ", wins)
    elif player_choice == "scissor" and cpu_choice == "rock":
        print(" ... You lost the Round  \n")
        player_hp -= rock_dmg
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

    elif player_choice == "scissor" and cpu_choice == "predict":
        print(" ... You lost the Round  \n")
        player_hp -= predict_dmg
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
