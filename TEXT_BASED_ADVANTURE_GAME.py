def TextbasedAdventureGame():
    while True:
        a = input("do you want to play this game?....[y/n]")
        
        if a == "n" or a=="N":
            print("okey thanks\nbye.....")
            break
        
        elif a=="y" or a=="Y":
            
            print("okey...lets start")
            
            print("there is two doars infornt of you...")
            
            print("behind one doar their is a monster...if u choose that one it will eat u.\nif u choose other one u will go to the next level ")
            doars=input("which one u want to choose....[L/R]")
            
            if doars=="l"or doars=="L":
                print("opps...wrong doar\nnow monster will eat u.\ntry again.")
                break
            elif doars=="r"or doars=="R":
                print("wahh...very good welcome to the [LEVEL 2]")
                print("come back later.....")


TextbasedAdventureGame()
