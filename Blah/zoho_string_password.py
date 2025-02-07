"""Password length should be 6-11 characters, can't have continuous Uppercase letters, can't start with numbers eg:Zoho@123 """

Input=input("Enter the Password: ")

print(Input)

is_digit= '0'<= Input[0] <= '9'


while True:
    if not is_digit and 6<=len(Input)<=11:
        print("valid")
    else:
        print("Invalid")
    break




