#! /user/bin/python3

"""
Nicolas Fricker
01/10/2021

Transcript.py
"""

import re

class Transcript(str):
	"""docstring for Transcript"""
	def __new__(cls, content):
		return str.__new__(cls, content)

	def __str__(self):
		return str.__str__(self)

	def __repr__(self):
		return f"Transcript: {str.__str__(self)}"

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
		return Transcript(str.__getitem__(self, indices))

	def complement(self): 
		"""generate string of reverse complement of sequence"""
		comp = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
		return ''.join([comp[b] for b in self])

	def reverse_complement(self): 
		"""generate string of reverse complement of sequence"""
		return self.complement()[::-1]

	def find_all_primer_locations(self, primers: tuple):
		all_fwd_primers = [i.span() for i in re.finditer(primers[0], self) if i]
		all_rev_primers = [i.span() for i in re.finditer(primers[1].reverse_complement(), self) if i]

		for fwd, rev in zip(all_fwd_primers, all_rev_primers):
			yield (fwd, rev)








	# def find_all_primer_locations(self, tag, primers):
		# result = {
		# 	"tag": tag,
		# 	"fwd": [i.span() for i in re.finditer(primers[0], self) if i],
		# 	"rev": [i.span() for i in re.finditer(primers[1].reverse_complement(), self) if i],
		# 	"len": 0,
		# 	"notes": ""
		# }
		
		# if len(result["rev"]) & len(result["fwd"]):
		# 	if result["fwd"][0][0] > result["rev"][0][1]:
		# 		result["len"] = result["fwd"][0][0] - result["rev"][0][1]
		# 		result["notes"] = f"inverted: fwd > rev"
		# 	else:
		# 		result["len"] = result["rev"][0][1] - result["fwd"][0][0]

		# yield result


