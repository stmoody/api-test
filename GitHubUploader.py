from github import Github
from os.path import dirname

from GitHubUtils import \
    getContentFile, getDirectoryContent, \
    fileChanged, fileExists, \
    createBranch, commitUpdate, commitNew

class GitHubUploader:

    def __init__(self, token, sRepo: str):
        g = Github(token)
        self._repo = g.get_repo(sRepo)

    def commitFiles(self, files: list[tuple]) -> list:
        lRet = []

        branch = 'script-upload'
        lRet.append(createBranch(self._repo, branch, 'main'))

        pathToFiles = dirname(files[0][0])
        directoryContent = getDirectoryContent(self._repo, pathToFiles, branch)

        newFiles = [ (filename, content)
                     for filename, content in files
                     if not fileExists(filename, directoryContent) ]
        changedFiles = [ (filename, content)
                         for filename, content in files
                         if filename not in newFiles
                         and fileChanged(content, getContentFile(self._repo, filename, branch)) ]

        for filename, content in newFiles:
            lRet.append(commitNew(self._repo, filename, content, branch, checkExists=False))

        for filename, content in changedFiles:
            lRet.append(commitUpdate(self._repo, filename, content, branch))

        return lRet
