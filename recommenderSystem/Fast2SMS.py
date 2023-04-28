# import requests
# url = "https://www.fast2sms.com/dev/bulk"
#
# # payload = "sender_id=FSTSMS&message=test&language=english&route=p&numbers=9999999999,888888888"
#
# payload = "sender_id=FSTSMS&amp;message=GoodMorning&amp;language=english&amp;route=p&amp;numbers=9970533440"
#
# headers = {
# 'authorization': "AR2dqJ9iCS0Lux7kTwG1ZDa8UXeIVv3M5tOcpsQnFhmbofjzy6MDNf6FbB8sWzOCdQmG9u0VIeqTJ5Uc",
# 'Content-Type': "application/x-www-form-urlencoded",
# 'Cache-Control': "no-cache",
# }
# response = requests.request("POST", url, data=payload, headers=headers)
# print(response.text)

# import requests
#
# url = "https://www.fast2sms.com/dev/bulkV2"
#
# querystring = {"authorization":"AR2dqJ9iCS0Lux7kTwG1ZDa8UXeIVv3M5tOcpsQnFhmbofjzy6MDNf6FbB8sWzOCdQmG9u0VIeqTJ5Uc", "message":"This is test message", "language":"english", "route":"q", "numbers":"9970533440"}
#
# headers = {
#     'cache-control': "no-cache"
# }
#
# response = requests.request("GET", url, headers=headers, params=querystring)
#
# print(response.text)

import urllib.request
import urllib.parse


def sendSMS(apikey, numbers, sender, message):
    data = urllib.parse.urlencode({'apikey': apikey, 'numbers': numbers,
                                   'message': message, 'sender': sender})
    data = data.encode('utf-8')
    request = urllib.request.Request("https://api.textlocal.in/send/?")
    f = urllib.request.urlopen(request, data)
    fr = f.read()
    return (fr)


resp = sendSMS('apikey', '918123456789',
               'Jims Autos', 'This is your message')
print(resp)