import os
import requests

SMS_ENDPOINT = os.environ.get("SMS_API")
SMS_USER = os.environ.get("SMS_USER")
SMS_PASSWORD = os.environ.get("SMS_PASSWORD")

def send_confirmation_sms(phone_number):

	confrimation_message = (
		"Your rescue request has been registered, we will follow up soon. Stay safe"
		)
	api_url ="{}?username={}?password={}&message={}&numbers={}&senderid=KSITMK".format(
		SMS_ENDPOINT,
		SMS_USER,
		SMS_PASSWORD,
		confrimation_message,
		phone_number.lstrip("0"),
	)
	try:
		request.get(api_url, timeout=1)
	except Exception as e:
		pass