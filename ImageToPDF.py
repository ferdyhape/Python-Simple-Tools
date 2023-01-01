from PIL import Image
# -- first, you have to install python and pillow libary

# -- installing python
# you can install python by downloading the file and viewing the tutorial from here https://www.python.org/downloads/

# -- installing pillow
# pip install Pillow 

print("-----------------------------------------\nPYTHON SCRIPT IMAGE TO PDF - BY FERDYHAPE\n-----------------------------------------\n")


print("HOW to use this tool?\n-----------------------------------------\n1. prepare an image file in a local directory (make sure the image file name is without spaces ex: file_image.jpg, fileimage.jpg)\n2. prepare a local path folder for pdf storage (if you dont want to always include the local path folder, change the default save in line 26 of the code)\n3. Run the script code\n4. if asked to input the image path, directly drag and drop the image file to the terminal the code works\n5. enter the local path folder for storing pdf files (if you have changed the default, you just have to enter without inputting)\n6. enter file name (without .pdf)")

repeat = "y"
while True:
    print('\n-----------------------------------------')
    image_input = input('Input image path: ')
    image_input = Image.open(image_input)
    image_converted = image_input.convert('RGB')

    path = input('Input new path: ')

    if path == "":
    # -- Default path at on D:\POLINEMA\Converted\ImageToPDF, enter without input if you dont want to change the path
        path = 'D:\\POLINEMA\\Converted\\ImageToPDF\\'

    name = input('Input name for pdf: ')
    pathwithname = path + name
    image_converted.save(pathwithname + '.pdf')
    print('-- pdf saved successfully on ' + path + ' with name ' + name + '.pdf')
    print('-----------------------------------------\n')
    if input('Do You Want To Continue? ').lower() != 'y':
        break