from PIL import Image
import time

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
                print("Data overflow")
                break
        return output_img
    else:
        print(f'Data overflows image capacity. Data size: {len(data_to_encrypt)} Image capacity: {img_cap}')

def decrypt(input_image):
    image_data = iter(input_image.getdata())
    decrypted_data = ''
    pixel_set = []
    
    for pixel in image_data:
        pixel_set.append(pixel)
        if len(pixel_set) == 3:
            # We are always looking for 3 pixels, because it give us 9 bits
            # Bit 1-8 are representation of a ASCII char; odd value of 9'th bit indicates the end of message
            bin_data = ''
            values = list(sum(pixel_set, ()))
            for i in values[:8]:
                # Decrypt single 8bit character
                if i % 2 == 0:
                    bin_data += '0'
                else:
                    bin_data += '1'
            decrypted_msg += chr(bin_data)
            if values[-1] % 2 == 0:
                # If 9'th bit is odd break the loop 
                break
            del pixel_set[:]
    return decrypted_data

def main():
    pass

if __name__ == '__main__' : 
    main()
