import requests

resp=requests.get("http://www.uniprot.org/uniprot/B5ZC00.fasta")

print(resp.text)