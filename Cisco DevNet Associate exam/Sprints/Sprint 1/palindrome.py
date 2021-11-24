user_input = input("Please enter a word to find out if its a palindrome or not: ")
reverse_input = user_input[::-1]
if user_input ==  reverse_input:
    print ("this is a palindrome")
else:
    print("This is not palindrome")