import shutil
import pyfiglet

width = shutil.get_terminal_size().columns

# ── Institute big block text ───────────────────────────────
institute_art = pyfiglet.figlet_format("BBSHRDB", font="banner").replace("#", "█")
for line in institute_art.splitlines():
    print("\033[1;97m" + line.center(width) + "\033[0m")

# Full name small below it
text1 = "Institute: Benazir Bhutto Shaheed Human Resource Research & Development Board"
print("\033[1;97m" + text1.center(width) + "\033[0m")

print()

# ── Course — use "small" font so it fits in one line ──────
course_art = pyfiglet.figlet_format("Python with AI", font="small").replace("#", "█")
for line in course_art.splitlines():
    print("\033[1;96m" + line.center(width) + "\033[0m")

# Full course name small below it
text2 = "Course: Python Programming with AI"
print("\033[1;96m" + text2.center(width) + "\033[0m")

print()
print()

def treasure():
    while True:
        print("=== WELCOME TO TREASURE ISLAND ===")
        print("Your mission is to find the treasure.")
        print()

        choice = input("Do you go left or right? ").lower()

        if choice == "left":
            print("You go left. The path opens to a river.")
            print()

            choice = input("Do you swim or wait? ").lower()

            if choice == "wait":
                print("You wait by the river. You hear mysterious sounds...")
                print()
                print("A cave reveals three doors: red, blue, yellow.")

                door = input("Which door do you choose? (red/blue/yellow) ").lower()

                if door == "yellow":
                    print()
                    print("⭐ CONGRATULATIONS! ⭐")
                    print("You found the treasure!")
                elif door == "red":
                    print("Burned by fire. Game Over.")
                elif door == "blue":
                    print("Eaten by beasts. Game Over.")
                else:
                    print("Invalid choice. Game Over.")
            else:
                print("Attacked by trout. Game Over.")
        else:
            print("You fall into a hole. Game Over.")

        print()
        again = input("Play again? (yes/no) ").lower()
        if again != "yes":
            print("Thanks for playing! Goodbye!")
            break


while True:
    print()
    print("╔══════════════════════════════════╗")
    print("║       🎮  PYVERSE ARCADE  🎮    ║")
    print("╠══════════════════════════════════╣")
    print("║  1.  🏝️  Treasure Island         ║")
    print("║  2.  🚪   Exit                   ║")
    print("╚══════════════════════════════════╝")
    print()

    while True:
        pick = input("Choose a game (1/2): ")
        if pick in ["1", "2"]:
            break
        print("Please enter 1 or 2")

    if pick == "2":
        print("Thanks for playing PyVerse Arcade! Goodbye! 👋")
        break

    print()

    if pick == "1":
        treasure()

    print()
    while True:
        action = input("Back to main menu? (yes/no) ").lower()
        if action in ["yes", "no"]:
            break
        print("Please type 'yes' or 'no'.")

    if action == "no":
        print("Thanks for playing PyVerse Arcade! Goodbye! 👋")
        break