from pathlib import Path

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


class GoogleDriveHandler:
    GDRIVE_FOLDER = "1_WTsl1ROkALwUTm2i82yh6rQRiJLK789"

    def __init__(self):
        self.auth = GoogleAuth()
        self.drive = GoogleDrive(self.auth)

    def create_folder(self, folder_name: str) -> str:
        folder = self.drive.CreateFile({"title": folder_name,
                                        "mimeType": "application/vnd.google-apps.folder",
                                        "parents": [{"id": self.GDRIVE_FOLDER}]})
        folder.Upload()
        return folder["id"]

    def upload_file(self, file_path: Path, target_folder: str):
        gfile = self.drive.CreateFile({"parents": [{"id": target_folder}]})
        gfile.SetContentFile(file_path)
        gfile["title"] = file_path.__str__().split("/")[-1]
        gfile.Upload()


if __name__ == "__main__":
    gd = GoogleDriveHandler()
    new_folder = gd.create_folder("Testing")
    print("Test folder created")
    gd.upload_file(Path(__file__).parent / "test" / "upload_test.txt", new_folder)
    print("Test file uploaded")
