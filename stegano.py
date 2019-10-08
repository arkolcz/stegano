import encrypt as e
import decrypt as d

def main():
    while True:
        print("#################### Encryption Tool ###################\n"
            "1) Encrypt file\n"
            "2) Decrypt file\n"
            "3) Quit")
        user_input = int(input("Execute: "))
        if user_input == 1:
            e.encryption_menu()
            break
        elif user_input == 2:
            d.decryption_menu()
            break
        elif user_input == 3:
            break
        else:
            print('Incorrect input')
            
if __name__ == '__main__' : 
    main()
