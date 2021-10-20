#! /user/bin/python3

"""
Nicolas Fricker
01/10/2021

FASTAReader.py
"""

import re

from validateprimers.Transcript import Transcript

class FASTAReader(object):
	"""
	Define objects to read FastA files.

	instantiation: 
	thisReader = FastAreader ('testTiny.fa')
	usage:
	for head, seq in thisReader.readFasta():
	print (head,seq)
	"""
	def __init__(self, filename: str = ""):
		super(FASTAReader, self).__init__()
		self.filename = filename
		
	def open(self):
		"""Open file"""
		if self.filename == "":
			print(f"Input FASTA Filename: ")
			# \n for unix (mac & linux) and \r\n for windows
			self.filename = sys.stdin.readline().strip("\n")

		return open(self.filename)

	def read(self):
		"""Parse File"""
		with self.open() as openfile:
			for match in re.finditer(r">(.*)\n([ATGC\n]*)", "".join(openfile)):
				yield match.group(1), Transcript(re.sub("\n", "", match.group(2)))




