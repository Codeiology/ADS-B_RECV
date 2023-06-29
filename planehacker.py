# Import dependencies

import os
import sys
import signal
import requests
import time
import colorama
from colorama import Fore, Back, Style

# Initialize functions and variables

colorama.init()

user_interrupt_occured = False
def user_interrupt(signal, frame):
    global user_interrupt_occured
    user_interrupt_occured = True
    print("")
    print("Program stopped.")
    print("")
    sys.exit()
signal.signal(signal.SIGINT, user_interrupt)

def connectionstatus():
    headers = {
        'Accept': 'application/json'
    }
    response = requests.get('https://api.adsbdb.com/v0/online', timeout=5, headers=headers)
    if response.status_code == 200:
        return True
    else:
        return False

def anim(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.001)
    print("")

def animslow(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.05)
    print("")

def loading_screen(message):
    print(message, end="")
    spinner = ["|", "/", "-", "\\"]
    start_time = time.time()
    i = 0
    while True:
        if time.time() - start_time > 3:
            print("\b \b" * (len(message) + 1), end="")
            break
        print(f"\b{spinner[i%4]}", end="", flush=True)
        i += 1
        time.sleep(0.05)
        
# The main attraction

os.system("clear")
anim('''
            ______
            _\ _~-\___
    =  = ==(____AA____D
                \_____\___________________,-~~~~~~~`-.._
                /     o O o o o o O O o o o o o o O o  |\_
                `~-.__        ___..----..                  )             -=[Receivers provided by ADS-B One https://api.adsb.one]=-
                      `---~~\___________/------------`````
                      =  ===(_________D
                                                                                         -=[Coded by Taj Entabi]=-
                                                                                         
                                                                                                                      
                                                                                                                               
       db        88888888ba,    ad88888ba           88888888ba            88888888ba  88888888888 ,ad8888ba,  8b           d8
      d88b       88      `"8b  d8"     "8b          88      "8b           88      "8b 88         d8"'    `"8b `8b         d8'
     d8'`8b      88        `8b Y8,                  88      ,8P           88      ,8P 88        d8'            `8b       d8'
    d8'  `8b     88         88 `Y8aaaaa,            88aaaaaa8P'           88aaaaaa8P' 88aaaaa   88              `8b     d8'
   d8YaaaaY8b    88         88   `"""""8b, aaaaaaaa 88""""""8b,           88""""88'   88"""""   88               `8b   d8'
  d8""""""""8b   88         8P         `8b """""""" 88      `8b           88    `8b   88        Y8,               `8b d8'
 d8'        `8b  88      .a8P  Y8a     a8P          88      a8P           88     `8b  88         Y8a.    .a8P      `888'
d8'          `8b 88888888Y"'    "Y88888P"           88888888P"            88      `8b 88888888888 `"Y8888Y"'        `8'
                                                                                                                               
                                                               888888888888
                      
''')
loading_screen("Connecting to ADS-B geostationary receivers... ")
good2go = connectionstatus()
if good2go:
    print(Fore.GREEN + "\nCONNECTED\n" + Fore.RESET)
    loading_screen("Readying the ADS-B geostationary receivers... ")
    def unixtime():
        current = int(time.time())
        return current
    global jsonheaders
    jsonheaders = {
        'Accept': 'application/json'
    }
    def getmil():
        response = requests.get('https://api.adsb.one/v2/mil/', headers=jsonheaders)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Something went wrong. Status code: {response.status_code}")
            exit()
    def getladd():
        response = requests.get('https://api.adsb.one/v2/ladd/', headers=jsonheaders)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Something went wrong. Status code: {response.status_code}")
            exit()
    def getpia():
        response = requests.get('https://api.adsb.one/v2/pia/', headers=jsonheaders)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Something went wrong. Status code: {response.status_code}")
            exit()
    def gethex(hex):
        hex2 = hex.upper()
        response = requests.get(f'https://api.adsb.one/v2/hex/{hex2}', headers=jsonheaders)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Something went wrong. Status code: {response.status_code}")
            exit()
    def getcall(call):
        response = requests.get(f'https://api.adsb.one/v2/callsign/{call}', headers=jsonheaders)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Something went wrong. Status code: {response.status_code}")
            exit()
    def getreg(reg):
        response = requests.get(f'https://api.adsb.one/v2/reg/{reg}', headers=jsonheaders)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Something went wrong. Status code: {response.status_code}")
            exit()
    def gettype(typ):
        response = requests.get(f'https://api.adsb.one/v2/type/{typ}', headers=jsonheaders)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Something went wrong. Status code: {response.status_code}")
            exit()
    def getsquawk(squawk):
        response = requests.get(f'https://api.adsb.one/v2/squawk/{squawk}', headers=jsonheaders)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Something went wrong. Status code: {response.status_code}")
            exit()
    def getloc(lat, lon, rad):
        response = requests.get(f'https://api.adsb.one/v2/point/{lat}/{lon}/{rad}', headers=jsonheaders)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Something went wrong. Status code: {response.status_code}")
            exit()
    def parse(data):
        ac_data = data["ac"]
        print("████████████████████████████████████████████████████████████████████████████████████████████████████████")
        for aircraft in ac_data:
            flight = aircraft.get("flight")
            lat = aircraft.get("lat")
            lon = aircraft.get("lon")
            alt = aircraft.get("alt_baro")
            speed = aircraft.get("gs")
            seen = str(aircraft.get("seen"))
            squawk = aircraft.get("squawk")
            rssi = aircraft.get("rssi")
            emerg = aircraft.get("emergency")
            hexid = aircraft.get("hex")
            craftyp = aircraft.get("t")
            receivers = aircraft.get("recentReceiverIds")
            print()
            if flight is not None:
                anim(f"URL:  https://flightaware.com/live/flight/{flight}")
                anim(f"Flight: {flight}")
            else:
                anim("Flight: NOT FOUND")
            if lat is not None:
                anim(f"Latitude: {lat}")
            else:
                anim("Latitude: NOT FOUND")
            if lon is not None:
                anim(f"Longitude: {lon}")
            else:
                anim("Longitude: NOT FOUND")
            if alt is not None:
                if alt == 'ground':
                    anim("Altitude: LANDED")
                else:
                    anim(f"Altitude: {alt} feet")
            else:
                anim("Altitude: NOT FOUND")
            if speed is not None:
                anim(f"Speed: {speed} knots")
            else:
                anim("Speed: NOT FOUND")
            if seen is not None:
                anim(f"Last seen: {seen} seconds ago")
            else:
                anim("Last seen: NOT FOUND")
            if hexid is not None:
                anim(f"Hexadecimal ID: {hexid}")
            else:
                anim("Hexadecimal ID: NOT FOUND")
            if squawk is not None:
                anim(f"SQUAWK code: {squawk}")
            else:
                anim("SQUAWK code: NOT FOUND")
            if emerg is not None:
                if emerg == 'none':
                    anim("Situation: Normal")
                else:
                    anim(Fore.RED + f"ON BOARD EMERGENCY: {emerg}" + Fore.RESET)
            else:
                anim("Situation: NOT FOUND")
            if rssi is not None:
                anim(f"RECV_RSSI: {rssi}")
            else:
                anim(f"RECV_RSST: NOT FOUND")
            if craftyp is not None:
                anim(f"Aircraft model: {craftyp}")
            else:
                anim(f"Aircraft model: NOT FOUND")
            if receivers is not None:
                print("RECEIVER IDs:")
                for receiver in receivers:
                    anim(receiver)
            else:
                print(f"RECEIVER IDs NOT FOUND.")
            print("████████████████████████████████████████████████████████████████████████████████████████████████████████")
            print()
    print(Fore.GREEN + "\nREADY\n" + Fore.RESET)
    while True:
        anim('''
The following options are currently available:

[1] Get info for all aircrafts flagged as [MILITARY]
[2] Get info for all aircrafts flagged as [LADD]
[3] Get info for all aircrafts flagged as [PIA]
[4] Target all aircrafts with a specific Mode S hexadecimal identification
[5] Target specific aircraft by callsign
[6] Target specific aircraft by registration code
[7] Target all aircrafts with ICAO type codes
[8] Target aircrafts that are "squawking" the specified value
[9] Specify a point with longitude and latitude and find aircrafts within a certain radius
    ''')
        menuchoice = input("Choose a number: ")
        if menuchoice == "1":
            print("AIMING RECEIVERS...")
            time.sleep(1)
            print("DETECTING PACKETS...")
            time.sleep(1.5)
            print("DECODING PACKETS...")
            time.sleep(0.5)
            print("PARSING DATA...")
            data = getmil()
            print()
            print()
            parse(data)
        elif menuchoice == "2":
            print("AIMING RECEIVERS...")
            time.sleep(1)
            print("DETECTING PACKETS...")
            time.sleep(1.5)
            print("DECODING PACKETS...")
            time.sleep(0.5)
            print("PARSING DATA...")
            data = getladd()
            print()
            print()
            parse(data)
        elif menuchoice == "3":
            print("AIMING RECEIVERS...")
            time.sleep(1)
            print("DETECTING PACKETS...")
            time.sleep(1.5)
            print("DECODING PACKETS...")
            time.sleep(0.5)
            print("PARSING DATA...")
            data = getpia()
            print()
            print()
            parse(data)
        elif menuchoice == "4":
            hex = input("\nHexadecimal Mode S Identification? ")
            print()
            print("AIMING RECEIVERS...")
            time.sleep(1)
            print("DETECTING PACKETS...")
            time.sleep(1.5)
            print("DECODING PACKETS...")
            time.sleep(0.5)
            print("PARSING DATA...")
            data = gethex(hex)
            print()
            print()
            parse(data)
        elif menuchoice == "5":
            call = input("\nCallsign? ")
            print()
            print("AIMING RECEIVERS...")
            time.sleep(1)
            print("DETECTING PACKETS...")
            time.sleep(1.5)
            print("DECODING PACKETS...")
            time.sleep(0.5)
            print("PARSING DATA...")
            data = getcall(call)
            print()
            print()
            parse(data)
        elif menuchoice == "6":
            reg = input("\nRegistration code? ")
            print()
            print("AIMING RECEIVERS...")
            time.sleep(1)
            print("DETECTING PACKETS...")
            time.sleep(1.5)
            print("DECODING PACKETS...")
            time.sleep(0.5)
            print("PARSING DATA...")
            data = getreg(reg)
            print()
            print()
            parse(data)
        elif menuchoice == "7":
            typ = input("\nICAO Type code? ")
            print()
            print("AIMING RECEIVERS...")
            time.sleep(1)
            print("DETECTING PACKETS...")
            time.sleep(1.5)
            print("DECODING PACKETS...")
            time.sleep(0.5)
            print("PARSING DATA...")
            data = gettype(typ)
            print()
            print()
            parse(data)
        elif menuchoice == "8":
            sqwa = input("\nSquawking value? ")
            print()
            print("AIMING RECEIVERS...")
            time.sleep(1)
            print("DETECTING PACKETS...")
            time.sleep(1.5)
            print("DECODING PACKETS...")
            time.sleep(0.5)
            print("PARSING DATA...")
            data = getsquawk(sqwa)
            print()
            print()
            parse(data)
        elif menuchoice == "9":
            lon = input("Longitude? ")
            lat = input("Latitude? ")
            rad = input("Radius to search (mi)? ")
            print()
            print("AIMING RECEIVERS...")
            time.sleep(1)
            print("DETECTING PACKETS...")
            time.sleep(1.5)
            print("DECODING PACKETS...")
            time.sleep(0.5)
            print("PARSING DATA...")
            data = getloc(lat, lon, rad)
            print("\n")
            parse(data)
else:
    print(Fore.RED + "Failed to connect to ADS-B receivers. Check your connection.")
    sys.exit()

if user_interrupt_occured:
    sys.exit(0)
