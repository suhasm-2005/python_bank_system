import random
import pandas as pd

Acc_Holder = {"Name": [], "Age": [], "Phone": [], "Aadhar": [], "Account_num": []}


def Bank_Menu():
    print("1. Create Bank Account.")
    print("2. Search Account.")
    print("3. Update Account.")
    print("4. Show all Acount Holders.")
    print("5. Exit")


def Create_Acc():
    NAME = input("Enter the name: ")
    AGE = int(input("Enter your age: "))
    while True:
        PHONE = input("Enter yor phone number: ")
        if len(PHONE) == 10 and PHONE.isdigit():
            break
        print("Your phone number must contain only 10 digits!")
    while True:
        AADHAR = input("Enter your aadhar: ")
        if len(AADHAR) == 12 and AADHAR.isdigit():
            break
        print("Your aadhar number must contain only 12 digits!")

    if AADHAR:
        OTP_number = random.randint(1000, 9999)
        print("Your OTP number:", OTP_number)
        OTP = int(input("Enter the OTP number: "))
        if OTP_number == OTP:
            ACC = random.randint(100000, 999999)
            Acc_Holder["Name"].append(NAME)
            Acc_Holder["Age"].append(AGE)
            Acc_Holder["Phone"].append(PHONE)
            Acc_Holder["Aadhar"].append(AADHAR)
            Acc_Holder["Account_num"].append(ACC)
            print("Your Account Created Successfully!")
            print("Your Account number: ", ACC)


def Search_Acc():
    if not Acc_Holder["Account_num"]:
        print("No to accounts to search...!!!")
    else:
        df = pd.DataFrame(Acc_Holder)
        search_acc = int(input("enter the account number to search: "))
        search = df[df["Account_num"] == search_acc]
        if not search.empty:
            print(search)
        else:
            print("No such accounts..!")


def Update_Acc():
    acc = int(input("Enter the account number:"))
    if acc not in Acc_Holder["Account_num"]:
        print("No such account found..!!!")
        return
    idx = Acc_Holder["Account_num"].index(acc)
    print("1.update phone number.")
    print("\n2.update Aadhar number.")

    Choice = int(input("Enter your choice: "))
    if Choice == 1:
        while True:
            phone = input("Enter the new phone number: ")
            if len(phone) == phone and phone.isdigit():
                Acc_Holder["Account_num"][idx] = phone
                print("Phone number is updated successfully.")
                break
            else:
                print("Phone number must be 10 digits.")
    elif Choice == 2:
        while True:
            aadhar = input("Enter the new phone number: ")
            if len(aadhar) == aadhar and aadhar.isdigit():
                Acc_Holder["Aadhar"][idx] = aadhar
                print("Aadhar number is updated successfully.")
                break
            else:
                print("Aadhar number must be 10 digits.")
    else:
        print("Invalid choice..!!!")


def show_Acc():
    df1 = pd.DataFrame(Acc_Holder)
    if not df1.empty:
        print("/nAccounts Holders: ")
        print(df1)
    else:
        print("No Accounts Holders..!")


Bank_Menu()
while True:

    choice = int(input("Enter the choice: "))
    if choice == 5:
        break
    elif choice == 1:
        Create_Acc()
    elif choice == 2:
        Search_Acc()
    elif choice == 3:
        Update_Acc()
    elif choice == 4:
        show_Acc()
    else:
        print("Invalid choice..!")
