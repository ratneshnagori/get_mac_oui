# get_mac_oui
Get OUI from MAC address

This python script will access the API and get all the information for provided MAC address.

It will print Company Name associated with the MAC.

Script can be run both as standalone or as function. 

Script usage as standalone:-
===========================
python3 get_mac_oui.py mac-address

E.g. - python3 get_mac_oui.py d46a.3542.2800

Script usage in Docker :-
=========================
docker run build-name mac-address 

E.g. - docker run get_mac_oui d46a.3542.2800

If the MAC address is valid the script will return the company information in string format :-

*************************************
python3 get_mac_oui.py d46a.3542.2800
Query:
	MAC address to check - d46a.3542.2800
Result:
	The company assosciated with MAC d46a.3542.2800 is - Cisco Systems, Inc
*************************************

If the MAC address is invalid the script will return "None" and print appropriate error :-

*************************************
python3 get_mac_oui.py d46dddd
Query:
	MAC address to check - d46dddd
Error:
	Could not find company information for the given MAC. Please check if MAC is correct
Result:
	The company assosciated with MAC d46dddd is - None
*************************************

*************************************
python3 get_mac_oui.py d4
Query:
	MAC address to check - d4
Error:
	Invalid MAC or OUI address was received.
Result:
	The company assosciated with MAC d4 is - None
*************************************
