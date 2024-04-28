def equal_frequency_partition(data, num_partitions):
    n = len(data)
    partition_size = n // num_partitions
    partitions = []
    start = 0
    for i in range(num_partitions):
        end = min(start + partition_size, n)
        partitions.append(data[start:end])
        start = end
    return partitions

# Example usage with your provided data
data = [5, 10, 11, 13, 15, 35, 50, 55, 72, 92, 204, 215, 300, 315, 370, 460]
num_partitions = 4 
result = equal_frequency_partition(sorted(data), num_partitions)
print("Equal-frequency partitions:")
for i, partition in enumerate(result):
    print(f"Partition {i+1}: {partition}")
