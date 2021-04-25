from github import InputGitAuthor
from github import Github
from src.common.config import cfg

def push(path, message, content, branch, new_file=False, append_content=False):
    github_credentials = cfg["github"]
    api_key = github_credentials['api_key']

    author = InputGitAuthor(
        "RemisHaroon",
        "remis.haroon@gmail.com"
    )

    g = Github(api_key)
    repo = g.search_repositories("tech_roastery")[0]

    if not new_file and append_content:
        file = repo.get_contents(path, ref="master")  # Get file from branch
        data = file.decoded_content.decode("utf-8")  # Get raw string data
        data += "\n " + content   # Modify/Create file
    else:
        data = content

    if branch != "master":
        source = repo.get_branch("master")
        repo.create_git_ref(ref=f"refs/heads/{branch}", sha=source.commit.sha)  # Create new branch from master
    if not new_file:  # If file already exists, update it
        contents = repo.get_contents(path, ref=branch)  # Retrieve old file to get its SHA and path
        repo.update_file(contents.path, message, data, contents.sha, branch=branch, author=author)  # Add, commit and push branch
    else:  # If file doesn't exist, create it
        repo.create_file(path, message, data, branch=branch, author=author)  # Add, commit and push branch
