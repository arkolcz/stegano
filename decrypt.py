from PIL import Image

def decryption_menu():
    img_path = input('Image location: ')
    img = Image.open(img_path)
    decrypted_text = decrypt(img)
    print("Decrypted message: " + decrypted_text)

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
            decrypted_data += bin_data
            if values[-1] % 2 == 0:
                # If 9'th bit is odd break the loop 
                break
            # Clear pixel set after each loop iteration
            del pixel_set[:]
    return decrypted_data
