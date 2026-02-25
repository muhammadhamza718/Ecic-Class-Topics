import shutil
import pyfiglet

width = shutil.get_terminal_size().columns

text1 = "Institute: Benazir Bhutto Shaheed Human Resource Research & Development Board"
text2 = "Course: Python Programming with AI"

print("\033[1;37;44m" + text1.center(100) + "\033[0m")
print("\033[1;30;47m" + text2.center(100) + "\033[0m")

print()
print()

title = pyfiglet.figlet_format("PyVerse Arcade", font="slant")
for line in title.splitlines():
    print("\033[1;35m" + line.center(width) + "\033[0m")

def rollercoaster():
    print("=== ROLLERCOASTER BOOKING SYSTEM ===")
    print("Welcome to the ultimate theme park experience!")

    count = 0
    revenue = 0
    seniors = 0
    photos = 0

    while True:
        count += 1
        print(f"\nCustomer {count}")
        print("──────────")

        while True:
            h = input("What is your height (in cm)? ")
            if h.isdigit():
                h = int(h)
                break
            print("Invalid input! Please enter a number.")

        if h <= 120:
            print("✗ Sorry, you are too short to ride.")
        else:
            print("✓ Great! You can ride this rollercoaster!")

            while True:
                a = input("How old are you? ")
                if a.isdigit():
                    a = int(a)
                    break
                print("Invalid input! Please enter a number.")

            if a < 12:
                price = 5
                print("Age group: Child (Under 12)")
            elif a <= 18:
                price = 7
                print("Age group: Teenager (12-18)")
            elif 45 <= a <= 55:
                price = 0
                seniors += 1
                print("Age group: Senior (45-55)")
                print("🎉 SPECIAL DISCOUNT! 🎉")
                print("Your ride is completely FREE!")
            else:
                price = 12
                print("Age group: Adult (18+)")

            print(f"Ticket price: ${price}")

            while True:
                p = input("Do you want to buy photos? (yes/no) ").lower()
                if p in ["yes", "no"]:
                    break
                print("Please type 'yes' or 'no'.")

            photo = 3 if p == "yes" else 0
            if photo > 0:
                photos += 1

            total = price + photo
            revenue += total

            print()
            print("==== YOUR BILL ====")
            if price == 0:
                print("Ticket: $0 (Senior Discount!)")
            else:
                print(f"Ticket: ${price}")
            if photo > 0:
                print(f"Photos: +${photo}")
            else:
                print("Photos: $0")
            print("────────────")
            print(f"Total: ${total}")
            if price == 0:
                print("Thank you for celebrating with us!")

        while True:
            again = input("\nProcess another customer? (yes/no) ").lower()
            if again in ["yes", "no"]:
                break
            print("Please type 'yes' or 'no'.")

        if again == "no":
            break

    print("\n=== SESSION SUMMARY ===")
    data = [
        ("Total Customers Processed", count),
        ("Total Revenue", f"${revenue}"),
        ("Photo Packages Sold", photos),
        ("Senior Free Rides", seniors),
    ]
    for label, value in data:
        print(f"{label}: {value}")

    if count > 0:
        avg = revenue / count
        print(f"Average Revenue per Customer: ${avg:.2f}")

    print("Thank you for visiting!")


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


def space():
    while True:
        print("=== SPACE MISSION CONTROL ===")
        print("Welcome, Astronaut. Your mission briefing begins now.")
        print()

        while True:
            name = input("Enter your full name: ").strip()
            if name.replace(" ", "").isalpha() and len(name) >= 2:
                break
            print("Invalid input! Please enter letters only.")

        sign = name[:3].upper()
        print(f"✓ Identity confirmed. Your call sign is: [{sign}]")
        print()

        while True:
            h = input("Enter your health score (0-100): ")
            if h.isdigit():
                h = int(h)
                if 0 <= h <= 100:
                    break
                print("Score must be between 0 and 100.")
            else:
                print("Invalid input! Please enter a number.")

        if h < 75:
            print(f"✗ Health score {h}/100 — BELOW MINIMUM (75).")
            print(f"Sorry [{sign}], you are not cleared for this mission.")
            print("Please visit the medical bay and try again.")
        else:
            print(f"✓ Health score {h}/100 — CLEARED!")
            print()

            print("=== CHOOSE YOUR DESTINATION ===")
            print("  1. Moon    — Risk: LOW    | Fuel needed: 50%")
            print("  2. Mars    — Risk: MEDIUM | Fuel needed: 75%")
            print("  3. Jupiter — Risk: HIGH   | Fuel needed: 90%")
            print()

            while True:
                dest = input("Choose your destination (moon/mars/jupiter): ").lower().strip()
                if dest in ["moon", "mars", "jupiter"]:
                    break
                print("Invalid! Please type: moon, mars, or jupiter.")

            if dest == "moon":
                risk = "LOW"
                need = 50
                emoji = "🌕"
                days = "3 days"
            elif dest == "mars":
                risk = "MEDIUM"
                need = 75
                emoji = "🔴"
                days = "7 months"
            else:
                risk = "HIGH"
                need = 90
                emoji = "🪐"
                days = "2 years"

            print(f"{emoji} Destination: {dest.upper()} | Risk: {risk} | Duration: {days}")
            print()

            print("=== EQUIPMENT CHECKLIST ===")
            items = ["Oxygen Tank", "Space Suit", "Navigation Computer"]
            ready = True

            for item in items:
                while True:
                    check = input(f"Is your {item} ready? (yes/no): ").lower().strip()
                    if check in ["yes", "no"]:
                        break
                    print("Please type 'yes' or 'no'.")
                if check == "yes":
                    print(f"  ✓ {item} — OK")
                else:
                    print(f"  ✗ {item} — MISSING")
                    ready = False

            print()

            while True:
                f = input("Enter current fuel level (0-100): ")
                if f.isdigit():
                    f = int(f)
                    if 0 <= f <= 100:
                        break
                    print("Fuel must be between 0 and 100.")
                else:
                    print("Invalid input! Please enter a number.")

            print()
            print("==== LAUNCH REPORT ====")
            print(f"Astronaut  : {name} [{sign}]")
            print(f"Health     : {h}/100")
            print(f"Destination: {dest.upper()} {emoji}")
            print(f"Risk Level : {risk}")
            print(f"Fuel       : {f}% (Required: {need}%)")
            print(f"Equipment  : {'ALL CLEAR ✓' if ready else 'INCOMPLETE ✗'}")
            print("────────────────────────")

            if ready:
                if f >= need:
                    if risk == "LOW":
                        print("🟢 ALL SYSTEMS GO!")
                        print(f"🚀 Launching to the MOON, Astronaut [{sign}]!")
                        print("Safe travels. See you in 3 days. 🌕")
                    elif risk == "MEDIUM":
                        print("🟡 ALL SYSTEMS GO — CAUTION ADVISED!")
                        print(f"🚀 Launching to MARS, Astronaut [{sign}]!")
                        print("A bold mission. Good luck out there. 🔴")
                    else:
                        print("🔴 ALL SYSTEMS GO — EXTREME MISSION!")
                        print(f"🚀 Launching to JUPITER, Astronaut [{sign}]!")
                        print("You are one of the bravest astronauts alive. 🪐")
                else:
                    print("⛽ LAUNCH ABORTED — INSUFFICIENT FUEL!")
                    print(f"You need {need}% fuel but only have {f}%.")
                    print("Please refuel and try again.")
            else:
                if f >= need:
                    print("🔧 LAUNCH ABORTED — EQUIPMENT INCOMPLETE!")
                    print("Fuel is ready but missing equipment is a safety risk.")
                    print("Complete your checklist and return for re-screening.")
                else:
                    print("🚫 LAUNCH ABORTED — MULTIPLE ISSUES DETECTED!")
                    print("Both equipment and fuel requirements are not met.")
                    print("Report to Mission Control for a full systems check.")

        print()
        again = input("Play again? (yes/no) ").lower()
        if again != "yes":
            print("Thanks for playing! Mission Control out. 🚀")
            break


while True:
    print()
    print("╔══════════════════════════════════╗")
    print("║       🎮  PYVERSE ARCADE  🎮    ║")
    print("╠══════════════════════════════════╣")
    print("║  1.  🎢  Rollercoaster           ║")
    print("║  2.  🏝️  Treasure Island         ║")
    print("║  3.  🚀  Space Mission Control   ║")
    print("║  4.  🚪   Exit                   ║")
    print("╚══════════════════════════════════╝")
    print()

    while True:
        pick = input("Choose a game (1/2/3/4): ")
        if pick in ["1", "2", "3", "4"]:
            break
        print("Please enter 1, 2, 3, or 4.")

    if pick == "4":
        print("Thanks for playing PyVerse Arcade! Goodbye! 👋")
        break

    print()

    if pick == "1":
        rollercoaster()
    elif pick == "2":
        treasure()
    elif pick == "3":
        space()

    print()
    while True:
        action = input("Back to main menu? (yes/no) ").lower()
        if action in ["yes", "no"]:
            break
        print("Please type 'yes' or 'no'.")

    if action == "no":
        print("Thanks for playing PyVerse Arcade! Goodbye! 👋")
        break