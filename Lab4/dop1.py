# Program to convert an xml
# file to json file

# import json module and xmltodict
# module provided by python
import json


# open the input xml file and read
# data in form of python dictionary
# using xmltodict module
with open("xml.xml") as xml_file:
	
	data_dict = xmltodict.parse(xml_file.read())
	xml_file.close()
	
	# generate the object using json.dumps()
	# corresponding to json data
	
	json_data = json.dumps(data_dict)
	
	# Write the json data to output
	# json file
	with open("json1.json", "w") as json_file:
		json_file.write(json_data)
		json_file.close()
