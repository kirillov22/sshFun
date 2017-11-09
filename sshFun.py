#!/usr/bin/env
"""
    A selection of tools to change settings via SSH
    Author: Kirill Kirillov
    Date: November 2017
    Note use these tools at your own risk and if performing on another persons
    machine please be mindful that you may lose friends if you do this, but they
    should really be smart enough to know how to stop this from happening.
"""

import os, time, pprint, random, math

def main():
    """Main program where your fun begins"""
    isEnd = False
    commands = {
    "-help": "Shows the help. Who would have guessed",
    "-default": "resets things to their default state",
    "-gammabreathe": "Mimicks a breathing effect of the gamma values by making the screen brighter",
    "-redbreathe": "Mimicks a breathing effect of the gamma values by making the screen redder",
    "-greenbreathe": "Mimicks a breathing effect of the gamma values by making the screen greener",
    "-bluebreathe": "Mimicks a breathing effect of the gamma values by making the screen bluer",
    "-yellowbreathe": "Mimicks a breathing effect of the gamma values by making the screen yellower",
    "-darkbreathe": "Mimicks a breathing effect of the gamma values by making the screen darker",
    "-randomgamma": "Randomly changes the gamma value every second",
    "-sendmessage": "Sends the person a nice wee message of your choosing",
    "-forkbomb": "If you want to be a real asshole and just crash their computer xD"}

    while not isEnd:
        command = input("Please enter a command or type -help: ")
        command = command.strip().lower()
        if command == "-help":
            pprint.pprint(commands, width=120, indent=5)
        elif command == "-default":
            setDefault()
        elif command == "-gammabreathe":
            gammaBreathe()
        elif command == "-redbreathe":
            redBreathe()
        elif command == "-greenbreathe":
            greenBreathe()
        elif command == "-bluebreathe":
            blueBreathe()
        elif command == "-yellowbreathe":
            yellowBreathe()
        elif command == "-darkbreathe":
            darkBreathe()
        elif command == "-randomgamma":
            randomGamma()
        elif command == "-sendmessage":
            sendMessage()
        elif command == "-sillypopup":
            sillyPopUp()
        elif command == "-forkbomb":
            print("Get ready because this thot is about to be patrolled.")
            forkbomb()
        else:
            print("Command: '{}' not found.".format(command))

def setDefault():
    os.system("DISPLAY=:0 xgamma -gamma 1,1,1")


def gammaBreathe():
    sleepTime = 0.1

    while 1:
        for i in range(1, 9):
            os.system("DISPLAY=:0 xgamma -gamma {}".format(i))
            time.sleep(sleepTime)
        for i in range(9, 1, -1):
            os.system("DISPLAY=:0 xgamma -gamma {}".format(i))
            time.sleep(sleepTime)


def redBreathe():
    sleepTime = 0.1

    while 1:
        for i in range(1, 9):
            os.system("DISPLAY=:0 xgamma -rgamma {}".format(i))
            time.sleep(sleepTime)
        for i in range(9, 1, -1):
            os.system("DISPLAY=:0 xgamma -rgamma {}".format(i))
            time.sleep(sleepTime)

def greenBreathe():
    sleepTime = 0.1

    while 1:
        for i in range(1, 9):
            os.system("DISPLAY=:0 xgamma -ggamma {}".format(i))
            time.sleep(sleepTime)
        for i in range(9, 1, -1):
            os.system("DISPLAY=:0 xgamma -ggamma {}".format(i))
            time.sleep(sleepTime)


def blueBreathe():
    sleepTime = 0.1

    while 1:
        for i in range(1, 9):
            os.system("DISPLAY=:0 xgamma -bgamma {}".format(i))
            time.sleep(sleepTime)
        for i in range(9, 1, -1):
            os.system("DISPLAY=:0 xgamma -bgamma {}".format(i))
            time.sleep(sleepTime)


def yellowBreathe():
    sleepTime = 0.1

    while 1:
        for i in range(1, 9):
            os.system("DISPLAY=:0 xgamma -rgamma {}".format(i))
            os.system("DISPLAY=:0 xgamma -ggamma {}".format(i))
            time.sleep(sleepTime)
        for i in range(9, 1, -1):
            os.system("DISPLAY=:0 xgamma -rgamma {}".format(i))
            os.system("DISPLAY=:0 xgamma -ggamma {}".format(i))
            time.sleep(sleepTime)


def darkBreathe():
    sleepTime = 0.1

    while 1:
        i = 1.0
        while i > 0.1:
            os.system("DISPLAY=:0 xgamma -gamma {}".format(i))
            time.sleep(sleepTime)
            i -= 0.05
        i = 0.1
        while i < 0.9:
            os.system("DISPLAY=:0 xgamma -gamma {}".format(i))
            time.sleep(sleepTime)
            i += 0.05


def randomGamma():
    sleepTime = 0.5

    while 1:
        value = 1 + (9 - 1) * random.random()
        os.system("DISPLAY=:0 xgamma -gamma {}".format(value))
        time.sleep(sleepTime)


def sendMessage():
    message = input("Please enter a message: ")
    title = input("Give the message a title: ")
    os.system("DISPLAY=:0 zenity --error --text='{}\!' --title='{}!' --width=200 --height=200".format(message, title))


def sillyPopUp():
    number = input("How many popups are we opening? ")
    message = "Uh oh! Not another silly pop up. Angery reaccs!"
    title = "Silly pop up"

    if number.isdigit and int(number) > 0:
        number = int(number)
        for i in range(0, number):
            os.system("DISPLAY=:0 zenity --error --text='{}\!' --title='{}!' --width=200 --height=200".format(message, title))
    else:
        print("You silly goose. Enter a valid number!")


def forkbomb():
    if input("Are you sure? y/n ") == "y":
        print("THOT, BE GONE!!!!!!!!!!!")
        while(1):
            os.fork()
    else:
        print("Thanks for not being an asshole!\n -Sincerely,\n   the idiot who gives away their private SSH key")

main()
