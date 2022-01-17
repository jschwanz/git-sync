#!/usr/local/bin/python3.9
from pathlib import Path
from git import Repo

def get_git_folders(base_path: str="~/src") -> list[str]:
    p = Path(base_path).glob('*')
    paths = [x for x in p if x.is_dir()]
    return paths

def pull_repos():
    paths = get_git_folders()
    #print(paths)
    for path in paths:
        try:
            repo = Repo(path=str(path))
            if str(repo.active_branch) in ["master", "main"] and not repo.is_dirty():
                print("Pulling the latest for", str(path))
                repo.remote().pull(verbose=True)
                repo.remote().fetch(prune=True, verbose=True)
            elif str(repo.active_branch) not in ["master", "main"]:
                print("Repo not on the main branch, skipping", str(path))
            elif repo.is_dirty():
                print("Repo", str(path), "is dirty, you need to fix that")
            else:
                print("active branch is", repo.active_branch)
        except:
            print("not a repo")

pull_repos()
