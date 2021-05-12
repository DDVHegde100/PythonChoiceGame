import time

print("Choose your Path:Adventure Game./n/n")

name=input("Enter your name:")
age=int(input("Enter your age:"))

health=10

if age >= 3:
    print("Nice! You are old enough to play!You aren't a literal baby.")
    start=input("Shall we start the Adventure?").lower()
else:
    print("\nHow did you even get access to this program? You are not old enough to play...")
    print("\nExiting...")
    count = 0
    while count != 5:
        print(".", end="")
        time.sleep(2/5)
        count += 1
    print()

if(start=="yes" or (start=="y")):
        print("Starting.../n")
        time.sleep(1)
        print("Loading...")
        time.sleep(1)
        count=0
        while count !=5:
            print(".", end="")
            time.sleep(2/5)
            count += 1

        print("/nYou are starting with", health, "health.")
        print("Let's play!/n")

        time.sleep(2)

        left_or_right = input("First choice... Left or Right (left/right)? ")
if left_or_right == "left":
             
        while count != 5:
                print(".", end="")
                time.sleep(2/5)
                count += 1

        ans = input("\nAs you move left, you spot a shallow lake. Do you swim across or go around (across/around)? ")

else:
            count = 0
            while count != 5:
                print(".", end="")
                time.sleep(2/5)
                count += 1

            print("\nYou enter the forest, and fall into a thick anthill full of bullet ants. They engulf you and you die a brutal death...")
            

            if ans == "around":
                count = 0
                while count != 5:
                    print(".", end="")
                    time.sleep(2/5)
                    count += 1

                print("\nYou went around and reached the other side of the lake.")
            elif ans == "across":
                count = 0
                while count != 5:
                    print(".", end="")
                    time.sleep(2/5)
                    count += 1

                print("\nAs you were swimming through, you were bitten by a few piranha. You managed to get across but have accumulated several minor injuries.")
                print("You lose 5 health.")
                health -= 5

            ans = input(
                "\nAs you continue, you notice an old cabin next to a rapid river. Which do you go to (river/house)? ")
            if ans == "house":
                count = 0
                while count != 5:
                    print(".", end="")
                    time.sleep(2/5)
                    count += 1
            
                print(
                    "\nYou move toward the house and slowly open. To your surpise, a man is there, who doesn't seem happy with your entrance. He hits you with a stick and chases you out.")
                print("You lose 5 health.")
                health -= 5
            else:
                count = 0
                while count != 5:
                    print(".", end="")
                    time.sleep(2/5)
                    count += 1
            
                print(
                    "\nYou trad across the river on a sheet of wood you found. You manage to get across and find that you have reached the end of the forest.")
                
                if health <= 0:
                    count = 0
                    while count != 5:
                        print(".", end="")
                        time.sleep(2/5)
                        count += 1
                        print("\nYou lost all your health through this adventure, and youhave died.")
                else:
                    count = 0
                    while count != 5:
                        print(".", end="")
                        time.sleep(2/5)
                        count += 1
                        print("\You have survived this perilous journey. Good Job, you have won the game!")
                    

            
            
                

        
