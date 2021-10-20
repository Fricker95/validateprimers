#! /user/bin/python3

"""
Nicolas Fricker
01/10/2021

Primer.py
"""

from validateprimers.Transcript import Transcript

class Primer(Transcript):
	"""docstring for Primer"""
	def __new__(cls, content):
		return str.__new__(cls, content)

	def __str__(self):
		return str.__str__(self)

	def __repr__(self):
		return f"Primer: {str.__str__(self)}"

	def __len__(self):
		return str.__len__(self)

	def __eq__(self, item):
		return str.__eq__(self, item)

	def __hash__(self):
		return str.__hash__(self)

	def __iter__(self):
		return str.__iter__(self)

	def __contains__(self, item):
		return str.__contains__(self, item)

	def __getitem__(self, indices):
		return Primer(str.__getitem__(self, indices))


