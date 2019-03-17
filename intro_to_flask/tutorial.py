"""
tutorial.py

Contents:
	This is a very basic flask application that will return some 
	data when the different urls are called.

Usage:
	On the command line


""" 
import json
from flask import Flask()


app = Flask(__name__)


@app.route("/")
def index():
	"""
	Return a basic message from the base url
	"""
	message = "Hello, world!"
	return message


@app.route("/states")
def state_population_list():
	"""
	This endpoint returns information about 
	state populations in 2010 and 2018. 

	Supports the following query parameter filters:
	1. year = 2010 or year = 2018
	2. population_gt = NNNN
	3. population_lt = NNNN

	Reads in the states csv file into a dictionary 
	and returns data. 
	"""
	pass


@app.route("/states/{abbr}")
def state_population_detail():
	"""
	This endpoint returns information about a 
	single state's population in 2010 and 2018.

	Reads in the states csv file into a dictionary 
	and returns data
	"""
	pass


@app.route("/frequencies")
def word_frequencies():
	"""
	This endpoint returns information about the 
	frequencies of words in a sentence 
	that is posted to the endpoint
	"""
	pass

