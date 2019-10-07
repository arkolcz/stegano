from PIL import Image
import os

def convert_data(data):
    binary_data = ''
    # Convert each character in data to binary format and add one additional bit '1' after ea ch binary sequence 
    for char in data:
        binary_data += format(ord(char), '08b') + '1'
    # Change last bit of the string from '1' to '0' to indicate the end of the message
    binary_data = list(binary_data)
    binary_data[len(binary_data) - 1] = '0'
    binary_data = (str("".join(binary_data)))
    # Group up bits in group of 3 to represent pixel (R, G, B)
    n = 3
    pixel_list = [str((binary_data[i:i+n])) for i in range(0, len(binary_data), n)] 
    return pixel_list

def modify_pixel(pixel, data):
    pixel = list(pixel)
    # For '0' change pixel value to odd, for '1' to even
    for i in range(3):
        if (data[i] == '0') and (pixel[i] % 2 != 0):
            pixel[i] -= 1 
        elif (data[i] == '1') and (pixel[i] % 2 == 0):
            pixel[i] += 1 
    return tuple(pixel)

def encrypt(input_img, data):
    # Convert data to binary format and group it as representation of pixels
    data_to_encrypt = convert_data(data) 
    # Use copy of image to retain original image intact
    output_img = input_img.copy()  
    # img_w, img_h - Width and height of original image in pixels, x, y - coordinates of single pixel
    img_w, img_h = output_img.size 
    x, y = 0, 0
    # Maximum number of bits that can be encrypted in image
    img_cap = (img_w * img_h) * 3

    if img_cap > len(data_to_encrypt):
        for data_set in data_to_encrypt:
            if x <= img_w:
                # Swap pixel at given x,y coordinates with modified pixel
                pixel = output_img.getpixel((x, y))
                modified_pixel = modify_pixel(pixel, data_set)
                output_img.putpixel((x, y), modified_pixel)
                x += 1
            elif y <= img_h:
                # If we reach end of the current row, start encrypting from the beginning of the next row 
                y += 1
                x = 0 
            else:
                raise Exception('Data overflow')
                break
        return output_img
    else:
        raise Exception(f'Data overflows image capacity. Data size: {len(data_to_encrypt)} Image capacity: {img_cap}')

def decrypt(input_img):
    pass

def encryption_menu():
    img_path = input('Image location: ')
    data = input('Text to encrypt: ')
    img = Image.open(img_path)
    encrypted_img = encrypt(img, data)
    # Encrypted file must be saved in loseless format like PNG 
    encrypted_img.save('encrypted_' + img_path + '.png', 'PNG')

def decryption_menu():
    img_path = input('Image location: ')
    img = Image.open(img_path)
    decrypted_text = decrypt(img)
    print("Decrypted message: " + decrypted_text)

def main():
    while True:
        print("#################### Encryption Tool ###################\n"
            "1) Encrypt file\n"
            "2) Decrypt file\n"
            "3) Quit")
        user_input = int(input("Execute: "))
        if user_input == 1:
            encryption_menu()
            break
        elif user_input == 2:
            decryption_menu()
            break
        elif user_input == 3:
            break
        else:
            print('Incorrect input')
    
if __name__ == '__main__' : 
    main()
    