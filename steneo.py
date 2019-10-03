from PIL import Image

def convert_data(data):
    binary_data = ''
    # Convert each character in data to binary format and add one additional bit '1' after ea ch binary sequence 
    for char in data:
        binary_data += format(ord(char), '08b') + '1'
    # Change last bit of the string from '1' to '0' to indicate the end of the message
    binary_data = list(binary_data)
    binary_data[len(binary_data) - 1] = '0'
    binary_data = (str("".join(binary_data)))
    return binary_data
    
def modify_pixel(pixel, bit):
    pass

def encrypt(input_img, data):
    data_to_encrypt = convert_data(data)
    output_img = input_img.copy()
    img_w, img_h = output_img.size

    # Maximum bits number that can be stored in image
    img_cap = (img_w * img_h) * 3 

    if img_cap < len(data_to_encrypt):
        print(f'Data overflows image capacity. Data size: {len(data_to_encrypt)} Image capacity: {img_cap}')
    else:
        for i in range(len(data_to_encrypt)):
            print(data_to_encrypt[i])
    #output_img.show()
    #for x in range(img_h):
    #    for i in range(img_w):
    #        output_img.putpixel((x, i), (255,255,255))
    #output_img.show()

    #print(output_img.getpixel((1,1)))
    #print(output_img.putpixel((1,1), (1,0,0)))
    #print(output_img.getpixel((1,1)))
    
def decrypt():
    pass

def main():
    img = Image.open('./img/av.jpg') # TODO: Draft, remove
    sentence = "Hello there, friend."   # TODO: Draft, remove
    encrypt(img, sentence)

if __name__ == '__main__' : 
    main()