from github import Github,Comparison

access_token ="633fbecee7611486536dcef846f5ba738e36351e"


def extract_project_commits(project_full_name):
    g=Github(access_token)
    repo=g.get_repo(project_full_name)
    for i in repo.get_branches():
        name = str(i)[13:(len(str(i))) - 2]










extract_project_commits("satyam35/double_commit")