import pygit2
repoClone = pygit2.clone_repository(url="https://github.com/satyam35/Demo.git", path="D:\github_clone")
index = repoClone.index
index.add_all()
index.write()
