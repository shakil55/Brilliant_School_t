import requests

def send_sms(phone_number, message):
    API_KEY = "YOUR_API_KEY"
    SENDER_ID = "YOUR_SENDER_ID"
    SMS_URL = "https://bulksmsbd.net/api/smsapi"

    payload = {
        "api_key": API_KEY,
        "senderid": SENDER_ID,
        "number": phone_number,
        "message": message
    }

    response = requests.post(SMS_URL, data=payload)

    if response.status_code == 200:
        return response.json()  # JSON response from the API
    else:
        return {"error": "Failed to send SMS"}
