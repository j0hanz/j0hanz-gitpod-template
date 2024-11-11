import os
import subprocess

def get_repo_name():
    try:
        repo_name = subprocess.check_output(["git", "rev-parse", "--show-toplevel"]).strip().decode('utf-8')
        return os.path.basename(repo_name)
    except subprocess.CalledProcessError:
        return "Unknown Repository"

def get_branch_name():
    try:
        branch_name = subprocess.check_output(["git", "rev-parse", "--abbrev-ref", "HEAD"]).strip().decode('utf-8')
        return branch_name
    except subprocess.CalledProcessError:
        return "Unknown Branch"

def get_gitpod_user():
    return os.getenv("GITPOD_GIT_USER_NAME", "Unknown User")

if __name__ == "__main__":
    repo_name = get_repo_name()
    branch_name = get_branch_name()
    gitpod_user = get_gitpod_user()

    print(f"Repository: {repo_name}")
    print(f"Branch: {branch_name}")
    print(f"Gitpod User: {gitpod_user}")