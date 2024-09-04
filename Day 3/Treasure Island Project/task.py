print('''
*******************************************************************************
          _,_           __   __                _,_           __   __
       ._(@I@)_.       /  \-/  \            ._(@I@)_.       /  \-/  \/
      .--{___}--.    ._\   |   /_.         .--{___}--.    ._\   |   /_.
      .-/  Y  \-.    .__\__Y__/__.         .-/  Y  \-.    .__\__Y__/__.
       /   |   \        _{___}_             /   |   \        _{___}_
       \__/-\__/       ' (@I@) '            \__/-\__/       ' (@I@) '
                          ~^~                                  ~^~
*******************************************************************************
''')
print("Welcome Local House Fly!")
print("Your mission is to find the high-value food.")

first_move = input("Would you like to fly left or right?\n").lower()
if first_move == "left":
    exit_door = input("You see a door to the outside, Where would you like to go?"
                      "   Type 'leave' or 'stay'\n").lower()
    if exit_door == "stay":
        dog_flee = input("A dog sees you! What do you do!? "
                         "   Type 'flee' or 'stay' \n").lower()
        if dog_flee == "flee":
            hallway = input("You are in a hallway facing a blue, red and yellow door"
                            "   Type 'blue' 'red' or 'yellow\n").lower()
            if hallway == "yellow":
                print("You have found the melon room! You win 500 points")
            elif hallway == 'blue':
                print("You run into an angry human who grabs their fly swatter and kills you. GAME OVER")
            else:
                print("You end up in the bathroom, someone had just showered so your wings get wet and you drown in the tub. GAME OVER")
        else:
            print("You have accepted your fate and was eaten by the dog. GAME OVER")

    else:
        print("There was a BBQ outside and you found leftover ribs to slurp on! You win 100 points")
else:
    kitchen = input("You are in the kitchen and see a plate on the counter, what do you do?"
                    "   Type 'eat' or 'wait'\n").lower()
    if kitchen == "eat":
        print("You go for the plate and it was FLY BAIT. GAME OVER")
    else:
        print("After some time of waiting, someone leaves their dish with stinky parmesan sandwich on it! You win 10 points")

