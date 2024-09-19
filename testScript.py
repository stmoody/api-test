from local_variables import _SECRET_PATH # ADD LOCALLY
import sys
sys.path.append(_SECRET_PATH)
from secret import _GITHUB_PAT # ADD LOCALLY

from GitHubUploader import GitHubUploader
uploader = GitHubUploader(_GITHUB_PAT, 'stmoody/api-test', printLogs=True)

baseFilePath = 'files'



# ## # Step 1: Upload some initial files # ##

# # first create some files (that would be provided by build)
# filenames = [ 'FA1.txt', 'FA2.txt', 'FA3.txt', 'FA4.txt', 'FA5.txt',
#               'FB1.txt', 'FB2.txt', 'FB3.txt', 'FB4.txt', 'FB5.txt' ]

# from fileutils import generateContent
# files = [ (f'{baseFilePath}/{filename}', generateContent(20))
#           for filename in filenames ]

# uploader.commitFiles(files)



# ## # Step 2: Create an update # ##

# # create a couple new files
# filenames = [ 'FC1.txt', 'FC2.txt' ]

# from fileutils import generateContent
# files = [ (f'{baseFilePath}/{filename}', generateContent(20))
#           for filename in filenames ]

# # update a couple of existing files
# filenames = [ 'FA1.txt', 'FA2.txt', 'FA3.txt', 'FA4.txt', 'FA5.txt' ]

# from fileutils import updatedFileContent
# files += [ (f'{baseFilePath}/{filename}',
#             updatedFileContent(f'{baseFilePath}/{filename}', 3))
#            for filename in filenames ]

# # add the non-updated files
# filenames = [ 'FB1.txt', 'FB2.txt', 'FB3.txt', 'FB4.txt', 'FB5.txt' ]

# from fileutils import _getLocalFileContent
# files += [ (f'{baseFilePath}/{filename}',
#             _getLocalFileContent(f'{baseFilePath}/{filename}'))
#            for filename in filenames ]

# uploader.commitFiles(files)
