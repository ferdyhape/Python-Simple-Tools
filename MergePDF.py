from PyPDF2 import PdfMerger

# -- first, you have to install python and PyPDF2 libary

# -- installing python
# you can install python by downloading the file and viewing the tutorial from here https://www.python.org/downloads/

# -- installing pillow
# pip install PyPDF2

print("-----------------------------------------\nPYTHON SCRIPT MERGE PDF - BY FERDYHAPE\n-----------------------------------------\n\n")


print("HOW to use this tool?\n-----------------------------------------\n1. prepare an pdf file in a local directory (make sure the image file name is without spaces ex: file_image.jpg, fileimage.jpg)\n2. prepare a local path folder for pdf storage (if you dont want to always include the local path folder, change the default save in line 20 of the code)\n3. Run the script code\n4. if asked to input the image path, directly drag and drop the image file to the terminal the code works\n5. enter the local path folder for storing pdf files (if you have changed the default, you just have to enter without inputting) \n6. enter file name (without .pdf)")


merger = PdfMerger()
while True:
    print('\n-----------------------------------------')
    pdf_files = []
    pdf_files.clear()
    while True:
        input_path = input("input path: ")
        pdf_files.append(input_path)
        if input('Do You Want To Insert PDF again?(Y/N) ').lower() != 'y':
            break

    for pdf_file in pdf_files:
        merger.append(pdf_file)

    path = input('Input new path: ')

    if path == "":
        # -- Default path at on D:\POLINEMA\tes pdf\, enter without input if you dont want to change the path
        path = 'D:\\POLINEMA\\tes pdf\\'

    name = input('Input name for merged pdf: ')
    pathwithname = path + name
    merger.write(pathwithname)
    merger.close()
    if input('Do You Want Merge PDF again?(Y/N) ').lower() != 'y':
        break