import requests




def messageSender(message):
   
    url = "https://discord.com/api/v9/channels/12566348930/messages"

    message =  message
    auth = "NTM5NDc4MzY4MTEwNzgDRHLibqAV1c"

    payload = {
    "content" : message
    }
    headers = {
    "Authorization":auth
    }
    
    res = requests.post(url=url,data=payload,headers=headers)


