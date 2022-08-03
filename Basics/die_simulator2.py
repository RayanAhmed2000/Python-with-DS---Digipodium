
##### Die Simulator ##########

# Game Rules..! 
# Consective 3 times 6 results in victory
# Consective 3 times 1 results in loss
  

from random import randint
win_streak = 0
count=0
lose_streak = 0

dice = ['1️⃣','2️⃣','3️⃣','4️⃣','5️⃣','6️⃣']
       # 0     1    2     3    4     5    

while True:
    input("Press enter to 🎲 Roll dice")
    out = randint(1,6)
    print(f'🎲 => {dice[out-1]}')

    if out == 6:
        win_streak+=1
        print("win_streak= ",win_streak)
    else:
        win_streak=0
    if out ==1:
        lose_streak+=1
        print("lose_streak= ",lose_streak)
    
    else:
        lose_streak=0


    if win_streak == 3:
        print("You win 👑")
        break
    elif lose_streak ==3:
        print("You lose ☠️")
        break
   