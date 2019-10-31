# Steganography: Encrypt text in image

## Background

Steganography is a technique of hiding message, file within another file. 

This tool allows to encrypt a message inside an image. The idea behind it is that every image is a matrix of pixels.</br>
Each pixel is represented by 3 values: **Red Green Blue (RGB)** which can take the value range **0-255**.</br>
Each ASCII character can be presented in binary form. For example: X -> 88 -> 1011000.</br>

For every '1' in binary message we change 0-255 RGB value to even and for '0' to odd. </br>
After each binary sequence of a character there is a bit that indicates the end of message: '0' - message end; '1' - message continue </br>

Each character with message end indicator is stored on 3 pixels (3 pixel x 3 RGB values = 9 bits that can be stored).

### Example:
**Text to encrypt:** XY </br>
**Binary representation:** 01011000 01011001 </br>
**Binary with message end indicators**: 01011000**1**01011001**0** </br>
**Image pixels**: (100,230,93) (213,210,212) (141,53,53) (31,0,34) (99,90,211) (43,45,61)</br>
**Bit encryption**: </br>
> <span style="color:red">0</span><span style="color:green">1</span><span style="color:lightblue">0</span> </br>
> (<span style="color:red">100</span>,<span style="color:green">230</span>,<span style="color:lightblue">93</span>) </br>
> Encrypted: (100,231,92)

