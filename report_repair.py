with open("report_repair_data.txt") as data:
    entries_as_str = data.readlines()
entries_as_int = [int(entry.strip() )for entry in entries_as_str]
numbers = [entry for entry in entries_as_int if (2020 - entry) in entries_as_int]
product = numbers[0] * numbers[1]
print(product)