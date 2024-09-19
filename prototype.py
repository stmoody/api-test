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
# ref = repo.create_git_ref(ref=f'refs/heads/{testBranchName}', sha=sha)
# print(f'Branch {ref.ref} created')


from fileutils import updatedFileContent, generateContent
# content = generateContent(20)
filename = 'testfile.txt'


# # commit new file
# path = f'files/{filename}'
# commitMsg = f'Add {path}'
# ret = repo.create_file(path, commitMsg, content, branch=testBranchName)
# print(f'Created commit ({ret["commit"].sha} | branch={testBranchName}) with message: {commitMsg}')


# # change existing file
# filename = filename
# path = f'files/{filename}'
# content = updatedFileContent(path, 5)
# commitMsg = f'Update {path}'
# # get file sha
# contentFile = repo.get_contents(path, ref=testBranchName)
# # print(contentFile)
# fileSha = contentFile.sha
# ret = repo.update_file(path, commitMsg, content, fileSha, branch=testBranchName)
# # print(ret)
# print(f'Created commit ({ret["commit"].sha} | branch={testBranchName}) with message: {commitMsg}')

filename1 = filename
filename2 = 'testfile2.txt'

filepath1 = f'files/{filename1}'
filepath2 = f'files/{filename2}'

from fileutils import _getLocalFileContent
filecontent1 = _getLocalFileContent(filepath1)
filecontent2 = updatedFileContent(filepath2, 5)

def commitFile(repo, filepath, content, branch):
    commitMsg = f'Blind editting {filepath}'
    # fileSha = repo.get_contents(filepath, ref=branch).sha
    contentFile = repo.get_contents(filepath, ref=branch)
    fileSha = contentFile.sha
    currentContent = contentFile.decoded_content.decode()
    if currentContent == content:
        print(f'No changes to {filepath}')
        return
    ret = repo.update_file(filepath, commitMsg, content, fileSha, branch=branch)
    print(f'Created commit ({ret["commit"].sha} | branch={branch}) with message: {commitMsg}')

# commitFile(repo, filepath1, filecontent1, testBranchName)
# commitFile(repo, filepath2, filecontent2, testBranchName)



# check if a file exists
pathToFiles = 'files'
directoryContent = repo.get_contents(pathToFiles, ref='main')
print('--- checking if files exist ---')
print(any(contentFile.name == filename1 for contentFile in directoryContent))
print(any(contentFile.name == filename2 for contentFile in directoryContent))
print(any(contentFile.name == 'fake-name.txt' for contentFile in directoryContent))
print('--- checking if file has changed ---')
existingFileContent = repo.get_contents(filepath1, ref='main').decoded_content.decode()
print(existingFileContent == filecontent1)
existingFileContent = repo.get_contents(filepath2, ref='main').decoded_content.decode()
print(existingFileContent == filecontent2)


pathToFiles = pathToFiles
lFilenames = [ filename1, filename2, 'fake-name.txt' ]

newFiles = [ filename for filename in lFilenames if not any(contentFile.name == filename for contentFile in directoryContent) ]
existingFiles = [ filename for filename in lFilenames if filename not in newFiles ]

def getfilecontent(filename):
    if filename == filename1: return filecontent1
    if filename == filename2: return filecontent2
    return None

unchangedFiles = [ filename for filename in existingFiles
                 if repo.get_contents(f'{pathToFiles}/{filename}', ref='main').decoded_content.decode() == getfilecontent(f'{filename}') ]
changedFiles = [ filename for filename in existingFiles if filename not in unchangedFiles ]

print(f'{newFiles=}')
print(f'{existingFiles=}')
print(f'{changedFiles=}')
print(f'{unchangedFiles=}')
print('-'*30)

newFiles, changedFiles, unchangedFiles = [], [], []
for filename in lFilenames:
    if not any(contentFile.name == filename for contentFile in directoryContent):
        newFiles.append(filename)
    elif repo.get_contents(f'{pathToFiles}/{filename}', ref='main').decoded_content.decode() == getfilecontent(f'{filename}'):
        unchangedFiles.append(filename)
    else: changedFiles.append(filename)

print(f'{newFiles=}\n{changedFiles=}\n{unchangedFiles=}')