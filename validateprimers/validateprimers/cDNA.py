#! /user/bin/python3

"""
Nicolas Fricker
01/10/2021

cDNA.py
"""

import re
import sys

from validateprimers.Transcript import Transcript
from validateprimers.Primer 	import Primer
from validateprimers.Protein 	import Protein

class cDNA(Transcript):
	"""docstring for cDNA"""

	dnaCodonTable = {
		'AAA': 'K',
		'AAC': 'N',
		'AAG': 'K',
		'AAT': 'N',
		'ACA': 'T',
		'ACC': 'T',
		'ACG': 'T',
		'ACT': 'T',
		'AGA': 'R',
		'AGC': 'S',
		'AGG': 'R',
		'AGT': 'S',
		'ATA': 'I',
		'ATC': 'I',
		'ATG': 'M',
		'ATT': 'I',
		'CAA': 'Q',
		'CAC': 'H',
		'CAG': 'Q',
		'CAT': 'H',
		'CCA': 'P',
		'CCC': 'P',
		'CCG': 'P',
		'CCT': 'P',
		'CGA': 'R',
		'CGC': 'R',
		'CGG': 'R',
		'CGT': 'R',
		'CTA': 'L',
		'CTC': 'L',
		'CTG': 'L',
		'CTT': 'L',
		'GAA': 'E',
		'GAC': 'D',
		'GAG': 'E',
		'GAT': 'D',
		'GCA': 'A',
		'GCC': 'A',
		'GCG': 'A',
		'GCT': 'A',
		'GGA': 'G',
		'GGC': 'G',
		'GGG': 'G',
		'GGT': 'G',
		'GTA': 'V',
		'GTC': 'V',
		'GTG': 'V',
		'GTT': 'V',
		'TAA': '-',
		'TAC': 'Y',
		'TAG': '-',
		'TAT': 'Y',
		'TCA': 'S',
		'TCC': 'S',
		'TCG': 'S',
		'TCT': 'S',
		'TGA': '-',
		'TGC': 'C',
		'TGG': 'W',
		'TGT': 'C',
		'TTA': 'L',
		'TTC': 'F',
		'TTG': 'L',
		'TTT': 'F'
	}

	def __init__(self, content):
		self._name: str = ""
		self._cds: tuple[int] = ()
		self._exons: list[tuple[int]] = []

	def __new__(cls, content):
		return str.__new__(cls, content)

	def __str__(self):
		return str.__str__(self)

	def __repr__(self):
		return f"{self._name} cDNA: \n{str.__str__(self)}"

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
		return cDNA(str.__getitem__(self, indices))

	def set_name(self, name: str):
		self._name = name

	def set_exon(self, exon: tuple[int]):
		self._exons.append(exon)

	def set_exons(self, exons: list[tuple[int]]):
		self._exons = exons

	def set_cds(self, cds: tuple[int]):
		self._cds = cds

	def get_name(self):
		return self._name

	def get_exon(self, index: int = 1):
		return self._exons[index-1]

	def get_exons(self):
		return self._exons

	def get_cds(self):
		return self._cds

	def get_cds_translation(self):
		return Protein(''.join(
			self.dnaCodonTable[self[i:i+3]]
				for i in range(0,len(self),3)
				if self[i:i+3] in self.dnaCodonTable.keys()
		))

	def get_variants(self, exons: list[int]):
		if len(exons) > len(self._exons):
			print("error exons len gt _exons")
			sys.exit()

		variant = ''.join([self[self._exons[i-1][0]:self._exons[i-1][1]] for i in exons])

		for i in exons:
			print(f"exon {i} : {self[self._exons[i-1][0]:self._exons[i-1][1]]}")
		return cDNA(variant)

	def pcr(self, primers: dict):
		print(f"fwd primer: 5'-{primers[0]}-3', length={len(primers[0])}")
		print(f"rev primer: 5'-{primers[1]}-3', length={len(primers[0])}")
		for fwd, rev in self.find_all_primer_locations(primers):
			if fwd is None:
				print(f"Failed fwd: {fwd}")
				break
			if rev is None:
				print(f"Failed rev: {rev}")
				break

			print(f"fwd location: {fwd}")
			print(f"rev location: {rev}")

			if fwd[0] < rev[1]:
				amplicon = cDNA(''.join(self[fwd[0] : rev[1]]))
			else:
				print("reversed fwd > rev")
				amplicon = cDNA(''.join(self[rev[0]: fwd[1]]))
			print(f"amplicon: {amplicon}, length={len(amplicon)}")

			yield amplicon


