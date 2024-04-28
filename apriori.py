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
            items = row['Items'].split(';')
            transactions.append(set(items))
    return transactions
csv_file = "test.csv"
transactions = convert_csv_to_transactions(csv_file)
min_support = 2
frequent_itemsets = apriori(transactions, min_support)
print("Frequent Itemsets:\n")
for itemset, support in frequent_itemsets:
        items = ', '.join(itemset)
        print(f"{items} => support = {support}")

