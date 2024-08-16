#!/usr/bin/env python3

"""This program is used to support my hobby of woodworking. In order to make
circles ish from straight wood (segmented circles), we have to do some
calculations to get the angle of the cut and the inner or outer diameter
(wood thickness/width).  This porgram will take user input - desired inner
diameter, how many pieces.  It will output the angle of the cut, inner length,
and outer length to get as close to a circle as is wanted."""

import math
from fractions import Fraction

#get desired number of pieces
def getPieces():
    while True:
        #error checking...need more than 2 pieces to make the shape hollow
        try:
            numPieces = float(input("How many pieces do you want in your circle (more than 2 please)?  "))
            assert numPieces > 2
            return numPieces
        except:
            print("Need at least 3 for a hollow center!")

#get desired inner diameter
def getInnerDiameter():
    while True:
        #error checking...need something greater than 0
        try:
            innerDiameter = float(input("What would you like the inner diameter to be?  "))
            assert innerDiameter > 0
            return innerDiameter
        except:
            print("Need something greater than 0.")

#get width of the wood
def getWidth():
    while True:
        #error checking...need something greater than 0
        try:
            woodWidth = float(input("How wide is your piece of wood?  "))
            assert woodWidth > 0
            return woodWidth
        except:
            print("Need something greater than 0.")

#converts improper fraction to mixed fraction for easy reading
def fractionConverter(float):
    #breakout our numerator and denominator
    intRatio = float.as_integer_ratio()
    numer = intRatio[0]
    denom = intRatio[1]

    wholeNumber = numer // denom
    remainder = (numer % denom)/denom

    if wholeNumber == 0:
        return "{}".format(Fraction(remainder))
    elif remainder == 0:
        return "{}".format(wholeNumber)
    return "{} {}".format(wholeNumber, Fraction(remainder))

#calculate the angle required and inner length for cut
def calcCuts():
    #get the required data
    pieces = getPieces()
    diameter = getInnerDiameter()
    width = getWidth()

    innerRadius = diameter/2
    outerRadius = (diameter + width)/2
    #divide total circle degrees by number of pieces for each miterAngle
    angle = 360/pieces
    #for each angle, we have two pieces so we set the miter at half the angle
    miterAngle = angle/2

    #inner length is based off straightening the arc
    innerCirc = math.pi*diameter #2*pi*r = circumference, 2*radius = diameter
    innerLength = math.sin(math.radians(miterAngle))*innerRadius*2

    #outer length is based off straightening the arc
    outerCirc = math.pi*(diameter + width)
    outerLength = math.sin(math.radians(miterAngle))*outerRadius*2 #still need to make straight line calcs vs curve

    #rounds to the nearest 1/8 - Just easier to read and cut...fix it with glue
    innerEigth = round(innerLength*8)/8
    outerEigth = round(outerLength*8)/8

    print("Set miter angle to - {}".format(miterAngle))
    print("Inner length should be - {}".format(innerLength))
    print("Inner length rounded to nearest eigth - {}".format(fractionConverter(innerEigth)))
    #print(str(Fraction(innerEigth)))
    #print(fractionConverter(innerEigth))
    print("Outer length should be - {}".format(outerLength))
    print("Outer length rounded to nearest eigth - {}".format(fractionConverter(outerEigth)))
    #print(str(Fraction(outerEigth)))
    #print(fractionConverter(outerEigth))

calcCuts()
