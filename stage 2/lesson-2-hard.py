def check_number(left_num):
    if (left_num.isdigit() == True) and (int(left_num) >=3) and (int(left_num) <=20):
        return True
    else:
        return False

left_num = input("Введите число от 3 до 20:")
while (check_number(left_num) == False):
    left_num = input("Да нет же, ЧИСЛО от 3 до 20:")

password_num = []
password_str = ""
used_num = []
numbers = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)

for i in numbers:
    for j in numbers:
        used_left_num = str(i) + "|" + str(j)
        used_right_num = str(j) + "|" + str(i)
        if int(left_num) % (i+j) == 0 and i != j and used_left_num not in used_num and used_right_num not in used_num:
            password_num.append(f'{i}+{j}')
            password_str = f"{password_str}{i}{j}"
            used_num.append(used_left_num)
            used_num.append(used_right_num)

print(password_str)
print(password_num)
print(used_num)
