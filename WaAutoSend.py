import pywhatkit as pw
import pyautogui
import keyboard as k

# -- first, you have to install python and pywhatkit libary

# -- installing python
# you can install python by downloading the file and viewing the tutorial from here https://www.python.org/downloads/

# -- installing pywhatkit
# pip install pywhatkit

print("-----------------------------------------\nPYTHON SCRIPT WA AUTO SEND - BY FERDYHAPE\n-----------------------------------------\n")
print("HOW to use this tool?\n-----------------------------------------\n1. Run script code\n2. input destination number (use country code, example: +62xxxx)2. Input the time in hours and minutes (at least 2 minutes difference from the current time)\n3. Input waiting time your computer open the browser(within second, default 30s, if you have fast connection, you can change to 10s, ex: 10, 20)\n4. Enter Close tab time, your browser will auto close whatsapp tab after sending message (input within seconds, default 15, ex: 10, 20)\n5. Input message\n6. Wait for the message to be sent")

while True:
    print('\n-----------------------------------------')
    phonumb = str(input("Phone Number: "))
    hour = int(input("Time Hour: "))
    min = int(input("Time Min: "))
    wait_time = int(input("Wait Time: "))
    close_tab_time = int(input("Close tab time: "))
    message = str(input("Message: "))

    if wait_time == "":
        wait_time = 30

    if close_tab_time == "":
        close_tab_time = 15

    pw.sendwhatmsg(phonumb, message, hour, min, wait_time, True, close_tab_time)
    print(r'Message successfully sent!')
    print('-----------------------------------------\n')
    if input('Do you want to schedule a message again? ').lower() != 'y':
        break
