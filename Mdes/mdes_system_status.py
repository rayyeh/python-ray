#
#
# Script-Name: example_mdes_system_status
#

from mastercardapicore import RequestMap, Config, APIException, OAuthAuthentication
from os.path import dirname, realpath, join
from mastercardmdescustomerservice import SystemStatus

def main():
	consumerKey = "YT8iexhqzg5vWetxDvntC5f13J6JFEnwlL8FTKtm7837dcf6!66f2fd60279d4e649c9343a6d0964d410000000000000000"
	# You should copy this from "My Keys" on your project page e.g. UTfbhDCSeNYvJpLL5l028sWL9it739PYh6LU5lZja15xcRpY!fd209e6c579dc9d7be52da93d35ae6b6c167c174690b72fa
	keyStorePath = "D:\keyalias-sandbox.p12"
	# e.g. /Users/yourname/project/sandbox.p12 | C:\Users\yourname\project\sandbox.p12
	keyAlias = "keyalias"   # For production: change this to the key alias you chose when you created your production key
	keyPassword = "keystorepassword"   # For production: change this to the key alias you chose when you created your production key

	auth = OAuthAuthentication(consumerKey, keyStorePath, keyAlias, keyPassword)
	Config.setAuthentication(auth)
	Config.setDebug(True) # Enable http wire logging
	Config.setSandbox(True)
	
	try:
		mapObj = RequestMap()
		response = SystemStatus.query(mapObj)
		print("SystemStatusResponse.CommentText--> %s") % response.get("SystemStatusResponse.CommentText") #SystemStatusResponse.CommentText-->System is fully operational.

	except APIException as e:
		print("HttpStatus: %s") % e.getHttpStatus()
		print("Message: %s") % e.getMessage()
		print("ReasonCode: %s") % e.getReasonCode()
		print("Source: %s") % e.getSource()

if __name__ == "__main__": main()
