import os
import dotenv
import time
from datetime import date
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

dotenv.load_dotenv()

# Store and receipt information.
store_name = "TRADER SHANE'S"
website = f"www.tradershanes.com"
today = date.today()
current_time = time.localtime()
t = time.strftime("%H:%M:%S", current_time)

# This is calling the .env file to get the tax rate and converting it into a float so it can be multiplied with the subtotal.
tax_rate = float(os.getenv("TAX_RATE"))


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
# Code adapted from Professor Rossetti's video walkthrough.
while True:
        item = (input("ENTER ITEM ID:")).strip()
        # First, checking to see if the cashier is done inputting to break the loop
        if item.upper() == "DONE":
            break       
        # Appends the products and prices into their respective lists.
        else:
            try:
                matching_id = [p for p in products if str(p["id"]) == str(item)]
                product = matching_id[0]["name"]
                grocery_list.append(product)
                item_price = to_usd(matching_id[0]["price"])
                price_list.append(matching_id[0]["price"])
                print(f"... {product} ({item_price})")
            except IndexError or ValueError:
                print("INVALID ENTRY. TRY AGAIN.")            

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
print("SUBTOTAL: ", to_usd(subtotal))
tax = (subtotal * tax_rate)
print("TAX: ", to_usd(tax))
total = to_usd((tax + subtotal))
print("TOTAL: ", total)
print("----------------------------")
print("THANK YOU! SEE YOU AGAIN SOON!")
print("----------------------------")

email_request = (input("Would you like to receive an e-mail receipt? [y/n]")).strip()
if email_request.lower() == "y":
    customer = input("Please enter your e-mail address:")
    # Sendgrid API request
    # Adapted from Professor Rossetti's guide on GitHub.
    SENDGRID_API_KEY = os.getenv("SENDGRID_API", default="OOPS, please set env var called 'SENDGRID_API_KEY'")
    SENDER_ADDRESS = os.getenv("SENDGRID_EMAIL", default="OOPS, please set env var called 'SENDER_ADDRESS'")

    client = SendGridAPIClient(SENDGRID_API_KEY)

    subject = (f"Your receipt from {store_name}.")

    body = (f"On {today} at {t}, your purchase from {store_name} came to a total of {total}.")

    message = Mail(from_email=SENDER_ADDRESS, to_emails=customer, subject=subject, html_content=body)
    
    # Adapted from Professor Rossetti's guide on GitHub.    
    try:
        response = client.send(message)
        # print("RESPONSE:", type(response))
        if (response.status_code) == 202:
            print("E-MAIL SENT. THANK YOU FOR SHOPPING AT TRADER SHANE'S!") 
        # print(response.body)
        # print(response.headers)
    except Exception as err:
        print(type(err))
        print(err)

    print("HAVE A NICE DAY!")

# print(SENDER_ADDRESS)
# print(SENDGRID_API_KEY)
