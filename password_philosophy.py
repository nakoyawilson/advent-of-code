with open("password_philosophy_data.txt") as data:
    passwords = data.readlines()
    password_data = []
    for password in passwords:
        password_list = password.split()
        password_list[0] = password_list[0].replace("-", " ")
        criteria = password_list[0].split()
        password_list[1] = password_list[1].replace(":", "")
        new_list = [criteria[0], criteria[1], password_list[1], password_list[2]]
        password_data.append(new_list)

# Part One Solution
valid_passwords = 0
for item in password_data:
    word = item[3]
    letter = item[2]
    first_num = int(item[0])
    second_num = int(item[1])
    if letter in word:
        if first_num <= word.count(letter) <= second_num:
            valid_passwords += 1
print(valid_passwords)

# Part Two Solution
correct_valid_passwords = 0
for item in password_data:
    word = item[3]
    letter = item[2]
    first_index = int(item[0]) - 1
    second_index = int(item[1]) - 1
    if word[first_index] == letter or word[second_index] == letter:
        if word[first_index] != word[second_index]:
            correct_valid_passwords += 1
print(correct_valid_passwords)
