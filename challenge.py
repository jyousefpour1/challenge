#!/usr/bin/env python3

'''

 This script prompts a user for temperature conversion
 and also prompts a user for volume conversion
 V.1.0

'''

import sys

def main():
    """Ask user if they want to convert temperature or volume"""
    temporvol = input("Do you want to convert temperature or volume? ")
    if temporvol == "temperature":
        temperature()
    elif temporvol == "volume":
        volume()
    else:
        print("invalid")
        sys.exit(1)


def temperature():
    """convert temperature"""
    temp_list = [
        "celsius",
        "fahrenheit",
        "kelvin",
        "rankine"
    ]

    tempinput = input("What is the temperature type "
                      "that you trying to convert from (celsius,fahrenheit,kelvin or rankine) ? ")

    if tempinput in temp_list:
        try:
            value = int(input("What is the numerical value? "))
        except:
            print("invalid")
            sys.exit(1)
        if tempinput == "celsius":
            kelvin = (value + 273)
        elif tempinput == "fahrenheit":
            kelvin = ((5/9) * (value - 32) + 273)
        elif tempinput == "kelvin":
            kelvin = value
        elif tempinput == "rankine":
            kelvin = (value * (5/9))
    else:
        print("invalid")
        sys.exit()

    tempto = input("What temperature type would you like to convert to? ").lower()

    tmp = input("What value did the student provide? ")
    if not tmp.isdigit():
        print("invalid")
        sys.exit(1)

    givenvalue = int(tmp)

    if tempto in temp_list:
        if tempto == "celsius":
            tempresult = (kelvin - 273)
        elif tempto == "fahrenheit":
            tempresult = (1.8 * (kelvin - 273) + 32)
        elif tempto == "kelvin":
            tempresult = kelvin
        elif tempto == "rankine":
            tempresult = (kelvin * (9/5))

    else:
        print("invalid")
        sys.exit()

    if round(tempresult, 1) == round(givenvalue, 1):
        print("correct")

    else:
        print("incorrect", "correct answer is", round(tempresult, 1))


def volume():
    """convert volume"""
    vol_list = [
        "liters",
        "tablespoons",
        "cubic-inches",
        "cups",
        "cubic-feet",
        "gallons"
    ]

    volinput = input("What is the volume type "
                     "you are trying to convert from? (liters, tablespoons, "
                     "cubic-inches, cups, cubic-feet, gallons) ")

    if volinput in vol_list:
        try:
            value = int(input("What is the numerical value? "))
        except:
            print("invalid")
            sys.exit()
        if volinput == "liters":
            liters = value
        elif volinput == "gallons":
            liters = (value * 3.78541)
        elif volinput == "tablespoons":
            liters = (value * 0.0147868)
        elif volinput == "cubic-inches":
            liters = (value * 0.0163871)
        elif volinput == "cups":
            liters = (value * 0.236588)
        elif volinput == "cubic-feet":
            liters = (value * 28.3168)
    else:
        print("invalid")
        sys.exit(1)

    volto = input("What is the target volume you like to convert to? "
                  "(liters, tablespoons, cubic-inches, cups, cubic-feet or gallons) ")

    vol = input("What volume value did the student provide? ")

    try:
        givenvol = float(vol)
    except ValueError:
        print("invalid")


    if volto in vol_list:
        if volto == "liters":
            volresult = liters
        elif volto == "gallons":
            volresult = (liters * 0.264172)
        elif volto == "tablespoons":
            volresult = (liters * 67.628)
        elif volto == "cubic-inches":
            volresult = (liters * 61.0237)
        elif volto == "cups":
            volresult = (liters * 4.22675)
        elif volto == "cubic-feet":
            volresult = (liters * 0.0353147)

    else:
        print("invalid")
        sys.exit()
    if round(volresult, 1) == round(givenvol, 1):
        print("correct")
    else:
        print("incorrect", "correct answer is", round(volresult, 1))

if __name__ == '__main__':
    main()
