# Google Sheets Data Downloader

## Description

This Python script allows you to download files from a Google Sheet that contains Google Drive links. It utilizes the Google Sheets API and Google Drive direct download links to retrieve files and save them to your local machine.

## Prerequisites

Before using this script, ensure you have the following files in your project directory:

- **`your_script_name.py`**: Your Python script containing the provided code.

- **`.env`**: Create a `.env` file in the same directory as your script and add the following line to it:


Replace `<your_google_sheet_url>` with the actual URL of your Google Sheet.

- **`credentials.json`**: Google Service Account credentials JSON file with the necessary permissions to access your Google Sheets and Google Drive.

- **`downloaded_ids.json`**: A JSON file that keeps track of downloaded file IDs.

## Usage

1. **Set Up Environment Variables**:

Make sure the `.env` file contains your Google Sheet URL as described above.

2. **Run the Script**:

Execute the script using the following command:

```bash
python your_script_name.py

You can copy the above content and paste it into your README file, and make sure to replace `your_script_name.py` with the actual name of your Python script, and add the required files in your project directory as mentioned in the "Prerequisites" section.
