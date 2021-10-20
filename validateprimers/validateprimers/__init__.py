#! /user/bin/python3

"""
Nicolas Fricker
01/10/2021

__init__.py


Run: 
	pip install -e <dir path to package>

Usage:
	'''
	import validateprimers as vp

	vp.Primer()
	'''
"""

import numpy as np
import json
import csv
import re
import sys
import os

from pprint 							import pprint

from validateprimers.FASTAReader 		import FASTAReader
from validateprimers.NCBIDataReport 	import NCBIDataReport

from validateprimers.Transcript 		import Transcript
from validateprimers.Primer 			import Primer
from validateprimers.cDNA 				import cDNA

