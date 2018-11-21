
from github import Github
import pandas as pd

user_name = input ('Enter Github Username :')
password = input ('Enter Github Password :')
repo_link = "https://github.com/kubernetes/kubernetes"
filename = input('Enter Output filename: ')

columns = ["login", "contributions", "Type", "site_admin", "name", "company",
           "blog", "location", "email", "followers", "description"]


g = Github(user_name, password)
repo = g.get_repo(input ('Enter Repo :'))


df = pd.DataFrame(columns = columns)
data = []
for contributor in repo.get_contributors():
    d = {}
    d['login'] = str(contributor.login)
    d['contributions'] = str(contributor.contributions)
    d['Type'] = str(contributor.type)
    d['site_admin'] = str(contributor.site_admin)
    d['name'] = str(contributor.name)
    d['company'] = str(contributor.company)
    d['blog'] = str(contributor.blog)
    d['location'] = str(contributor.location)
    d['email'] = str(contributor.email)
    d['followers'] = str(contributor.followers)
    d['login'] = str(contributor.login)
    d['description'] = str(contributor.bio)
    
    df = df.append(d, ignore_index=True)
    
df.to_csv(filename)                        


