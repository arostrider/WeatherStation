# TODO: add logger

import json
from datetime import datetime
from pathlib import Path

from cloud import GoogleDriveHandler
from sensor import measuring_cycle

ROOT = Path(__file__).parent
DATA = ROOT / "data"


def daily():
    today = datetime.now().date()
    daily_dir = DATA / today.strftime("%Y-%m-%d")
    daily_dir.mkdir(parents=True, exist_ok=False)
    gdrive = GoogleDriveHandler()
    gfolder = gdrive.create_folder(daily_dir.name)

    while datetime.now().date() == today:
        file_name = f"{datetime.now().time().strftime('%H-%M')}.json"
        output_path = daily_dir / file_name

        hourly_data = measuring_cycle(3600, 30)

        with open(output_path, "w", encoding="utf-8") as write_file:
            json.dump(hourly_data, write_file, indent=2)

        gdrive.upload_file(output_path, gfolder)
        print(f"Uploaded file {file_name} to {daily_dir} - ID: {gfolder}")


def main(days: int):
    for i in range(days):
        daily()


if __name__ == "__main__":
    main(days=2)
