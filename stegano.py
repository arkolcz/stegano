import encrypt as e
import decrypt as d

def main():
    heading = "#################### Encryption Tool ###################"
    menu_opts = ["Encrypt file", "Decrypt File", "Quit"]

    while True:
        print(heading)
        for i, option in enumerate(menu_opts):
            print(f"{i + 1}. {option}")

        try:
            user_input = int(input(f"{'-' * len(heading)}\nExecute: "))

            if user_input not in range(1, 4):
                raise ValueError
            else:
                break

        except ValueError:
            print("\nError: Invalid menu option\n")

    if user_input == 1:
        e.encryption_menu()
    elif user_input == 2:
        d.decryption_menu()
    elif user_input == 3:
        print('Exiting.')
           
            
if __name__ == '__main__' : 
    main()
