from github import Github

# get a PAT for authentication
from local_variables import _SECRET_PATH # ADD LOCALLY
import sys
sys.path.append(_SECRET_PATH)
from secret import _GITHUB_PAT # ADD LOCALLY

# get repository
g = Github(_GITHUB_PAT)
sRepo = 'stmoody/api-test'
repo = g.get_repo(sRepo)

# get root commit from main
sBranch = 'main'
sha = repo.get_branch(sBranch).commit.sha
print(sha)

# try creating a branch
testBranchName = 'test-branch-stmoody'
ref = repo.create_git_ref(ref=f'refs/heads/{testBranchName}', sha=sha)
print(f'Branch {ref.ref} created')


from fileutils import updatedFileContent, generateContent
content = generateContent(20)
filename = 'testfile.txt'

# commit new file
path = f'files/{filename}'
commitMsg = f'Add {path}'
ret = repo.create_file(path, commitMsg, content, branch=testBranchName)
print(f'Created commit ({ret["commit"].sha} | branch={testBranchName}) with message: {commitMsg}')
