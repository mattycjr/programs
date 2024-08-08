#!/usr/bin/env python3

"""Simple functions to calculate the area of a triangle, rectangle, circle, and donut.
Can be imported in Python and called individually."""

import math

def triangle(base, height):
	return base*height/2

def rectangle(base, height):
	return base*height

def circle(radius):
	return math.pi*(radius**2)

def donut(outside_radius, inside_radius):
	return circle(outside_radius) - circle(inside_radius)
