"""You had saved the items and their price details in a text file, which you purchased yesterday from a nearby super market.

You need to know:

1. How many items did you purchase?


2. How many items are free?


3. What is the total amount you had to pay?


4. What is the discount amount?


5. What is the final amount did you pay after the discount?



Help yourself by writing a python code to do this. Include necessary code to handle the possible exceptions.

Note:

Data is stored in a text file Purchase-1.txt.

Each line contains one item's details.

Item name and price is separated by a space.

You have to enter the file name during run time.

Sample Input 1:

Purchase-1.txt

Chocolate 50

Biscuit 35

Icecream 50

(blank line)

Sample output 1:

Enter the file name: Purchase-1

No of items purchased: 3

No of free items: 0

Amount to pay: 135

Discount given: 5

Final amount paid: 130

Sample input 2:

Purchase-1.txt

Chocolate 50

Biscuit 35

Icecream 50

Rice 100

Chicken 250

(blank line)

Perfume Free

Soup Free

(blank line)

Discount 80"""

def process_purchase_file():
    try:
        file_name = input("Enter the file name: ").strip()
        if not file_name.endswith('.txt'):
            file_name += '.txt'

        with open(file_name, 'r') as file:
            lines = file.readlines()

        num_items = 0
        num_free_items = 0
        total_amount = 0
        discount_amount = 0

        for line in lines:
            line = line.strip()
            if line == "":
                continue  

            parts = line.split()

            
            if len(parts) < 2:
                continue

            item = " ".join(parts[:-1])
            price = parts[-1]

            if price.lower() == "free":
                num_free_items += 1
            elif item.lower() == "discount":
                try:
                    discount_amount += int(price)
                except ValueError:
                    print(f"Ignoring invalid discount value: {price}")
            else:
                try:
                    total_amount += int(price)
                    num_items += 1
                except ValueError:
                    print(f"Ignoring invalid price for item '{item}': {price}")

        final_amount = total_amount - discount_amount

        print(f"\nNo of items purchased: {num_items}")
        print(f"No of free items: {num_free_items}")
        print(f"Amount to pay: {total_amount}")
        print(f"Discount given: {discount_amount}")
        print(f"Final amount paid: {final_amount}")

    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

process_purchase_file()
