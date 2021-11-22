
import sys
user_input = input("Please pick a number to find all numbers that divide equally into chosen number:  ")


try:
    int(user_input)
    print("you did pick a number")
except ValueError:
    print("you did not pick a number")
    sys.exit()


#if abs(user_input.isnumeric()) == True:
#    print("you picked a real number")
#else:
#    print("you did not pick a number")
#    sys.exit()
user_input = int(user_input)

user_input_list = []
temp_user_input = user_input

while temp_user_input != 0:
    if temp_user_input > 0:
        user_input_list.append(temp_user_input)
        temp_user_input -= 1
    elif temp_user_input < 0:
        user_input_list.append(temp_user_input)
        temp_user_input += 1
    else:
        print("please pick a real number")
for temp in user_input_list:
    apple = user_input % abs(temp)
    if apple == 0:
        print (abs(temp))
