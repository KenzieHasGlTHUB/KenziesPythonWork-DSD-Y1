# Task 1: Arcade Machine Dictionary

arcade = {
    "Pinball Wizard": "Category": "Pinball", "Status",: "Working"
    "Retro Racer": "Category": "Racing", "Status",: "Out of Order"
}
print("What would you like to do?")

print("1) View all machines")
print("2) Add a new machine")
print("3) Update a machine's status")
print("4) Delete a machine entry")
option=input("Please select now: ")

if option == "1":
    print(arcade)

elif option == "2":
    arcade.update = ({"Zombies Shootout": "Category": "1st Person Shooter", "Status",: "Working"})

elif option == "3":
    arcade.update({"Retro Racer", "Status": "Working"})

else:
    arcade.pop({"Pinball Wizard": "Category": "Pinball", "Status",: "Working"})