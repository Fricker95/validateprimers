#! /user/bin/python3

"""
Nicolas Fricker
01/10/2021

cDNA.py
"""

import re

from validateprimers.Transcript import Transcript

class Protein(Transcript):
	"""docstring for Protein"""

	# RNA codon table
	rnaCodonTable = {
		# U
		'UUU': 'F', 'UCU': 'S', 'UAU': 'Y', 'UGU': 'C',  # UxU
		'UUC': 'F', 'UCC': 'S', 'UAC': 'Y', 'UGC': 'C',  # UxC
		'UUA': 'L', 'UCA': 'S', 'UAA': '-', 'UGA': '-',  # UxA
		'UUG': 'L', 'UCG': 'S', 'UAG': '-', 'UGG': 'W',  # UxG
		# C
		'CUU': 'L', 'CCU': 'P', 'CAU': 'H', 'CGU': 'R',  # CxU
		'CUC': 'L', 'CCC': 'P', 'CAC': 'H', 'CGC': 'R',  # CxC
		'CUA': 'L', 'CCA': 'P', 'CAA': 'Q', 'CGA': 'R',  # CxA
		'CUG': 'L', 'CCG': 'P', 'CAG': 'Q', 'CGG': 'R',  # CxG
		# A
		'AUU': 'I', 'ACU': 'T', 'AAU': 'N', 'AGU': 'S',  # AxU
		'AUC': 'I', 'ACC': 'T', 'AAC': 'N', 'AGC': 'S',  # AxC
		'AUA': 'I', 'ACA': 'T', 'AAA': 'K', 'AGA': 'R',  # AxA
		'AUG': 'M', 'ACG': 'T', 'AAG': 'K', 'AGG': 'R',  # AxG
		# G
		'GUU': 'V', 'GCU': 'A', 'GAU': 'D', 'GGU': 'G',  # GxU
		'GUC': 'V', 'GCC': 'A', 'GAC': 'D', 'GGC': 'G',  # GxC
		'GUA': 'V', 'GCA': 'A', 'GAA': 'E', 'GGA': 'G',  # GxA
		'GUG': 'V', 'GCG': 'A', 'GAG': 'E', 'GGG': 'G'  # GxG
	}

	dnaCodonTable = {
		key.replace('U','T'):value for key, value in rnaCodonTable.items()
	}

	def __init__(self, content):
		self._exons: list[Transcript] = []
		self._cds: list[Transcript] = []
		self._primers: list[(Primer, Primer)] = []

	def __new__(cls, content):
		return str.__new__(cls, content)

	def __str__(self):
		return str.__str__(self)

	def __repr__(self):
		return f"cDNA: {str.__str__(self)}"

	def __len__(self):
		return str.__len__(self)

	def __eq__(self):
		return str.__eq__(self)

	def __iter__(self):
		return str.__iter__(self)

	def __contains__(self, item):
		return str.__contains__(self, item)

	def __getitem__(self, indices):
		return cDNA(str.__getitem__(self, indices))


