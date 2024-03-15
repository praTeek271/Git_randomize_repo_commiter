import time
import os
import  threading


def pull_modify_push(url, file_path, changes):
    repo_name = url.split("/")[-1].split(".")[0] or None
    
    if os.path.exists(repo_name):
        os.system("git pull origin main")
        # print("Pulled the repository")
    else:
        os.system(f"git clone {url}")
        # print("Cloned the repository")
    

    print(repo_name,"< ----  repo name")
    os.chdir(repo_name)

    # list all the files in the directory
    dir_list = os.listdir()
    if "readme.md" or "Readme.md" in dir_list:
        os.system("type nul > README.md")
        with open ("README.md", "a") as file:
            file.write(f"# {repo_name}\nThis Repo consists of the following files :")
            for dfile in dir_list:
                file.write(f"\n- {dfile}")
            file.write(f"\n\n\n\n\n- --->This is a test repository created by @prateek271\n<br><br>\n---\n<br><br>")
            file.write(f"###\tFeatures of the project:\n<br>\n")


    with open(file_path, "a") as file:
        file.write(changes)
        # print("Made changes to the file")

    # print("Commiting the changes")
    os.system("git add .")
    os.system('git commit -m "made changes"')

    print("Pushing the changes")
    os.system("git push origin main")
    time.sleep(3)
    os.chdir("..")
    print("Done")

def main(git_reo_project_name="test_webchat"):
    """
    This is the main function that performs the following tasks:
    1. Sets the URL and file path.
    2. Generates random commit changes.
    3. Starts a thread to execute the pull_modify_push function.
    """

    url = f"https://github.com/praTeek271/{git_reo_project_name}.git".format(git_reo_project_name)
    file_path = "README.md" or "readme.md"

    random_commit_changes=[
        "welcome to this repo",
        "hello world",
        "this is a test repo",
        "this is a test repo",
        " created by prateek",
        "automated commit",
        "it works like a charm",
        "i am a bot",
        "uses os module",
        "uses threading module",
        "uses time module",
        "uses random module",
        "uses git",
        "uses python",
        "uses github",
        "uses selenium",
        "uses chrome",
        "supports linux",
        "supports windows",
        "supports mac",
        "can be used for any repo",
        "can be used for any file",
        "can be used for any branch",
        "can be used for any repository",
    ]

    import random
    changes = "\n\n- "+random.choice(random_commit_changes)
    # changes = "\n\n- Hello World"
    print("Starting the process")
    t2 = threading.Thread(target=pull_modify_push, args=(url, file_path, changes))
    t2.start()
    t2.join()
    # pull_modify_push(url, file_path, changes)
# @last_commit = os.popen("git log").read().split("commit")

def cleaner(repo_name):
    """
    This function deletes the repository after the execution of the main function.
    """
    os.system(f"rmdir /s /q {repo_name}")
    import time
    from tqdm import tqdm

    for _ in tqdm(range(100),desc="Loding.....",ascii=False):
        time.sleep(0.01)
    print(f"Cleaned 🧹🧹\n",)
    print("{",time.ctime(),"}")  # print current time

def repo_selector():
    """
    This function selects the repository to work on.
    """
    import json, random

    repo_list = json.loads(open("extracted_data.json").read())
    # print(len(repo_list))
    random_repo = random.choice(repo_list)
    print(random_repo.get("name"))
    pr=random_repo.get("name")
    return pr     # returning the name of the repo 'randomly selected'


if __name__ == "__main__":
    
    no_of_times=14
    for i in range(no_of_times):
        print("Starting {i}/{no_of_times}".format(i=i+1,no_of_times=no_of_times).center(100,"-"))
        reponame=repo_selector()
        main(git_reo_project_name=reponame)
        time.sleep(5)
        cleaner(reponame)