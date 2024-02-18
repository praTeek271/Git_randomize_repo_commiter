import json

def extract_json(file_path):
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


def download_git_repo_info(username):
    import requests
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url)
    with open("repos_list.json", "w") as file:
        file.write(response.text)
    extract("repos_list.json")


download_git_repo_info("prateek271")   # github username of the user
