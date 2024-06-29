# from tkinter import *
# from tkinter import messagebox
 

# date_string = "Emre"
               
# news = "Uygun Tarih Bulundu 😇 {}".format(date_string)

# messagebox.showwarning("US Citizen Hacking", news)

from datetime import datetime

# print("inactive olma", inactivetime)

# {
#   "value": "70ff318d8dcdbe92",
#   "inactiveAt": 1719666628704,
#   "expiresAt": 1719675650120,
#   "updatedAt": 1719664831299,
#   "sessionReplayMode": 0,
#   "sessionReplaySentFirstChunk": false,
#   "sessionTraceMode": 0,
#   "traceHarvestStarted": false,
#   "serverTimeDiff": -206,
#   "custom": {}
# }

def calculateDurationFromEpoch(epoch):

    epoch = epoch/1000
    now =  datetime.now()
    expires = datetime.fromtimestamp(epoch)
    duration = expires - now
    kalan_sure = round((duration.total_seconds()/60))
    
    return kalan_sure


# expiresAt
# : 
# 1719626161509
# inactiveAt
# : 
# # 1719613767810

# epoch_time1expires = 1719675650120/1000
# epoch_time2inactive = 1719667123700/1000
# now =  datetime.now()
# expires = datetime.fromtimestamp(epoch_time1expires)
# inactivetime = datetime.fromtimestamp(epoch_time2inactive)

# ex=expires-now
# inac =inactivetime-now

# print("expires", expires)
# print("inactive", inactivetime)

# print("kalan ex",ex)
# print(inac)
# print("kalan inactive",inac.total_seconds()/60)

# print("kalan inactive",round(inac.total_seconds()/60))

