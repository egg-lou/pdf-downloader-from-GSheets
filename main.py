import os
import gdown
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
import gspread
import json
from dotenv import load_dotenv

load_dotenv()

google_sheet_url = os.environ.get("GOOGLE_SHEET_URL")

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
credentials = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(credentials)

sheet = client.open_by_url(google_sheet_url)

worksheet = sheet.get_worksheet(0)

data = worksheet.get_all_values()

df = pd.DataFrame(data, columns=data[0])


total_count = 0
successful_count = 0
error_count = 0
skipped_count = 0

drive_link_column = 12
name_column = df.iloc[:, 3]
download_folder = 'COR'
if not os.path.exists(download_folder):
    os.makedirs(download_folder)

downloaded_ids = set()
if os.path.exists('downloaded_ids.json') and os.path.getsize('downloaded_ids.json') > 0:
    with open('downloaded_ids.json', 'r') as file:
        downloaded_ids = set(json.load(file))

for index, row in df.iterrows():
    file_url = row[drive_link_column]
    if not pd.isna(file_url) and 'drive.google.com' in file_url:
        file_id = file_url.split('=')[-1]

        if file_id in downloaded_ids:
            skipped_count += 1
            print(f"Skipped already downloaded file: {file_url}")
            continue

        direct_download_url = f'https://drive.google.com/uc?export=download&id={file_id}'
        print(f"Direct Download url: {direct_download_url}")
        name = name_column[index]
        output_file = os.path.join(download_folder, f"{name}_COR.pdf")
        
        try:
            gdown.download(direct_download_url, output_file, quiet=False)
            print(f"Downloaded: {output_file}")
            successful_count += 1
            downloaded_ids.add(file_id)
            with open('downloaded_ids.json', 'w') as file:
                json.dump(list(downloaded_ids), file)
        except Exception as e:
            print(f"Failed to download {file_url}: {e}")
            error_count += 1

        total_count += 1

with open('downloaded_ids.json', 'w') as file:
    json.dump(list(downloaded_ids), file)

print(f"Total files: {total_count}")
print(f"Successfully downloaded files: {successful_count}")
print(f"Failed downloads: {error_count}")
print(f"Skipped downloads: {skipped_count}")
