from PIL import Image

def convert_data_to_bin(data):
    binary_data = ''
    # Convert each character in data to binary format and add one additional bit '1' after ea ch binary sequence 
    for char in data:
        binary_data += format(ord(char), '08b') + '1'

    # Change last bit of the string from '1' to '0' to indicate the end of the message
    binary_data = list(binary_data)
    binary_data[len(binary_data) - 1] = '0'
    binary_data = (str("".join(binary_data)))
    return binary_data

def bin_data_to_px(data_string):
    n = 3
    pixel_list = [str((data_string[i:i+n])) for i in range(0, len(data_string), n)] 
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
    data_to_encrypt = bin_data_to_px(convert_data_to_bin(data))
    output_img = input_img.copy()
    img_w, img_h = output_img.size
    x, y = 0, 0
    # Maximum number of bits that can be stored in image
    img_cap = (img_w * img_h) * 3

    if img_cap < len(data_to_encrypt):
        print(f'Data overflows image capacity. Data size: {len(data_to_encrypt)} Image capacity: {img_cap}')
    else:
        for data_set in data_to_encrypt:
            if x <= img_w:
                pixel = output_img.getpixel((x, y))
                modified_pixel = modify_pixel(pixel, data_set)
                output_img.putpixel((x, y), modified_pixel)
                x += 1
            elif y <= img_h: 
                y += 1
                x = 0 
            else:
                print("Data overflow")
                break
        return output_img

def decrypt():
    pass

def main():
    img = Image.open('./img/av.jpg') # TODO: Draft, remove
    sentence = "Hello there, friend."   # TODO: Draft, remove
    encrypted_image = encrypt(img, sentence) # TODO: Draft, remove
    encrypted_image.save('encrypted.jpg') # TODO: Draft, remove
    
if __name__ == '__main__' : 
    main()