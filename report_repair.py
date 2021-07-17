with open("report_repair_data.txt") as data:
    entries_as_str = data.readlines()
entries_as_int = [int(entry.strip()) for entry in entries_as_str]

# Part One Solution
two_entries = [entry for entry in entries_as_int if (2020 - entry) in entries_as_int]
two_entries_product = two_entries[0] * two_entries[1]
print(two_entries_product)

# Part Two Solution
three_entries = []
for num1 in entries_as_int:
    for num2 in entries_as_int:
        if (2020 - (num1+num2)) in entries_as_int:
            if num1 not in three_entries:
                three_entries.append(num1)
three_entries_product = three_entries[0] * three_entries[1] * three_entries[2]
print(three_entries_product)