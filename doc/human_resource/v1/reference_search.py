from glob import glob
from json import load, dumps


with open("./document/reference.json", mode="r", encoding="utf-8") as freee_api_reference:
	reference_json = load(freee_api_reference)

for key, val in reference_json["components"]["schemas"].items():
	print(key)
