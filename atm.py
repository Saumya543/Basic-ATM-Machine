
import time
time.sleep(5)

password = 1234
print("Please insert your Card")

pin = int(input("enter your atm pin"))

balance = 5000 
if pin==password:
    while True:
            
        print("""
            1 == balance
            2 == withdraw balance
            3 == deposit balance
            4 == exit
            """)
        try:
            option = int(input("[please enter your choice]"))
        except:
            print("invalid input")

        if option==1:
            print(f"your balance is {balance}")

            print("============================================")
            print("============================================")

        if option==2:
            withdraw_amount = int(input("please enter withdraw_amount"))

            print("============================================")
            print("============================================")

            balance = balance - withdraw_amount
            print(f"{withdraw_amount} is debited from your account")

            print("============================================")
            print("============================================")

            print(f"your updated balance is {balance}")

            print("============================================")
            print("============================================")

        if option==3:
            deposit_amount = int(input("please enter deposit_amount"))
            balance = balance + deposit_amount
            print(f"{deposit_amount} is credited to your account")

            print("============================================")
            print("============================================")

            print(f"your updated balance is {balance}")

            print("============================================")
            print("============================================")
                
        if option==4:
            print("Thank you for using our ATM")
            break


else:
    print("wrong pin please try again")        