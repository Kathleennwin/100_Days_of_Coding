fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    # Since these print statements are nested in the for-loop, it will print as many times until the list has
    # gone through all items so each will print 3 times for 3 items in the list
    print(fruit)
    print(fruit + " pie")
    # if the line below is moved away from the indentation, then it will print once and will print at the end
    # after the loop
    print(fruits)
