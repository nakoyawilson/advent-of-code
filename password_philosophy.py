# Part One Solution
with open("password_philosophy_data.txt") as data:
    passwords = data.readlines()
    password_data = []
    for password in passwords:
        list = password.split()
        list[0] = list[0].replace("-", " ")
        criteria = list[0].split()
        list[1] = list[1].replace(":", "")
        new_list = []
        new_list.append(criteria[0])
        new_list.append(criteria[1])
        new_list.append(list[1])
        new_list.append(list[2])
        password_data.append(new_list)

valid_passwords = 0
for item in password_data:
    if item[2] in item[3]:
        if item[3].count(item[2]) >= int(item[0]) and item[3].count(item[2]) <= int(item[1]):
            valid_passwords += 1
print(valid_passwords)
