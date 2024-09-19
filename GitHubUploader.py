from github import Github
from os.path import dirname, basename

from GitHubUtils import \
    getContentFile, getDirectoryContent, \
    fileChanged, fileExists, \
    createBranch, commitUpdate, commitNew

class GitHubUploader:

    def __init__(self, token, sRepo: str, *, printLogs=True):
        g = Github(token)
        self._repo = g.get_repo(sRepo)

        self._printLogs = printLogs

    def commitFiles(self, files: list[tuple]) -> list:
        lRet = []

        branch = 'script-upload'
        log = createBranch(self._repo, branch, 'main')
        if self._printLogs: print(log)
        lRet.append(log)

        afilepath = files[0][0] # assumes all files are in the same directory
        directoryContent = getDirectoryContent(self._repo, afilepath, branch)

        newFiles = [ (filepath, content)
                     for filepath, content in files
                     if not fileExists(basename(filepath), directoryContent) ]
        changedFiles = [ (filepath, content)
                         for filepath, content in files
                         if not any(filepath == fn for fn, _ in newFiles)
                         and fileChanged(content, getContentFile(self._repo, filepath, branch)) ]

        for filepath, content in newFiles:
            log = commitNew(self._repo, filepath, content, branch, checkExists=False)
            if self._printLogs: print(log)
            lRet.append(log)

        for filepath, content in changedFiles:
            log = commitUpdate(self._repo, filepath, content, branch)
            if self._printLogs: print(log)
            lRet.append(log)

        return lRet
