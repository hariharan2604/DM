import csv
import random

# Function to generate random transaction data
def generate_transaction():
    items =  ['computer', 'mouse', 'keyboard', 'monitor']
    num_items = random.randint(1, 4)  # Random number of items per transaction (1 to 5)
    return random.sample(items, num_items)

# Generate transaction data
transactions = []
for _ in range(100):
    transactions.append(generate_transaction())

# Write transaction data to CSV file
with open('computer.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Transaction ID', 'Items'])
    for i, transaction in enumerate(transactions, start=1):
        writer.writerow([i, "{" + ", ".join(transaction) + "}"])
