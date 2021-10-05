################################
# Program name:
#  Author: Tom Gill
#  Course: CWCT Python Essentials
#  Date: 9/24/2021
#  Assignment: P2M3A1 Stereo
#  Purpose:

# Create a StereoReceiver class. The attributes for the StereoReceiver are:
#
# Manufacturer
# Model
# Serial Number
# Band (AM/FM)
# Frequency (i.e. ‘station’)
# Volume (0-10)
# Power (i.e. On/Off)
# Two other attributes of your own choosing
# Create a constructor/initializer for the class that receives a Manufacturer, Model, and Serial Number. The
# constructor should set the attributes provided and also initialize any other attributes (e.g. power = off, volume = 0,
# band, frequency, etc.)
#
# Provide separate Accessor/Get Methods that will return Manufacturer, Model, Serial Number, Band, Frequency, Volume,
# and Power.
#
# Provide separate Mutator/Set Methods that will allow a user to turn the receiver on/off, change the volume, change
# the band, set the frequency/station, etc.
#
# Provide Accessor/Mutator methods for the attributes you provided as appropriate.
#
# Provide a string (__str__) method that will allow you to display the attributes of the receiver in a nicely formatted
# string.
#
# Create a main program that utilizes the StereoReceiver class:
#
# 1. Prompt the user for the Manufacturer, Model, Serial Number, Wattage,, and Number of Channels
# 2. Create an object for the StereoReceiver.
#    a. Catch any exceptions thrown due to invalid/omitted parameters
# 3. Using the Accessor Methods, display the Stereo Receiver’s information (manufacturer, model, etc.).
# 4. Turn on the StereoReceiver using the appropriate method.
# 5. Allow the user to change/set the band, frequency, and volume. Handle any exceptions caused by invalid data (should
#    be raised in the appropriate functions).
# 6. Allow the user to change any of the attributes you created (appropriately)
# 7. Display the StereoReceiver’s settings using the accessor methods (power, band, station, and volume)
# 8. Turn off the StereoReceiver.
# 9. Display the StereoReceiver using the string method.

#    Imports
import webbrowser, sys, keyboard, time



#   Dictionary for Channels

myChannels = {
    "p1": {
        "name" : "100.3 The Edge, New Rock for Little Rock",
        "freq" : 100.3,
        "page" : "https://www.iheart.com/live/1003-the-edge-89/?embed=true&autoplay=true",
        "band" : "FM",
        "sound": "Stereo",
        "preset" : "1"
    },
    "p2": {
        "name" : "107.7 Alice, Little Rock's #1 Hit Music Station",
        "freq" : 107.7,
        "page" : "https://www.iheart.com/live/alice-1077-5416/?embed=true&autoplay=true",
        "band" : "FM",
        "sound": "Stereo",
        "preset" : "2"
    },
    "p3": {
        "name" : "105.1 The Wolf, Little Rock Your Home for All Things Country",
        "freq" : 105.1,
        "page" : "https://www.iheart.com/live/1051-the-wolf-little-rock-93/?embed=true&autoplay=true",
        "band" : "FM",
        "sound": "Stereo",
        "preset" : "3"
    },
    "p4": {
        "name" : "102.9 Little Rock's News and talk",
        "freq" : 102.9,
        "page" : "https://www.iheart.com/live/fm-1029-5384/?embed=true&autoplay=true",
        "band" : "FM",
        "sound": "Stereo",
        "preset" : "4"
    },
    "p5": {
        "name": "98.5 Today's Hits and Yesterdays Favorites",
        "freq": 98.5,
        "page": "https://www.iheart.com/live/little-rocks-b985-fm-5431/?embed=true&autoplay=true",
        "band": "FM",
        "sound": "Stereo",
        "preset": "5"
    },
    "p6": {
        "name": "AM920 Sports talk - Little Rock's Sports Animal",
        "freq": 920,
        "page": "https://www.iheart.com/live/am-920-5385/?embed=true&autoplay=true",
        "band": "AM",
        "sound": "Mono",
        "preset": "6"
    },
    "p7": {
        "name": "Power 92 James - The People's Station Little Rock",
        "freq": 92.0,
        "page": "https://www.iheart.com/live/power-92-jams-5403/?embed=true&autoplay=true",
        "band": "FM",
        "sound": "Stereo",
        "preset": "7"
    },
    "p8": {
        "name": "Hot 94.9 All the Hits for Little Rock",
        "freq": 94.9,
        "page": "https://www.iheart.com/live/hot-949-101/?embed=true&autoplay=true",
        "band": "FM",
        "sound": "Stereo",
        "preset": "8"
    },
    "p9": {
        "name": "KSSN 96 Arkansas' Radio Station (Country)",
        "freq": 96.0,
        "page": "https://www.iheart.com/live/kssn-96-105/?embed=true&autoplay=true",
        "band": "FM",
        "sound": "Stereo",
        "preset": "9"
    },
    "static": {
        "name": "None",
        "freq": "",
        "page": "https://player.vimeo.com/video/5016361?h=ae57c70cdd/?embed=true&autoplay=true",
        "band": "",
        "sound": "Mono",
        "preset": "None"
    },
}
#   Constructor
class StereoReceiver:
    def __init__(self, manufacturer, model, serial, preset = "", band = "", freq = "", power = "off", vol = "0", sound = ""):
        self.__manufacturer = manufacturer
        self.__model = model
        self.__serial = serial
        self.band = band
        self.frequency = freq
        self.power = power
        self.volume = vol
        self.sound = sound
        self.preset = preset

#   Accessor methods
    def getMan(self):
        return self.__manufacturer
    def getMod(self):
        return self.__model
    def getSerial(self):
        return self.__serial
#   Mutator methods
    def setVol(self, volume):
        self.volume = volume
    def setPwr(self, power):
        self.power = power

    def __str__(self):
        return f"""
==============================================================================================
| {self.__model} by {self.__manufacturer}: Serial Number {self.__serial}|            A TOMOOGLE Interface    
----------------------------------------------------------------------------------------------
| Status Panel
| Power {self.power}    |   Volume {self.volume}    |   Sound: {self.sound} |   Preset: {self.preset}
|=============================================================================================="""

class Channel(StereoReceiver):
    def __init__(self, frequency, callSign, band, preset):
        self.frequency = frequency
        self.callSign = callSign
        self.band = band
        self.preset = preset
    def __str__(self):
        return f"""
| Now Playing
| {self.callSign} Preset #:{self.preset} an {self.band} band.
|---------------------------------------------------------------------------------------------"""

#           Weak way to clear the screen. Regretfully you cant really clear the screen so this will have to do.
def clear():
    print("\n" * 47)

def myExit():
    print("Thank your for listening with TOMOOGLE")
    sys.exit(0)


#           Get the station selected.
def getStation(preset):
    global counter
    preset = preset
    if counter < 1:
        myStereo = StereoReceiver(man, model, serial, myChannels[preset]["preset"], myChannels[preset]["band"],
                                  myChannels[preset]["freq"], "on", "5", myChannels[preset]["sound"])
        myStation = Channel(myChannels[preset]["freq"], myChannels[preset]["name"], myChannels[preset]["band"],
                            myChannels[preset]["preset"])
        clear()
        print(myStereo, myStation)
        webbrowser.open(myChannels[preset]["page"], new=0)
        time.sleep(1.25)
        keyboard.press_and_release("alt+tab")
        counter += 1
        print(counter)
    else:
        myStereo = StereoReceiver(man, model, serial, myChannels[preset]["preset"], myChannels[preset]["band"],
                                  myChannels[preset]["freq"], "on", "5", myChannels[preset]["sound"])
        myStation = Channel(myChannels[preset]["freq"], myChannels[preset]["name"], myChannels[preset]["band"],
                            myChannels[preset]["preset"])
        clear()
        print(myStereo, myStation)
        webbrowser.open(myChannels[preset]["page"])
        time.sleep(.5)
        keyboard.press_and_release("ctrl+w")                           # This was the how I managed to kill the playing
        time.sleep(.5)
        keyboard.press_and_release("ctrl+w")                           # station
        time.sleep(.5)
        webbrowser.open(myChannels[preset]["page"])
        time.sleep(1.25)
        keyboard.press_and_release("alt+tab")
        counter += 1

#           Validator for all integer selections
def intValidator(low, high, selection):
    try:
        selection = int(selection)
    except:
        return False
    if selection < low or selection > high:
        return False
    else:
        return selection

def setPreset():
    for p_id in myChannels:                                             # Shows available presets
        print("| Preset", p_id, myChannels[p_id]["name"])
    preset = input("Please enter a preset channel (1-9):")
    while True:                                                         # Validates preset selection
        selection = intValidator(1, 9, preset)
        if intValidator(1, 9, preset):
            break
        else:
            print("| Invalid selection, please re-enter:", end="")
            preset = input()
    preset = str(selection)
    if preset == "1":
        preset = "p1"
    elif preset == "2":
        preset = "p2"
    elif preset == "3":
        preset = "p3"
    elif preset == "4":
        preset = "p2"
    elif preset == "5":
        preset = "p5"
    elif preset == "6":
        preset = "p6"
    elif preset == "7":
        preset = "p7"
    elif preset == "8":
        preset = "p8"
    elif preset == "9":
        preset = "p9"
    else:
        preset = "static"
    getStation(preset)                                                 # plays selected preset


# Got help with this from https://stackoverflow.com/questions/22162321/search-for-a-value-in-a-nested-dictionary-python
# This method looks up the manually input frequency in the dictionary of channels. If found it returns the dictionary
# the frequency is in. If it is not, it returns None.

def getpath(nested_dict, value, prepath=()):
    for k, v in nested_dict.items():
        path = prepath + (k,)
        if v == value: # found value
            return path
        elif hasattr(v, 'items'): # v is a dict
            p = getpath(v, value, path) # recursive call
            if p is not None:
                return p

# Validate the FM frequency entered is a number in the band range
def freqValidatorFM(freq):
    try:
        freq = float(freq)
    except:
        return False
    if freq < 88.1 or freq > 108.1:
        return False
    else:
        return freq


# Gets an FM frequency from the user, validate it is a number in the FM frequency range then check the
# dictionary for an entry that matches that frequency. If there is an entry it returns nested dictionary name. If it is
# not in the dictionary, the User is prompted to input another frequency or exit.
def checkFreqFM():
    freq = input("| Enter an FM frequency to tune or press enter for main menu:")                   #100.3
    if freq == "":
        clear()
        print(myStereo)
        controls()
    else:
        while True:
            if freqValidatorFM(freq):
                freq = float(freq)
                break
            else:
                print("| Enter a valid frequency between 88.1 and 108.1")
                freq = input("Enter Frequency to tune:")
        while True:
            if getpath(myChannels, float(freq)) is not None:
                break
            else:
                getStation("static")
                time.sleep(1.5)
                keyboard.press_and_release("alt+tab")
                time.sleep(.5)
                keyboard.press_and_release("alt+tab")
                controls()

        freq = float(freq)
        fm = getpath(myChannels, freq)
        getStation(fm[0])

# Gets an AM frequency from the user, validate it is a number in the AM frequency range then check the
# dictionary for an entry that matches that frequency. If there is an entry it returns nested dictionary name. If it is
# not in the dictionary, the User is prompted to input another frequency or exit.
def checkFreqAM():
    freq = input("| Enter an AM frequency to tune or press enter for main menu:")                   #920
    if freq == "":
        clear()
        print(myStereo)
        controls()
    else:
        while True:
            if intValidator(535, 1700, freq):
                freq = int(freq)
                break
            else:
                print("| Enter a valid frequency between 535 and 1700")
                freq = input("| Enter Frequency to tune:")
        while True:
            if getpath(myChannels, int(freq)) is not None:
                break
            else:
                getStation("static")
                time.sleep(1.5)
                keyboard.press_and_release("alt+tab")
                time.sleep(.5)
                keyboard.press_and_release("alt+tab")
                controls()
        freq = int(freq)
        am = getpath(myChannels, freq)
        getStation(am[0])

def manTuning():
    clear()
    print(myStereo)
    print("|\tFM\t|\tAM\t")
    print("|---------------------------------------------------------------------------------------------")
    print("|\t1\t|\t2\t")
    print("|---------------------------------------------------------------------------------------------")
    selection = input("| Enter Selection:")
    while True:
        selection = intValidator(1, 2, selection)
        if intValidator(1, 2, selection):
            break
        else:
            print("| Invalid selection, please re-enter:", end="")
            selection = input()
    selection = str(selection)
    if selection == "1":
        checkFreqFM()
    if selection == "2":
        checkFreqAM()

def controls():
    print("| Turn off | Presets | Volume | Tune Frequency")
    print("|---------------------------------------------------------------------------------------------")
    print("|    1      |    2    |   3    |      4")
    print("|---------------------------------------------------------------------------------------------")
    selection = input("| Enter Selection:")

    while True:
        selection = intValidator(1, 4, selection)
        if intValidator(1, 4, selection):
            break
        else:
            print("| Invalid selection, please re-enter:", end="")
            selection = input()
    selection = str(selection)
    if selection == "1":                                                 #pwr off
        StereoReceiver.setPwr(myStereo, "Off")
        StereoReceiver.setVol(myStereo, "Off")
        webbrowser.open(myChannels["static"]["page"])
        time.sleep(.5)
        keyboard.press_and_release("ctrl+w")
        time.sleep(.5)
        keyboard.press_and_release("ctrl+w")
        keyboard.press_and_release("alt+tab")
        clear()
        print(myStereo)
        myExit()
    elif selection == "2":                                               # preset controls
        setPreset()
        controls()
    elif selection == "3":                                               # volume controls (sorry this doesnt really
        vol = input("| Enter volume desired (0-10):")                    # change sys volume)
        while True:
            if intValidator(1, 10, vol):
                break
            else:
                #clear()
                #print(myStereo)
                print("| Enter a valid volume (0-10):", end="")
                vol = input()
        vol = str(vol)
        StereoReceiver.setVol(myStereo, vol)
        clear()
        print(myStereo)
        controls()

    elif selection == "4":
        manTuning()
        controls()
    else:
        print ("Error 1")
    controls()


#           Initialize Stereo
man = input("Please enter your Stereo Manufacturer:")      #Kenwood
model = input("PLease enter your Model:")                  #KVR-1000"
serial = input("Please enter your Serial Number")         #89KVR9830"
counter = 0
clear()

#           Run Stereo
myStereo = StereoReceiver(man, model, serial)
print(myStereo)
input("Press Enter to power on your stereo.")
StereoReceiver.setPwr(myStereo, "On")
clear()
print(myStereo)
controls()
clear()
print(myStereo)
print("Thank your for listening with TOMOOGLE")


