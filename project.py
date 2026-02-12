# You will be creating a little store in your terminal. You will have a list of
# dictionaries that will be displayed to the user. Each Dictionary will have at
# least 3 properties (name, price and whatever you want)
# PART ONE:
# The user will select one item to purchase. You will then show the user
# ONLY the name of the item they purchased. You will need to use the item
# index to accomplish this task.

# PART TWO:
# You will now make the app more complex by incorporating while loops and
# a “cart”. Users will be shown the list of items and asked to purchase one.
# Afterwards ask the user if they wish to continue. Once the user has decided
# they are done shopping, print the names of the items purchased and the
# total of the cart.



Jiaxi_items = [
{
    "Name": "Samsung 55 in tv",
    "Price": 67.98,
    "Description": "useful tv~!"

},
{
    "Name": "Dog",
    "Price": 67.98,
    "Description": "Cute animal~!"

},
{
    "Name": "Justin",
    "Price": 0.1,
    "Description": "useful person~!"

},

{
    "Name": "bball",
    "Price": 10000,
    "Description": "useful ball~!"

}
]

print("Welcome to Jiaxi's Store! Select an item to purchase!:")

for index, item in enumerate(Jiaxi_items, start=0):
    print(index, ":", item["Name"])
purchase = input("What would you like to buy? : ")

print("Thank you for your purchase! Here is your receipt: ", purchase)
# print(Jiaxi_items[0]["Name"])

# for index, item in enumerate(Jiaxi_items):
#     print(index, ":", item("Name"))