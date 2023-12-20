#! /user/bin/python3

"""
Nicolas Fricker
01/10/2021

RTqPCR.py
"""

import numpy as np
import csv
import re

class RTqPCR():
	"""docstring for RTqPCR"""

	"""
		1	2	3	4	5	6	7	8	9	10	11	12
	A	A1	A2	A3	A4	A5	A6	A7	A8	A9	A10	A11	A12
	B	B1	B2	B3	B4	B5	B6	B7	B8	B9	B10	B11	B12
	C	C1	C2	C3	C4	C5	C6	C7	C8	C9	C10	C11	C12
	D	D1	D2	D3	D4	D5	D6	D7	D8	D9	D10	D11	D12
	E	E1	E2	E3	E4	E5	E6	E7	E8	E9	E10	E11	E12
	F	F1	F2	F3	F4	F5	F6	F7	F8	F9	F10	F11	F12
	G	G1	G2	G3	G4	G5	G6	G7	G8	G9	G10	G11	G12
	H	H1	H2	H3	H4	H5	H6	H7	H8	H9	H10	H11	H12
	"""
	GRID 	= {
		k : 0 for k in (r+c 
				for r in (chr(i) for i in np.arange(65, 73, 1))
				for c in (f"{i}" for i in np.arange(1, 13, 1))
		)
	}

	def __init__(self):
		pass


if __name__ == '__main__':
	print(RTqPCR.GRID)


