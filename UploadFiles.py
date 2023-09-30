import dropbox
import os
from dropbox.files import WriteMode

class TransferData:
    def __init__(self, accessToken):
        self.accessToken = accessToken
    def uploadFiles(self, file_from, files_to):
        db = dropbox.Dropbox(self.accessToken)
        for root, dirs, files in os.walk(file_from):
            for i in files:
                local_path = os.path.join(root, i)
                realtive_path = os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join(files_to, realtive_path)
                with open(local_path, 'rb') as f:
                    db.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))
def main():
    access_token = "sl.BnCkCiD7QiV-Ol0Qg0GDSnJw_TxYprLjBodCxXiSWnEa0wEV5Q4xD-o83gsAi_D_7p2N_y7R9DoRS30z8q5gWpXCwqPAMDzZC-NIUd28UlMFvPbKpIkH9h1El_0z_A8kBpkdlvP4ulyI"
    file_from = input("Enter the path of the file you want to upload")
    file_to = input("What is the dropbox folder to upload the files")
    data = TransferData(access_token)
    data.uploadFiles(file_from, file_to)

main()
