# shopping_cart.py
import datetime


def function1():


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

    # TODO: write some Python code here to produce the desired functionality...

    #selected_id=input("Please input a product identifier: ") #> "9" is string version
    #print(selected_id)
    #print(type(selected_id))

    #selected_id = input("Please input a product identifier: ")
    #matching_product = [p for p in products if p["id"] == selected_id]
    #print(matching_product)
    #print(type(matching_product))

    #todo multiple times--use while loop--must indent along with loop--NEED DONE AS WELL


    #CONDITIONALLY DETECT DONE
    total_price = 0 

    tax_rate = .06

    selected_ids = []

    while True:
        selected_id = input("Please input a product identifier: ")

        if selected_id == "DONE":
                break
        else:
            #matching_products = [p for p in products if str(p["id"]) == str(selected_id)]
            #matching_product = matching_products[0] #why is this zero--would it affect if you were to take out id#4?
            #total_price = total_price + matching_product["price"]
            #print("Selected product: " + matching_product["name"] + " " + str(matching_product["price"]))
            #^ABOVE WAS LOOKUP APPROACH
            selected_ids.append(selected_id)

    #INFO DISPLAY
def human_friendly_timestamp():
    t = datetime.datetime.now()
    print(t.strftime("%y-%m-%d"))
    return t.strftime("%y-%m-%d")


    print("---------------------------------------------")
    print("Welcome to the Jyve Grocery Store")
    print("www.jyve.grocerystore.com")
    print("---------------------------------------------")
    print("Checkout at :" + str(t)) #STILL NEED TO FORMAT****************
    print("---------------------------------------------")
    print(selected_ids)#******GET LIST OF PRODUCTS BELOW TO HAVE "SELECTED PRODUCTS" AND THEN ...+...+

    for selected_id in selected_ids:
# def find_product(selected_id):
        matching_products = [p for p in products if str(p["id"]) == str(selected_id)]
        matching_product = matching_products[0] #why is this zero--would it affect if you were to take out id#4?
        total_price = total_price + matching_product["price"]
        print("Selected product: " + matching_product["name"] + " " + str(matching_product["price"]))
    # return matching_product["name"] 

    print("---------------------------------------------")
    tax_price = total_price * tax_rate
    final_price = total_price + tax_price
    # print("SUBTOTAL: $" + str(total_price))
    # print("TAX: $" + str(tax_price)) #calculate taX--HOW TO PUT IN THE 6% AS A MEASURE OF TOTAL. THEN ADD THE TAX TO SUBTOTAL
    # print("TOTAL: $" + str(final_price))

def to_usd(total_price):
    print('TOTAL PRICE: $',round(total_price,2))
    print('TAX: $', round(.06*total_price,2))
    print('TOTAL: $', round(1.06*total_price,2))
    return round(1.06*total_price,2)

    print("---------------------------------------------")
    "Thanks for shopping at the Jyve Grocery Store!"
    print("---------------------------------------------")


    #LIST OF THINGS TO DO






    #APPEND TO ADD ITEMS TO LIST







    #
    #
    #
    #
    #
    #
    #



    # TODO: write some Python code here to produce the desired functionality...
    #print(products)

    #"DONE" 

    #GROCERY STORE NAME
    input()

    #GROCERY STORE PHONE NUMBER

    #DATE AND TIME OF BEGINNING CHECKOUT PROCESS
    import datetime
    t = datetime.datetime.now()
    print(type(t))
    print(t)
    #strftime("%Y-%m-%d") HOW TO CONVERT TO REGULAR TIME


    #NAME AND PRICE EACH ITEM

    #TOTAL COST OF SHOPPING CART ITEMS

    #AMOUNT OF TAX OWED

    #TOTAL AMOUNT OWED

    #FRIENDLY MESSAGE SAYING THANK YOU. take into account order
    print ("Thank you for shopping! Please come again.")




