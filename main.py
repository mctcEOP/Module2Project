# North Loop Provisions - Donut Shop Management System
# Your first Python program for Module 2

def welcome_message():
    # Display a welcome message
    print("Welcome To North Loop Provisions!\nCrafting artisanal donuts in Minneapolis' North Loop")

def show_menu():
    # Display Donut menu
    menu = {
        "Classic Glazed": 3.50,
        "Maple Bacon": 2.10,
        "Jam filled Vanilla": 3.20,
        "Strawvberry Frosting": 2.00,
        "Sugar donut": 1.50

    }

    print("\nToday's Donut's Menu")
    print("--------------------------")
    for donut, price in menu.items():
        print(f"{donut}: ${price:.2f}")
    
# Main program
if __name__ == "__main__":
    welcome_message()
    show_menu()
    print("\nReady to serve our community with the finest donuts!")

    # our complete menu list ordered by category
    donut_menu = {
        'Small Batch': [
            'Wild Rice & Honey',
            'Maple Bacon',
            'Swedish Cardamom'
            ],
        'Seasonal': [
            'Apple Cider',
            'Jucy Lucy',
            'Lake of the Woods'
        ],
        'Local Collabs': [
            'Spyhouse Coffee Cake',
            'Fulton Beer & Pretzel',
            'Sweet Science Ice Cream'
        ]
    }

    # Locally-sourced toppings
    toppings = [
        'House-Made Sprinkles',
        'Candied Hazelnuts',
        'Bee Pollen',
        'Cookie Butter Drizzle'
    ]

    # Track Morning sales with a dictionary
    morning_sales = []

    # record our first sales (by appending a transaction to the sales dictionary)
    morning_sales.append({
        'item': 'Wild rice & Honey',
        'quantity': 2,
        'toppings':['Bee pollen'],
        'time': '7:30 AM'
    })

    #Display our current menu - using a for loops

    print("Today's Morning Mneu:")
    for category, items in donut_menu.items():
        print(category + ":")
        for item in items:
            print(" - " + item)
