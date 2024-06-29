# from tkinter import *
# from tkinter import messagebox
 

# date_string = "Emre"
               
# news = "Uygun Tarih Bulundu 😇 {}".format(date_string)

# messagebox.showwarning("US Citizen Hacking", news)

from datetime import datetime


# expiresAt
# : 
# 1719626161509
# inactiveAt
# : 
# 1719613767810



epoch_time1expires = 1719626161509/1000
epoch_time2inactive = 1719614396442/1000
now =  datetime.now()
expires = datetime.fromtimestamp(epoch_time1expires)
inactivetime = datetime.fromtimestamp(epoch_time2inactive)

print("expires", expires)
print("inactive olma", inactivetime)



