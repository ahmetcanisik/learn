from os import getenv
from github import Github, Auth
from base64 import b64decode
from json import loads as json_loads, dumps as json_dumps

"""
Repo URL: https://github.com/dizipaltv/api/
Add new_url in dizipal.json 
"""
def update_repo(new_url: str | None = None):
    token = getenv("GITHUB_TOKEN")
    
    if not token:
        print("Error: GITHUB_TOKEN is missing in .env file!")
        return
    
    if new_url is None:
        print("Error: new_url is missing!")
        return
        
    auth = Auth.Token(token)
    g = Github(auth=auth)
    repo = g.get_repo("dizipaltv/api")
    
    try:
        contents = repo.get_contents("dizipal.json")
        content = json_loads(b64decode(contents.content).decode("utf-8"))
        
        if content["currentSiteURL"] != new_url:
            content["currentSiteURL"] = new_url
            repo.update_file(
                contents.path,
                f"Updated currentSiteURL to {new_url} in {contents.path}",
                json_dumps(content, indent=4),
                contents.sha  # <-- Eksik olan SHA parametresini ekledik
            )
            print("✅ Updated! https://github.com/dizipaltv/api/")
    except Exception as err:
        print("❌ Something went wrong! New URL was not uploaded to GitHub!", err)
    finally:
        g.close()
    