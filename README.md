# IKnowWhereYouLive
Nick Evans, Chris Liu

Python scripts to allows users to detect landmarks in an image without GPS metadata information by utilizing API’s of mulitiple AI, comparing and combining their results. 

* [Google Cloud Vision](https://console.cloud.google.com/welcome?inv=1&invt=Abh8eA&project=braided-pride-435220-m5)
* [Picarta AI](https://picarta.ai/)
* [ChatGPT](https://chatgpt.com/)

## Requirements
* Python 3.8 or higher
* Google Cloud Vision API credentials
* Required Python packages (requirements.txt)

## Installation

Clone the repository:
```bash
git clone https://github.com/Spongebanana27/IKnowWhereYouLive.git
```

Install dependencies:
```bash
pip install -r requirements.txt
```
Create an account for Picarta API
* Create API credentials (API key)
Create an account for Google API:
* Create a project in the Google Cloud Console
* Enable the Vision API and Maps API for your project
* Create API credentials (API key and service account key)
Create an account for ChatGPT

Create a config.json 
```json
{
  "google_api_key": "YOUR_GOOGLE_API_KEY_HERE",
  "google_application_credentials_file_path": "PATH_TO_YOUR_GOOGLE_APPLICATION_CREDENTIALS_FILE",
  "image_directory_path": "PATH_TO_YOUR_IMAGE_DIRECTORY",
  "picarta_api_key": "YOUR_PICARTA_API_KEY_HERE"
}
```



## Data
* https://github.com/ianare/exif-samples
* Personal photos from Nick

## Related Work 
* https://github.com/PierrunoYT/photo-location-finder

## Usage

### Picarta AI

### Google Cloud Vision

### ChatGPT
Due to ChatGPT's file upload limits, manually ask ChatGPT to predict the location of each image. 
Create a file, chatgpt.csv, to store the results.