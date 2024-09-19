from local_variables import _SECRET_PATH # ADD LOCALLY
import sys
sys.path.append(_SECRET_PATH)
from secret import _GITHUB_PAT # ADD LOCALLY

from GitHubUploader import GitHubUploader
uploader = GitHubUploader(_GITHUB_PAT, 'stmoody/api-test')

baseFilePath = 'files'



# ## # Step 1: Upload some initial files # ##

# # first create some files (that would be provided by build)
# filenames = [ 'a1.txt', 'a2.txt', 'a3.txt', 'a4.txt', 'a5.txt',
#               'b1.txt', 'b2.txt', 'b3.txt', 'b4.txt', 'b5.txt' ]

# from fileutils import generateContent
# files = [ (f'{baseFilePath}/{filename}', generateContent(20))
#           for filename in filenames ]

# logs = uploader.commit(files)
# for log in logs: print(log)



# ## # Step 2: Create an update # ##

# # create a couple new files
# filenames = [ 'c1.txt', 'c2.txt' ]

# from fileutils import generateContent
# files = [ (f'{baseFilePath}/{filename}', generateContent(20))
#           for filename in filenames ]

# # update a couple of existing files
# filenames = [ 'a1.txt', 'a2.txt', 'a3.txt', 'a4.txt', 'a5.txt' ]

# from fileutils import updatedFileContent
# files += [ (f'{baseFilePath}/{filename}',
#             updatedFileContent(f'{baseFilePath}/{filename}', 3))
#            for filename in filenames ]

# logs = uploader.commit(files)
# for log in logs: print(log)
