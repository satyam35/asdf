from github import Github

# using username and password
g = Github("user", "password")

# new_repo = g.get_user().create_repo("name", "description")
# new_repo.create_file("file name", "commit", "text")
# for repo in g.get_user().get_repos():
#     print(repo.name)
#     # print(repo.path)
#     repo.edit(has_wiki=False)
    # to see all the available attributes and methods
    # print(dir(repo))
# user = g.get_user("ProgrammingWithMA")
# print(user.login)
# for repo in user.get_repos():
#     print(repo.name)
repo = g.get_repo("CodesWithNaitik/codeswithnaitik.github.io")
# repo = g.get_repo("ProgrammingWithMA/ProgrammingWithMA.github.io")
# print(repo.name)
# programmingwithma.github.io
contents = repo.get_contents("")
# for content_file in contents:
#     print(content_file)
while contents:
     file_content = contents.pop(0)
     if file_content.type == "dir":
         contents.extend(repo.get_contents(file_content.path))
     else:
        print(file_content)
# repositories = g.search_repositories(query='language:python')
# for repo in repositories:
#      print(repo)
