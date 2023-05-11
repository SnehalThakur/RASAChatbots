# import required module
import requests
import json


def sendSMSToPatient(message="Thank you for contacting us. Your appointment has been scheduled successfully"):
    # mention url
    url = "https://www.fast2sms.com/dev/bulkV2"

    # create a dictionary
    my_data = {
        # Your default Sender ID
        'sender_id': 'FSTSMS',

        # Put your message here!
        'message': message,

        'language': 'english',
        'route': 'p',

        # You can send sms to multiple numbers
        # separated by comma. ,8669416075,8530695473,8530426407
        'numbers': '8669416075,8530695473,8530426407'
    }

    # create a dictionary
    headers = {
        'authorization': 'AR2dqJ9iCS0Lux7kTwG1ZDa8UXeIVv3M5tOcpsQnFhmbofjzy6MDNf6FbB8sWzOCdQmG9u0VIeqTJ5Uc',
        'Content-Type': "application/x-www-form-urlencoded",
        'Cache-Control': "no-cache"
    }

    # make a post request
    response = requests.request("POST",
                                url,
                                data=my_data,
                                headers=headers)

    # load json data from source
    returned_msg = json.loads(response.text)

    # print to send message
    print(returned_msg['message'])
