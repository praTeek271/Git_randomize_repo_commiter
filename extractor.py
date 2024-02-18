import json

def extract(file_path):
    json_data = json.loads(open(file_path).read())
    new_data = []
    # Extracting the imports
    imports = ['name']
    for data in json_data:
        info=data.get(imports[0])
        new_data.append({"name":info})
    # Writing the extracted data to a new file
    with open("extracted_data.json", "w") as file:
        file.write(json.dumps(new_data, indent=2))
extract("repos_list.json")