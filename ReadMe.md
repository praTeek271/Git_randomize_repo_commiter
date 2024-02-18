# Git Committer

This is a Python script that automates the process of making commits to a Git repository. It's named `git_commiter.py`.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You need to have Python installed on your machine. You can download Python from [here](https://www.python.org/downloads/).

You also need to have Git installed. You can download Git from [here](https://git-scm.com/downloads).

### Usage

To use this script, navigate to the directory containing `git_commiter.py` in your terminal and run the following command:

```bash
python git_commiter.py
```
Follow the prompts in the terminal to make your commit.

### Contributing

If you have suggestions for how git_commiter.py could be improved, or want to report a bug, open an issue! Contributions of all kinds are welcomed!

For more, check out the Contributing Guide.

### Working of the script

The script first selects the repository from a collection of repository names stoted in a file named `repod_list.json` or `extracted_data.json` . It uses Random module to select a random repository from the list. Then it navigates to the selected repository and makes a clone of the repository. Then it navigates to the cloned repository and makes a commit to the repository. The commit message is also generated randomly and is stored in the `ReadMe.md` file of the repository. The script then pushes the commit to the repository. The script then navigates back to the original directory and deletes the cloned repository.

Makeing a commit to a repository is a very important task and should be done with caution. 
### <font color="red">**This script is only for `educational purposes` and should not be used for any malicious purposes.**</font>

### License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

License
MIT © Prateek271

