import click
import os
from github import Github
from dotenv import load_dotenv

load_dotenv()

path = os.getenv("FILEPATH")
github_token = os.getenv("GITHUB_TOKEN")

@click.command()
@click.option("-n", "--new-repo", help="create a new github repository")
def create(new_repo):
    folderName = new_repo 
    os.makedirs(path + str(folderName))
    user = Github(github_token).get_user()
    user.create_repo(folderName)
    # f strings 
    print(f"Succesfully created repository {folderName}")

if __name__ == "__main__":
    create()
