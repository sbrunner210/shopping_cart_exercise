import os
import dotenv
import time
from datetime import date

dotenv.load_dotenv()

# Store and receipt information.
store_name = "PLACEHOLDER HERE"
website = f"www.{store_name}.com"
today = date.today()
current_time = time.localtime()
t = time.strftime("%H:%M:%S", current_time)
tax_rate = 0.08

# Empty lists for storing groceries and prices from inputs.
grocery_list = []
price_list = []

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

# Adapted from Professor Rosetti's exercise prompt.
def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.

    Param: my_price (int or float) like 4000.444444

    Example: to_usd(4000.444444)

    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71

# Input process for groceries.
while True:
        item = (input("ENTER ITEM ID:")).strip()
        # First, checking to see if the cashier is done inputting to break the loop
        if item.upper() == "DONE":
            break
        # Sorts the product IDs into a list to check for an error in the input
        elif int(item) not in [p["id"] for p in products]:   
            print("INVALID ENTRY. TRY AGAIN.")            
        # Appends the products and prices into their respective lists.
        else:
            matching_id = [p for p in products if str(p["id"]) == str(item)]
            product = matching_id[0]["name"]
            grocery_list.append(product)
            item_price = to_usd(matching_id[0]["price"])
            price_list.append(matching_id[0]["price"])
            print(f"... {product} ({item_price})")




print("----------------------------")
print(f"WELCOME TO {store_name}!")
print(website)
print("----------------------------")
print(f"CHECKOUT AT: {today} {t}")
print("----------------------------")
print("SELECTED PRODUCTS:")

# Loops through the grocery list and prints the items line by line.
for grocery in grocery_list:
    index = grocery_list.index(grocery)
    register_price = to_usd(price_list[index])
    print(f"... {grocery} {register_price}")

print("----------------------------")
subtotal = (sum(price_list))
print("SUBTOTAL: ", subtotal, to_usd(subtotal))
tax = (subtotal * tax_rate)
print("TAX: ", tax, to_usd(tax))
total = (tax + subtotal)
print("TOTAL: ", total, to_usd(total))
print("----------------------------")
print("THANK YOU! SEE YOU AGAIN SOON!")