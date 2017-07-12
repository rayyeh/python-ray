#
#
# Script-Name: example_mdes_search_token_unique_ref
#

from mastercardapicore import RequestMap, Config, APIException, OAuthAuthentication
from os.path import dirname, realpath, join
from mastercardmdescustomerservice import Search


def main():
    consumerKey = "YT8iexhqzg5vWetxDvntC5f13J6JFEnwlL8FTKtm7837dcf6!17c438eb264f403f80d8fada38b34e1b0000000000000000"
    # You should copy this from "My Keys" on your project page e.g. UTfbhDCSeNYvJpLL5l028sWL9it739PYh6LU5lZja15xcRpY!fd209e6c579dc9d7be52da93d35ae6b6c167c174690b72fa
    keyStorePath = "D:\ub-mdescs-1499832439-sandbox.p12"
    # e.g. /Users/yourname/project/sandbox.p12 | C:\Users\yourname\project\sandbox.p12
    keyAlias = "keyalias"  # For production: change this to the key alias you chose when you created your production key
    keyPassword = "keystorepassword"  # For production: change this to the key alias you chose when you created your production key

    auth = OAuthAuthentication(consumerKey, keyStorePath, keyAlias, keyPassword)
    Config.setAuthentication(auth)
    Config.setDebug(True)  # Enable http wire logging
    Config.setSandbox(True)

    try:
        mapObj = RequestMap()
        mapObj.set("SearchRequest.TokenUniqueReference", "DWSPMC00000000010906a349d9ca4eb1a4d53e3c90a11d9c")
        mapObj.set("SearchRequest.AuditInfo.UserId", "A1435477")
        mapObj.set("SearchRequest.AuditInfo.UserName", "John Smith")
        mapObj.set("SearchRequest.AuditInfo.Organization", "Any Bank")
        mapObj.set("SearchRequest.AuditInfo.Phone", "5555551234")

        response = Search.create(mapObj)
        print("SearchResponse.Accounts.Account[0].AccountPanSuffix--> %s") % response.get(
            "SearchResponse.Accounts.Account[0].AccountPanSuffix")  # SearchResponse.Accounts.Account[0].AccountPanSuffix-->1234
        print("SearchResponse.Accounts.Account[0].ExpirationDate--> %s") % response.get(
            "SearchResponse.Accounts.Account[0].ExpirationDate")  # SearchResponse.Accounts.Account[0].ExpirationDate-->1215
        print("SearchResponse.Accounts.Account[0].AlternateAccountIdentifierSuffix--> %s") % response.get(
            "SearchResponse.Accounts.Account[0].AlternateAccountIdentifierSuffix")  # SearchResponse.Accounts.Account[0].AlternateAccountIdentifierSuffix-->4300
        print("SearchResponse.Accounts.Account[0].Tokens.Token[0].TokenUniqueReference--> %s") % response.get(
            "SearchResponse.Accounts.Account[0].Tokens.Token[0].TokenUniqueReference")  # SearchResponse.Accounts.Account[0].Tokens.Token[0].TokenUniqueReference-->DWSPMC00000000010906a349d9ca4eb1a4d53e3c90a11d9c
        print(
            "SearchResponse.Accounts.Account[0].Tokens.Token[0].PrimaryAccountNumberUniqueReference--> %s") % response.get(
            "SearchResponse.Accounts.Account[0].Tokens.Token[0].PrimaryAccountNumberUniqueReference")  # SearchResponse.Accounts.Account[0].Tokens.Token[0].PrimaryAccountNumberUniqueReference-->FWSPMC0000000004793dac803f190a4dca4bad33c90a11d3
        print("SearchResponse.Accounts.Account[0].Tokens.Token[0].TokenSuffix--> %s") % response.get(
            "SearchResponse.Accounts.Account[0].Tokens.Token[0].TokenSuffix")  # SearchResponse.Accounts.Account[0].Tokens.Token[0].TokenSuffix-->7639
        print("SearchResponse.Accounts.Account[0].Tokens.Token[0].ExpirationDate--> %s") % response.get(
            "SearchResponse.Accounts.Account[0].Tokens.Token[0].ExpirationDate")  # SearchResponse.Accounts.Account[0].Tokens.Token[0].ExpirationDate-->0216
        print("SearchResponse.Accounts.Account[0].Tokens.Token[0].AccountPanSequenceNumber--> %s") % response.get(
            "SearchResponse.Accounts.Account[0].Tokens.Token[0].AccountPanSequenceNumber")  # SearchResponse.Accounts.Account[0].Tokens.Token[0].AccountPanSequenceNumber-->002
        print("SearchResponse.Accounts.Account[0].Tokens.Token[0].DigitizationRequestDateTime--> %s") % response.get(
            "SearchResponse.Accounts.Account[0].Tokens.Token[0].DigitizationRequestDateTime")  # SearchResponse.Accounts.Account[0].Tokens.Token[0].DigitizationRequestDateTime-->2015-01-20T18:04:35-06:00
        print("SearchResponse.Accounts.Account[0].Tokens.Token[0].TokenActivatedDateTime--> %s") % response.get(
            "SearchResponse.Accounts.Account[0].Tokens.Token[0].TokenActivatedDateTime")  # SearchResponse.Accounts.Account[0].Tokens.Token[0].TokenActivatedDateTime-->2015-01-20T18:04:35-06:00
        print("SearchResponse.Accounts.Account[0].Tokens.Token[0].FinalTokenizationDecision--> %s") % response.get(
            "SearchResponse.Accounts.Account[0].Tokens.Token[0].FinalTokenizationDecision")  # SearchResponse.Accounts.Account[0].Tokens.Token[0].FinalTokenizationDecision-->A
        print("SearchResponse.Accounts.Account[0].Tokens.Token[0].CorrelationId--> %s") % response.get(
            "SearchResponse.Accounts.Account[0].Tokens.Token[0].CorrelationId")  # SearchResponse.Accounts.Account[0].Tokens.Token[0].CorrelationId-->101234
        print("SearchResponse.Accounts.Account[0].Tokens.Token[0].CurrentStatusCode--> %s") % response.get(
            "SearchResponse.Accounts.Account[0].Tokens.Token[0].CurrentStatusCode")  # SearchResponse.Accounts.Account[0].Tokens.Token[0].CurrentStatusCode-->A
        print("SearchResponse.Accounts.Account[0].Tokens.Token[0].CurrentStatusDescription--> %s") % response.get(
            "SearchResponse.Accounts.Account[0].Tokens.Token[0].CurrentStatusDescription")  # SearchResponse.Accounts.Account[0].Tokens.Token[0].CurrentStatusDescription-->Active
        print("SearchResponse.Accounts.Account[0].Tokens.Token[0].ProvisioningStatusCode--> %s") % response.get(
            "SearchResponse.Accounts.Account[0].Tokens.Token[0].ProvisioningStatusCode")  # SearchResponse.Accounts.Account[0].Tokens.Token[0].ProvisioningStatusCode-->S
        print("SearchResponse.Accounts.Account[0].Tokens.Token[0].ProvisioningStatusDescription--> %s") % response.get(
            "SearchResponse.Accounts.Account[0].Tokens.Token[0].ProvisioningStatusDescription")  # SearchResponse.Accounts.Account[0].Tokens.Token[0].ProvisioningStatusDescription-->Provisioning successful
        print("SearchResponse.Accounts.Account[0].Tokens.Token[0].TokenRequestorId--> %s") % response.get(
            "SearchResponse.Accounts.Account[0].Tokens.Token[0].TokenRequestorId")  # SearchResponse.Accounts.Account[0].Tokens.Token[0].TokenRequestorId-->00212345678
        print("SearchResponse.Accounts.Account[0].Tokens.Token[0].WalletId--> %s") % response.get(
            "SearchResponse.Accounts.Account[0].Tokens.Token[0].WalletId")  # SearchResponse.Accounts.Account[0].Tokens.Token[0].WalletId-->103
        print("SearchResponse.Accounts.Account[0].Tokens.Token[0].PaymentAppInstanceId--> %s") % response.get(
            "SearchResponse.Accounts.Account[0].Tokens.Token[0].PaymentAppInstanceId")  # SearchResponse.Accounts.Account[0].Tokens.Token[0].PaymentAppInstanceId-->92de9357a535b2c21a3566e446f43c532a46b54c46
        print("SearchResponse.Accounts.Account[0].Tokens.Token[0].TokenType--> %s") % response.get(
            "SearchResponse.Accounts.Account[0].Tokens.Token[0].TokenType")  # SearchResponse.Accounts.Account[0].Tokens.Token[0].TokenType-->S
        print("SearchResponse.Accounts.Account[0].Tokens.Token[0].LastCommentId--> %s") % response.get(
            "SearchResponse.Accounts.Account[0].Tokens.Token[0].LastCommentId")  # SearchResponse.Accounts.Account[0].Tokens.Token[0].LastCommentId-->2376
        print("SearchResponse.Accounts.Account[0].Tokens.Token[0].Device.DeviceId--> %s") % response.get(
            "SearchResponse.Accounts.Account[0].Tokens.Token[0].Device.DeviceId")  # SearchResponse.Accounts.Account[0].Tokens.Token[0].Device.DeviceId-->3e5edf24a24ba98e27d43e345b532a245e4723d7a9c4f624e93452c92de9357a535b2c21a3566e446f43c532d34s6
        print("SearchResponse.Accounts.Account[0].Tokens.Token[0].Device.DeviceName--> %s") % response.get(
            "SearchResponse.Accounts.Account[0].Tokens.Token[0].Device.DeviceName")  # SearchResponse.Accounts.Account[0].Tokens.Token[0].Device.DeviceName-->John Phone
        print("SearchResponse.Accounts.Account[0].Tokens.Token[0].Device.DeviceType--> %s") % response.get(
            "SearchResponse.Accounts.Account[0].Tokens.Token[0].Device.DeviceType")  # SearchResponse.Accounts.Account[0].Tokens.Token[0].Device.DeviceType-->09
        print("SearchResponse.Accounts.Account[0].Tokens.Token[0].Device.SecureElementId--> %s") % response.get(
            "SearchResponse.Accounts.Account[0].Tokens.Token[0].Device.SecureElementId")  # SearchResponse.Accounts.Account[0].Tokens.Token[0].Device.SecureElementId-->92de9357a535b2c21a3566e446f43c532a46b54c46
        print("SearchResponse.Accounts.Account[0].Tokens.Token[0].TokenDeletedFromConsumerApp--> %s") % response.get(
            "SearchResponse.Accounts.Account[0].Tokens.Token[0].TokenDeletedFromConsumerApp")  # SearchResponse.Accounts.Account[0].Tokens.Token[0].TokenDeletedFromConsumerApp-->false

    except APIException as e:
        print("HttpStatus: %s") % e.getHttpStatus()
        print("Message: %s") % e.getMessage()
        print("ReasonCode: %s") % e.getReasonCode()
        print("Source: %s") % e.getSource()


if __name__ == "__main__": main()
