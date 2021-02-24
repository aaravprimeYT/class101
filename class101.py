import dropbox

class TransferData:
    def __init__(self,accessToken):
        self.accessToken = accessToken

    def uploadFiles(self,fileFrom,fileTo):
        dbx = dropbox.Dropbox(self.accessToken)

        with open(fileFrom,"rb") as f:
            dbx.files_upload(f.read(),fileTo)

def main():
    accessToken = "Hq6d1c1qg4wAAAAAAAAAAYKlyT3MSZBlEcwVSxr7bxh0wkWUHcWGjGsylYO4eEUk"
    transferData = TransferData(accessToken)
    
    fileFrom = input("Enter the file path to transfer: ")
    fileTo = '/test_dropbox/hello.txt'

    transferData.uploadFiles(fileFrom,fileTo)

if __name__ == '__main__':
    main()