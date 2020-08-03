#Handling different type of errors
import urllib.request
from http import HTTPStatus
from urllib.error import HTTPError, URLError

def main():
    #url = "http://no-way-this-exist.org" #Will generate URLError
    #url = "http://httpbin.org/status/404" #Will generate HTTPError
    url = "http://httpbin.org/html" #should work

    #Use exeption handling to attempt to URL Access

    try:
        result = urllib.request.urlopen(url)
        print("Result code: {0}".format(result.status))
        if (result.getcode() == HTTPStatus.OK):
            print(result.read().decode('utf-8'))
    except HTTPError as err:
        print("We got this error: {0}".format(err.code))
    except URLError as err:
        print("This site has a problem {0}".format(err.reason))
    

if __name__ == "__main__":
    main()