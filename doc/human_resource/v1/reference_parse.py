from glob import glob
from json import load, dumps


with open("./reference.json", mode="r", encoding="utf-8") as freee_api_reference:
	reference_json = load(freee_api_reference)

for url, contents in reference_json["paths"].items():
	for method, _ in contents.items():
		api_name = contents[method]["operationId"]
		content = {"paths": url}
		content.update(contents[method])
		with open(f"./IF/{method}/{api_name}.json", mode="w", encoding="utf-8") as api_file:
			api_file.write(dumps(content, indent=4, ensure_ascii=False))
