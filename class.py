import time

print("Choose your Path:Adventure Game./n/n")

name=input("Enter your name:")
age=int(input("Enter your age:"))

health=15

if age >= 10:
    print("Nice! You are old enough to play!")
    start=input("Shall we start the Adventure?").lower()
else:
    print("\nYou are not old enough to play...")
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

        ans = input("\nNice, you follow the path and reach a lake... Do you swim across or go around (across/around)? ")

else:
            count = 0
            while count != 5:
                print(".", end="")
                time.sleep(2/5)
                count += 1

            print("\nYou enter a jungle and get eaten by a bear...")

            ans = input(
                "\nNice, you follow the path and reach a lake... Do you swim across or go around (across/around)? ")

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

                print("\nYou managed to get across, but were bit by a fish.")
                print("You lose 5 health.")
                health -= 5

            ans = input(
                "\nYou notice a house and a river. Which do you go to (river/house)? ")
            if ans == "house":
                count = 0
                while count != 5:
                    print(".", end="")
                    time.sleep(2/5)
                    count += 1
            
                print(
                    "\nYou go to the house and are greeted by the owner... He doesn't like you and hits you with a stick.")
                print("You lose 5 health.")
                health -= 5

                if health <= 0:
                    count = 0
                    while count != 5:
                        print(".", end="")
                        time.sleep(2/5)
                        count += 1
                else:
                    count = 0
                    while count != 5:
                        print(".", end="")
                        time.sleep(2/5)
                        count += 1

                    print("\nYou have survived... You win!")

            print("\nYou enter a jungle and get eaten by a bear...")
            print("\nYou now have 0 health and you lost the game...")
                

        
