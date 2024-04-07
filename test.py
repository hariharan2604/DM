from collections import defaultdict
import csv

def generate_candidates(itemset, length):
    """Generate candidate itemsets of length 'length'."""
    candidates = set()
    for item1 in itemset:
        for item2 in itemset:
            union = item1.union(item2)
            if len(union) == length:
                candidates.add(union)
    return candidates

def prune(itemset, candidates, min_support, transactions):
    """Prune candidate itemsets that do not meet the minimum support."""
    support_counts = defaultdict(int)
    pruned_candidates = set()
    for transaction in transactions:
        for candidate in candidates:
            if candidate.issubset(transaction):
                support_counts[candidate] += 1
    for candidate, count in support_counts.items():
        support = count
        if support >= min_support:
            pruned_candidates.add((candidate, support))  # Storing support value
    return pruned_candidates

def apriori(transactions, min_support):
    """Generate frequent itemsets using the Apriori algorithm."""
    itemset = set()
    for transaction in transactions:
        for item in transaction:
            itemset.add(frozenset([item]))

    frequent_itemsets = []
    k = 1
    while itemset:
        candidates = generate_candidates(itemset, k+1)
        frequent_candidates = prune(itemset, candidates, min_support, transactions)
        frequent_itemsets.extend(frequent_candidates)
        itemset = {candidate for candidate, _ in frequent_candidates}
        k += 1
    return frequent_itemsets

def convert_csv_to_transactions(csv_file):
    transactions = []
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            items = row['Items'].replace('{', '').replace('}', '').split(', ')
            transactions.append(set(items))
    return transactions

# Example usage:
csv_file = 'computer.csv'  # Replace 'transactions.csv' with the path to your CSV file
transactions = convert_csv_to_transactions(csv_file)

min_support = 2  # Setting minimum support as count instead of a fraction
frequent_itemsets = apriori(transactions, min_support)
print("Frequent Itemsets:")
for itemset, support in frequent_itemsets:
    items = ', '.join(itemset)
    print(f"{items} => support = {support}")
