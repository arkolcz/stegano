from PIL import Image

def convert_data(word):
    # Convert chars to bits
    binary_data = ''
    for char in word:
        binary_data += format(ord(char), '08b')
    return binary_data

def modify_pixel(pixel, bit ):
    print(pixel, bit)
    return None

def encode(input_img, data):
    data_to_encode = convert_data(data)
    output_img = input_img.copy() # Create an output image that will contain encoded data
    pixels = iter(output_img.getdata()) # Get all pixels from output_image as tuples
    print(output_img)
    
    #for i in range(len(data_to_encode)):
    # pixels[i] = modify_pixel(i, data_to_encode[i])

def decode():
    pass

def main():
    img = Image.open('./img/some_img.jpg') # TODO: Draft, remove
    sentence = "Hello there, friend."   # TODO: Draft, remove
    encode(img, sentence)

if __name__ == '__main__' : 
    main()