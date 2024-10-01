def check_number(left_num):
    if (left_num.isdigit() == True) and (int(left_num) >=3) and (int(left_num) <=20):
        return True
    else:
        return False

left_num = input("Введите число от 3 до 20:")
while (check_number(left_num) == False):
    left_num = input("Да нет же, ЧИСЛО от 3 до 20:")

numbers = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
for i in numbers:
    print (i)