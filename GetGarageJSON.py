#Program to dump JSON data from the Parking Services API
#11/25/2024
#Jackson Vaughn

import requests
import json
#Constant
URL = 'https://secure.parking.ucf.edu/GarageCounter/GetOccupancy'
        

#dumps the JSON into a file for keeping.
def DumpJSON(URL):
    #send GET request

    try:
        r = requests.get(URL)
    except:
        print(Exception)

    #dump JSON into a file for easier viewing
    ParkingData = r.json()
    with open('ParkingData.json' , 'w') as json_file:
        json.dump(ParkingData, json_file,indent=4)

    #For each garage print out the name, available and total spots.
    #We know there are 9 garages/lots
    GaragesList = []
    for Garage in range(0,9):
        GarageName = ParkingData[Garage]['location']['name']
        GarageAvailable = ParkingData[Garage]['location']['counts']['available']
        GarageTotal = ParkingData[Garage]['location']['counts']['total']
        GarageOccupied = ParkingData[Garage]['location']['counts']['occupied']

        #Prints out for debugging
        print(f'Garage: {GarageName}')
        print(f'Spots available: {GarageAvailable}')
        print(f'Total spots: {GarageTotal}')
        print(f'Occupied spots: {GarageOccupied}\n')


        #put the garages and other info into a JSON so its easier to read what we need.
        #also easier to transmit to a JavaScript file
        with open('Garages.json' , 'w') as json_file:
            json.dump(ParkingData, json_file,indent=4)

        

DumpJSON(URL)
