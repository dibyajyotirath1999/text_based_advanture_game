def treasurehunt():
    name=input("enter your name:")
    print("hello {}...welcome to the game".format(name))
    while True:
        a = input("do you want to play this game?....[y/n]")
        if a == "n" or a=="N":
            print("okey thanks {}\nbye.....".format(name))
            break
        elif a=="Y"or a=="y":
            print("okey {}...lets start".format(name))
            print("there is two doars infornt of you...")
            print("behind one doar their is a monster...if u choose that one it will eat u.\nif u choose other one u will go to the next level ")
            doars=input("which one u want to choose....[L/R]")
            if doars=="l"or doars=="L":
                print("opps...wrong doar\nnow monster will eat u.\try again.")
                break
            elif doars=="r"or doars=="R":
                print("good job!!!... {} \nwelcome to the level2\n************[LEVEL 2]***************".format(name))
                print("infront of you there is 3 doars..")
                print("behind one doar ..there will be a monster\nbehind 2nd doar there will some diamonds...u can pic it and go....\nif u choose the correct one u will go to the final level")
                l2doars=input(" okey now there is 3 doars infront of u...\nwhich one u want to choose [L/M/R]")
                if l2doars=="l" or l2doars=="L":
                    print("okey..better luck next time...be happy with some diamonds")
                    break
                elif l2doars=="m" or l2doars=="M":
                    print(" sorry {} gandi mareilu re pua....jaa ! garaku pala..".format(name))
                    break
                elif l2doars=="r" or l2doars=="R":
                    print("wow..great {} ow you r in the final level\n************ FINAL LEVEL ***************".format(name))
                    f=input("in the final level...there is two doars.....what u want to choose [L/R]")
                    if f=="l" or f=="L":
                        print("gala...bara brsa ra tapasya sukhua poda re gala...\n chhii!!!...")
                        break
                    elif f=="r" or f=="R":
                        print("wooooohoo.....you got it {}..yo found the treasur..\ncongrats...\n$$$$$$$$ TRESURE FOUND $$$$$$$$$$$$$".format(name))
                        break






treasurehunt()
