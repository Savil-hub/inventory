
#========The beginning of the class==========
#define class shoe with the following attributes: country, code, product, cost, quantity
class Shoe:
    def __init__(self, country, code, product, cost, quantity):
        # Define the Shoe class variables
        self.country = country
        self.code = code
        self.product = product
        self.cost = float(cost)
        self.quantity = int(quantity)

    def get_cost(self):
        return self.cost

    def get_quantity(self):
        return self.quantity

    def __str__(self):
        return f'''
        Country: {self.country}
        Code: {self.code} 
        Product: {self.product} 
        Cost: ${round(self.cost, 2)}
        Quantity: {self.quantity}
        '''



#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []
#==========Functions outside the class==============

# Function to read shoe data from inventory.txt
# Function to read shoe data from inventory.txt
def read_shoes_data():
    with open("inventory.txt", "r") as file:
        # Creating Shoe objects with the data and appending them to the shoe_list
        for line in file:
            temp = line.strip().split(",")
            if 'Country' not in temp:
                shoe_list.append(Shoe(temp[0], temp[1], temp[2], temp[3], temp[4]))

# Read shoe data from the file once before entering the main loop
read_shoes_data()

# Function to write shoe data to the inventory file
def write_shoes_data():
    with open("inventory.txt", "w") as file:
        file.write("Country,Code,Product,Cost,Quantity\n")
        for shoe in shoe_list:
            file.write(f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}\n")

# Function to capture shoe data from the user and update the list
def capture_shoes():
    country = input("Enter the country: ")
    code = input("Enter the code: ")
    product = input("Enter the product: ")
    cost = float(input("Enter the cost: "))
    quantity = int(input("Enter the quantity: "))
    shoe_list.append(Shoe(country, code, product, cost, quantity))
    print("Shoe data captured successfully!")


# Function to view all shoe details
def view_all():
    for shoe in shoe_list:
        print(shoe)


''''Function to find the shoe with the lowest quantity,
which are the shoes that need to be re-stocked. Ask the user if they want add to this quantity and
then update it. this quantity should be upadted on the file for this shoe.'''
def re_stock():
    #using a function to find the shoe object with the lowest quantity. inf is a palce holder to make sure no number in shoe quantity is greater than my place holder number 
    lowest_quantity = float("inf")
    restock_shoe = None


    #loop through every quantity in shoes list until it finds the lowest quantiy in the shoe list and repalce the inf with this new lower number until it finds the lowest number
    for shoe in shoe_list:
        if shoe.get_quantity() < lowest_quantity:
            lowest_quantity = shoe.get_quantity()
            restock_shoe = shoe


    #asking the user if they want to add this quantity of shoes and then update it.
    if restock_shoe:
        print(f"The shoe to restock is:\n{restock_shoe}")
        try:
            new_quantity = int(input("Enter the new quantity: "))
            if new_quantity >= 0:
                restock_shoe.quantity = new_quantity
                print("Restock completed successfully!")
                # Write the updated data to the file after restocking
                write_shoes_data()
            else:
                print("Invalid quantity entered. Quantity must be non-negative")
        except ValueError:
            print("Invalid input. Please enter a valid quantiy")
    else:
        print("No shoes found to restock.")


# Function to search for a shoe by its code and print its details
def search_shoe():
    search_code = input("Enter the shoe code to search: ")
    found = False
    for shoe in shoe_list:
        if shoe.code == search_code:
            print(f"Shoe with code {search_code} found:\n{shoe}")
            found = True
            break
    if not found:
        print(f"No shoe found with code {search_code}")


# Function to calculate and display the total value for each item
def value_per_item():
    for shoe in shoe_list:
        value = shoe.get_cost() * shoe.get_quantity()
        print(f"The total value for {shoe.product} is: {value}")


# Function to determine and display the product with the highest quantity and then print this being for sale
def highest_qty():
    highest_quantity = -1
    high_quantity_product = None
    for shoe in shoe_list:
        if shoe.get_quantity() > highest_quantity:
            highest_quantity = shoe.get_quantity()
            high_quantity_product = shoe.product
    if high_quantity_product:
        print(f"The product with the highest quantity is: {high_quantity_product}")
    else:
        print("No products found in the inventory.")

#==========Main Menu=============
# Function to # Menu loop
while True:
    print("\nMenu:")
    print("1. Capture Shoe Data")
    print("2. View All Shoes")
    print("3. Restock Shoes")
    print("4. Search for a shoe by its code")
    print("5. Value per Item")
    print("6. Highest Quantity Product")
    print("7. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        capture_shoes()
    elif choice == "2":
        view_all()
    elif choice == "3":
        re_stock()
    elif choice == "4":
        search_shoe()
    elif choice == "5":
        value_per_item()
    elif choice == "6":
        highest_qty()
    elif choice == "7":
        break
    else:
        print("Invalid choice. Please try again")