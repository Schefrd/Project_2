import random

print("Hi there!")
print("----------------------------------------")
print("I've generated a random 4 digit number for you. Let's play a bulls and cows game.")
print("----------------------------------------")

# vytvoření tajného čísla
cisla = ['0','1','2','3','4','5','6','7','8','9']
prvni = random.choice(['1','2','3','4','5','6','7','8','9'])
ostatni = cisla.copy()
ostatni.remove(prvni)
tajne = prvni + ''.join(random.sample(ostatni,3))

pokusy = 0

while True:
    tip = input("Enter a number: ")
    pokusy += 1

    if len(tip) != 4:
        print("The number must have 4 digits.")
        continue
    if not tip.isdigit():
        print("Input numbers only.")
        continue
    if tip[0] == '0':
        print("It must not contain 0 at the beginning.")
        continue
    if len(set(tip)) != 4:
        print("No repeating digits.")
        continue

    # vypocet
    bulls = 0
    cows = 0
    for i in range(4):
        if tip[i] == tajne[i]:
            bulls += 1
        elif tip[i] in tajne:
            cows += 1

    if bulls == 1:
        bull_txt = "bull"
    else:
        bull_txt = "bulls"
    if cows == 1:
        cow_txt = "cow"
    else:
        cow_txt = "cows"
    # vysledek
    print(bulls, bull_txt, ",", cows, cow_txt)
    print("----------------------------------------")

    if bulls == 4:
        print("Congrats! Secret number was ", tajne, "and you hit it on the ", pokusy, ". try.")
        break

