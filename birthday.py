# This's a automatic birthday wisher program.
# A birday message will be sent automatically to a particular person whom will add in 'bdayfile.txt'
# Note : Pls take care of the format when you add someone's details in 'bdayfile.txt'
# Feel free to ask if have any doubt...

from datetime import datetime
from plyer import notification
import time
import pywhatkit

# Path of file
bdayfile = r'D:\Python\Project\bdayfile.txt'

def birthdayReminder():
    filename = open(bdayfile, "r")
    today = time.strftime('%d%m')
    bday = False

    for bday_date in filename:
        if today in bday_date:
            bday_date = bday_date.split(' ')
            bday = True
            if __name__ == "__main__":
                notification.notify(
                    title="Birthday Reminder!",
                    message='''"Wishing a happy birthday!"''',
                    app_name = 'Automatic Birthday Wisher',
                    app_icon=r"C:\Users\shami_20topwo\Downloads\Juliewiens-Christmas-Gift.ico",
                    #Path of icon which will appear in notification
                    timeout=3
                )
            if bday == True : 
             pywhatkit.sendwhatmsg(bday_date[3], "Happy birthday dear!", 17, 38)

if __name__ == '__main__':
    birthdayReminder()