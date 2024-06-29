import requests




def messageSender(message):
   
    url = "https://discord.com/api/v9/channels/1256640121940348930/messages"

    message =  message
    auth = "NTM5NDc4MzY4MTEwNzcyMjI1.GqYjyE.d7fWKZWHqxjmXe2yPR2OIkOd_VgDRHLibqAV1c"

    payload = {
    "content" : message
    }
    headers = {
    "Authorization":auth
    }
    
    res = requests.post(url=url,data=payload,headers=headers)


