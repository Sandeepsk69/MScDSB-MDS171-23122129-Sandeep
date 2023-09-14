
# Sandeep Kumar G 23122129 
# Creating the lists for items, quantity, price.
Items = ["apple", "banana", "orange", "grapes", "mango", "kiwi", "watermelon", "pineapple", "strawberry", "blueberry"]
Quantity = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Price = [45,45,68,89,26,89,19,99,69,49]

# Create 100 rows in the CSV file
import random
rows = []
for i in range(0,100):
    index = random.randint(0, 9)            # Generate random index to access items from the list
    row = [Items[index], Quantity[index], Price[index]]
    rows.append(row)

# Write the data to the CSV file
with open('shopping.csv', 'w') as f:
    f.write("Item,Quantity,Unit Price\n")
    for row in rows:
        f.write(f"{row[0]},{row[1]},{row[2]}\n")

# Calculate total cost for each row
with open('shopping.csv', 'r') as f:
    lines = f.readlines()[1:]
    for line in lines:
        row = line.strip().split(',')
        total_cost = float(row[1]) * float(row[2])
        print(f"{row[0]}: Total Cost = {total_cost}")

# Display the results of the first 5 and last 10 rows
with open('shopping.csv', 'r') as f:
    lines = f.readlines()[1:]
    for i in range(len(lines)):
        row = lines[i].strip().split(',')
        total_cost = float(row[1]) * float(row[2])
        if i < 5 or i >= 90:
            print(f"{row[0]}: Quantity = {row[1]}, Unit Price = {row[2]}, Total Cost = {total_cost}")

# Calculate total cost for each unique item in the dataset
item_totals = {}
with open('shopping.csv', 'r') as f:
    lines = f.readlines()[1:]
    for line in lines:
        row = line.strip().split(',')
        total_cost = float(row[1]) * float(row[2])
        if row[0] not in item_totals:
            item_totals[row[0]] = [0, 0]
        item_totals[row[0]][0] += float(row[1])
        item_totals[row[0]][1] += total_cost
    print("\nItem Name | Total Quantity | Total")
    for item in item_totals:
        print(f"{item} | {item_totals[item][0]} | {item_totals[item][1]}")

# Print the minimum & maximum price for each item sold
item_prices = {}
with open('shopping.csv', 'r') as f:
    lines = f.readlines()[1:]
    for line in lines:
        row = line.strip().split(',')
        if row[0] not in item_prices:
            item_prices[row[0]] = []
        item_prices[row[0]].append(float(row[2]))
    print("\nItem | Minimum Price | Maximum Price")
    for item in item_prices:
        print(f"{item} | {min(item_prices[item])} | {max(item_prices[item])}")