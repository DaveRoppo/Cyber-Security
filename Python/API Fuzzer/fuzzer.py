# Import Requests and Sys libraries
import requests
import sys

# Create function to continue loop if status code 404 is returned by API, and to print relevant data otherwise 
def loop():
    # Create for loop to iterate through word list
    for word in sys.stdin:
        # Create variable for APi response
        res = requests.get(url=f"http:/*INSERT URL HERE*/{word.strip()}")
        if res.status_code == 404:
           loop()
        else:
           # Create variable to view all json data in API response
            data = res.json()
            print(data)
          # Print status code and the word from the list that triggered the response
            print(res.status_code)
            print(word)
loop()

# This API fuzzer script was inspired by PhD Security's YouTube course "Python for Hackers FULL COURSE | Bug Bounty & Ethical Hacking"


