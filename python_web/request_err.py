#Using request library to access internet data
import requests
from requests import HTTPError, Timeout

def main():

    #Get an standard error
    try:
        #url = "http://httpbin.org/status/404"
        url = "http://httpbin.org/delay/5"
        result = requests.get(url, timeout=2)
        result.raise_for_status()
        printResults(result)
    except HTTPError as err:
        print("Error: {0}".format(err))
    except Timeout as err:
        print("Request timed out: \n {0}".format(err))
    




def printResults(resData):
    print("Result code: {0}".format(restData.status_code))
    print("\n")

    print("Headers: ---------------------")
    print(restData.headers)
    print("\n")

    print("Returned Data: ----------------------")
    print(restData.text)


if __name__ == "__main__":
    main()