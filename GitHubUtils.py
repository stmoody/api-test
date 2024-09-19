from os.path import dirname

def _createCommitMessage(sha: str, branch: str, commitMsg: str) -> str:
    return f'Created commit ({sha} | branch={branch}) with message: {commitMsg}'

def getDirectoryContent(repo, filepath: str, branch: str) -> list:
    return repo.get_contents(dirname(filepath), ref=branch)

def fileExists(filepath: str, directoryContent: list) -> bool:
    return any(contentFile.name == filepath for contentFile in directoryContent)

def commitUpdate(repo, filepath, content, branch, *, checkDiff=True) -> str:

    contentFile = repo.get_contents(filepath, ref=branch)
    if checkDiff and contentFile.decoded_content.decode() == content:
        return f'No changes to {filepath} detected. Skipping commit.'
    fileSha = contentFile.sha

    commitMsg = f'updating {filepath}'

    dRet = repo.update_file(filepath, commitMsg, content, fileSha, branch=branch)
    return _createCommitMessage(dRet['commit'].sha, branch, commitMsg)

def commitNew(repo, filepath, content, branch, *, checkExists) -> str:

    if checkExists:
        directoryContent = getDirectoryContent(repo, filepath, branch)
        if fileExists(filepath, directoryContent):
            return f'File {filepath} already exists. Skipping commit.'

    commitMsg = f'creating {filepath}'

    dRet = repo.create_file(filepath, commitMsg, content, branch=branch)
    return _createCommitMessage(dRet['commit'].sha, branch, commitMsg)

def createBranch(repo, branchName, baseBranch: str) -> str:
    sha = repo.get_branch(baseBranch).commit.sha

    ref = repo.create_git_ref(f'refs/heads/{branchName}', sha=sha)
    return f'Branch {ref.ref} created'
