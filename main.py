#!/usr/bin/env python3

import string 
import random
from random import randint
import argparse
import sys
import requests

print("Password Generator")

pwgenWordFile = open("rockyou.txt", "r").readlines()

pwgenWordData = pwgenWordFile.read()

pwgenWordClean = pwgenWordData.split("\n")
pwgenWordList = pwgenWordClean.pop()

pwgenWordParser = argparse.ArgumentParser (description= "Generates a secure, memorable password using the XKCD method", prog="xkcdpwgen")

## wordParser.add_argument( "-h", "--help", "show this help message and exit")
pwgenWordParser.add_argument( "-w", "--words", type=int, help= "include WORDS words in the password (default=4)")
pwgenWordParser.add_argument( "-c", "--caps", type=int, help= "capitalize the first letter of CAPS random words (default=0)")
pwgenWordParser.add_argument( "-n", "--numbers", type=int, help= "insert NUMBERS random numbers in the password (default=0)")
pwgenWordParser.add_argument( "-s", "--symbols", type=int, help= "iinsert SYMBOLS random symbols in the password (default=0)")

args = pwgenWordParser.parse_args()


## what I'm using to generate the random passwords.
pwgenNumbersList = ['0','1','2','3', '4', '5', '6', '7', '8', '9']
pwgenSymbolsList = ['$', '&', '@', '(', ')', '{', '^', '%', ':', '*']


def pwgen():
	length = int(input("pw length: "))
	random.shuffle(pwgenNumbersList)
	pwgenPassword = []
	for words in range(length):
		pwgenPassword.append(random.choice(pwgenNumbersList))

		random.shuffle(pwgenPassword)

print("".join(pwgenPassword))


def symbolgen(symbolNum):
	symbolPassword = []
	for symbols in range(0, symbolNum):
		randomSymbolIndex = random.randint(0, len(pwgenSymbolsList)-1)

pwgen()


