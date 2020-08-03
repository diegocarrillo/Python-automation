#Using basic authentication with requests library
import requests
from requests.auth import HTTPBasicAuth

def main():
    #Access a URL that requires authentication - the format of this
    #URL is that you provive the user/password to auth againts
    url = "http://httpbin.org/basic-auth/DiegoC/MyStrongPass"
    
    #Create credentials 
    myCreds = HTTPBasicAuth("DiegoC", "MyStrongPass")

    #Issue the requets with the authentication credentials
    result = requests.get(url, auth=myCreds) #We could use auth="DiegoC", "MyStrongPass"

    printResults(result)
    
def printResults(restData):
    print("Result code: {0}".format(restData.status_code))
    print("\n")

    print("Headers: ---------------------")
    print(restData.headers)
    print("\n")

    print("Returned Data: ----------------------")
    print(restData.text)


if __name__ == "__main__":
    main()