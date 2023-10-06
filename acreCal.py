#One acre of land is equivalent to 43,560 square feet. Write a Python function that asks the user
#to enter a number of acres. The function should calculate the equivalent number of square feet
#and the price assuming land costs $35/square feet.


#arce = 43560
#price = 35

def arce_to_sqft(acres):
    sqft = acres * 43560
    price = sqft * 35
    print("Buying " + str(acres) + " acres is " + str(sqft) + " square feet")
    print("The price will cost $" + str(price))

numOfArce = int(input("Enter in a number of acres? "))
arce_to_sqft(numOfArce)

