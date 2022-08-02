##### Die Simulator ##########

# Game Rules..! 
# if you bring 6 three times you win
# if you bring 1 three times you lose

from random import randint
win_count = 0
lose_count = 0

dice = ['1️⃣','2️⃣','3️⃣','4️⃣','5️⃣','6️⃣']

while True:
    input("Press enter to 🎲Roll dice")
    out = randint(1,6)
    print(f'🎲 => {dice[out-1]}')

    if out == 6:
        win_count+=1
    elif out ==1:
        lose_count+=1
    if win_count == 3:
        print("You win 👑")
        break
    elif lose_count ==3:
        print("You lose ☠️")
        break

#make an edit of consecutive occurence of 6 and 1