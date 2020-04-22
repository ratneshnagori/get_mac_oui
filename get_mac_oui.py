import requests
import sys

#Function to access macaddress.io API and extract Info into JSON format
def get_mac_oui(argv):
    try:
        #call the api
        result = requests.get('https://api.macaddress.io/v1?',
	    params= {'apiKey': 'at_6YhPKq9ETW5TrHgerWMqbYPW1Ri25', 'output': 'json' , 'search': argv})

        #return the company information
        if result.json()["vendorDetails"]["companyName"] != '':
            return result.json()["vendorDetails"]["companyName"]

        #return NONE if MAC is valid but doesn't exists.
        print("Error:\n\tCould not find company information for the given MAC. Please check if MAC is correct")
        return None
    except:
        #if MAC is invalid
        if result.status_code == 422:
            print("Error:\n\tInvalid MAC or OUI address was received.")
            return None
        
        #if encountered any other error while accessing APIs
        print("Error:\n\tUnexpected error encountered. Code: " + result.status_code)
        return None

if __name__ ==  "__main__":
    if len(sys.argv) <= 1:
        print("Usage: get_mac_oui.py mac-address")
    else:
        #to print "help" text
        if sys.argv[1] == "--h" or sys.argv[1] == "--help":
            print("Usage: get_mac_oui.py mac-address")
        else:
            print("Query:\n\tMAC address to check - " + sys.argv[1])
            company_info = get_mac_oui(sys.argv[1])
            print("Result:\n\tThe company assosciated with MAC " + sys.argv[1] + " is - "  + str(company_info))