from json import loads
from glob import glob
from os.path import basename, splitext

root_path = "./doc/human_resource/v1/IF/get"

arg_format = "{0}: {1}|None=None"

method_format = "def {0}(\n\t{1}):\n\tendpoint_url = \"{2}\"\n{3}\n\treturn self.api_call(method=\"\", endpoint_url=endpoint_url, query=query)\n\n\n"
query_format = "\t{0}={0},\n\t"
query_req = "\tquery = dict(\n\t{0}\n\t)"

for json_path in glob(root_path+"/**.json"):
	with open(json_path, mode="r", encoding="utf-8") as schema:
		schema_json = loads(schema.read())
		method_args = ["self"]
		required_args = ["*"]
		query = []
		method = splitext(basename(json_path))[0]
		text = ""
		req = ""
		if "parameters" in schema_json:
			for param in schema_json["parameters"]:
				arg = param["name"]
				arg_type = param["schema"]["type"]
				
				if arg_type == "string":
					arg_type = "str"
				elif arg_type == "integer":
					arg_type = "int"
				elif arg_type == "boolean":
					arg_type = "bool"
				else:
					raise
				query.append(arg)
				if "required" in param:
					required_args.append(arg_format.format(arg, arg_type))
	
				elif not "required" in param:
					method_args.append(arg_format.format(arg, arg_type))
		else:
			pass
		
		for m in required_args:
			method_args.append(m)
		for q in query:
			req += query_format.format("".join(q), "".join(q))

		with open("./test_method.py", mode="a") as new_file:
			qreq = query_req.format(req)
			print(arg)
			text = method_format.format(method, ", \n\t".join(method_args), schema_json["paths"], qreq)
			print(text)
			new_file.write(text)
