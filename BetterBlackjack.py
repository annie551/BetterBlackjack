import time
import random

print("Welcome to Blackjack. The object of the game is to get as close\nto 21 as you can without going over. Good Luck!\n")

pscore = 0
cscore = 0

plist = []
dlist = []

deck = [i for i in range (1,14)] * 4

again = "yes"

while again == "yes":

    player = 0
    dealer = 0

    plist = []
    dlist = []

    random.shuffle(deck)

    while deck[0]+deck[2]>21:
        random.shuffle(deck)

    plist.append(deck[0])
    plist.append(deck[2])

    dlist.append(deck[1])
    dlist.append(deck[3])

    print("Your Cards:")
    for x in plist:
        print(x)
    print("Dealer's Cards:")
    print("??")
    for y in range(1, len(dlist)):
        print(dlist[y])

    player = deck[0]+deck[2]
    dealer = deck[1]+deck[3]

    del(deck[0])
    del(deck[0])
    del(deck[0])
    del(deck[0])

    hitstand = input("\nHit or Stand\n").lower()
    while hitstand != "hit" and hitstand != "stand":
        hitstand = input("That is not a valid option. Please choose either hit or stand.\n").lower()
    while hitstand == "hit":
        plist.append(deck[0])
        player += int(deck[0])
        del (deck[0])
        print("\nYour Cards:")
        for x in plist:
            print(x)
        print("Dealer's Cards:")
        print("??")
        for y in range(1, len(dlist)):
            print(dlist[y])
        if player > 21:
            print("YOU LOSE! :(")
            cscore += 1
            break
        elif player == 21:
            print("YOU WIN!!!! :)")
            pscore += 1
            break
        else:
            hitstand = input("\nHit or Stand\n")

    if hitstand == "stand":
        print("\nYour Cards:")
        for x in plist:
            print(x)
        print("Dealer's Cards:")
        dlist.append(deck[0])
        dealer += int(deck[0])
        del(deck[0])
        for y in dlist:
            print(y)
        if dealer > 21:
            print("YOU WIN!!! :)")
            pscore += 1
        if dealer == 21:
            print("YOU LOSE! :(")
            cscore += 1
        lossSaid = 0
        if dealer > player and dealer <= 21:
            print("\nYOU LOSE! :(")
            cscore += 1
            lossSaid = 1
        while dealer < player and dealer <= 21:
            time.sleep(2.5)
            print(deck[0])
            dealer += int(deck[0])
            del(deck[0])
            if dealer > player and lossSaid == 0:
                print("YOU LOSE! :(")
                cscore += 1
            elif dealer > 21:
                print("YOU WIN!!! :)")
                pscore += 1

    again = input("\nWould you like to play again? (yes/no)\n").lower()
    while again != "yes" and again != "no":
        again = input("That is not a valid response. Please enter either yes or no.\n")
    if len(deck)<10 and again == "yes":
        print("We have reached near the end of the deck. We will reshuffle the deck.")
        deck = [i for i in range (1,14)]*4


print("YOUR SCORE: %d" % pscore)
print("DEALER SCORE: %d" % cscore)
if pscore > cscore:
    print("Yay! You really know how to play your luck!:)")

elif pscore == cscore:
    print("Damn. You just wasted a damn long time and you didn't even win anything! -_-")

else:
    print("Haha. You lost your money! Remember to not be salty and hope you come back next time!")
