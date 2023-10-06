#Write a function that uses a for loop to create a list of 5 grocery items. Ask the user to type in a grocery item and indicate whether that item is in the list.
groceryList = []

#loop def
def loop():
    for i in range (5):
        item = input("Enter a grocery item: ")
        groceryList.append(item)

loop()
searchItem = input("Enter an item to search for: ")
if searchItem in groceryList:
    print(searchItem + " is in the list!")
else:
    print(searchItem + " is not in the list!")
    