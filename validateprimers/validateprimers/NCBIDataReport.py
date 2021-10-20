#! /user/bin/python3

"""
Nicolas Fricker
01/10/2021

NCBIDataReport.py
"""

import json
import sys

from pprint import pprint

from ncbi.datasets.openapi 				import ApiClient as DatasetsApiClient
from ncbi.datasets.openapi 				import ApiException as DatasetsApiException
from ncbi.datasets.openapi.api.gene_api import GeneApi as DatasetsGeneApi
from ncbi.datasets.openapi.models 		import V1GeneMatch

class NCBIDataReport(object):
	"""docstring for NCBIDataReport"""
	def __init__(self, taxon: str = "human"):
		super(NCBIDataReport, self).__init__()
		self.taxon = taxon
		
	def open(self, filename):
		"""Open file"""
		if filename == "":
			print(f"Input NCBI Data Report Filename: ")
			# \n for unix (mac & linux) and \r\n for windows
			filename = sys.stdin.readline().strip("\n")

		return open(filename)

	def read(self, filename: str):
		"""Parse File"""
		with self.open(filename) as openfile:
			data = json.load(openfile)

		return data

	def fetch(self, symbols: V1GeneMatch):
		gene_symbols: List[str] = symbols
		results = []

		with DatasetsApiClient() as api_client:
			gene_api = DatasetsGeneApi(api_client)
			try:
				# For a single species retrieve gene metadata using a list of gene symbols
				gene_reply = gene_api.gene_metadata_by_tax_and_symbol(gene_symbols, self.taxon)
				for gene in gene_reply.genes:
					if gene.gene:
						results.append(gene.gene.to_dict())
					# self.print_gene_information(gene)
			except DatasetsApiException as e:
				print(f'Exception when calling GeneApi: {e}\n')

		return results

	def fetchToFile(self, filename: str, symbols: V1GeneMatch, type: [str]):
		# gene_reply = gene_api.download_gene_package([351], include_annotation_type = ["FASTA_RNA"], async_req = True)
				# for gene in gene_reply.get():
				# 	print(gene)
		pass

		# for variant in data["transcripts"]:
			# pprint(variant)
			# print(variant["gene_symbol"])
			# print(self.fetch(["APP"]))
			# sys.exit()
			# print(variant["name"])
			# print(variant["length"])
			# print(variant["exons"]["accessionVersion"])
			# for exon in variant["exons"]["range"]:
			# 	print(f'{exon["begin"]}, {exon["end"]}; {exon["order"]}')




