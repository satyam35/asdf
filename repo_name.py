from github import Github
g=Github("satyam35","satyam@1234567890")
repo= g.get_repo("satyam35/double_commit")
for i in repo.get_branches():
    name=str(i)[13:(len(str(i)))-2]
    #commit = repo.get_commit(sha=name)
    #for j in (commit.files):
        #print(j)
    c=repo.get_commits(sha=name)
    print(c.totalCount)





