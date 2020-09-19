from github import Github
# using username and password
g = Github("user name", "password")
# to get the the repo
new_repo = g.get_repo("name")
# to get the file for updating
new_repo.de
content = new_repo.get_contents("path", ref="ref")
content.update_file("path", "message", "content", 
            content.sha, branch="optional")
#  to delete the file
content.delete_file("path", "message", 
        content.sha, branch="optional")

        