# YouTube Video Downloader

This is a simple Python script that allows you to download YouTube videos in the highest available resolution.

## How it works

The script uses the `pytube` library to handle the downloading of YouTube videos. It also uses the `tqdm` library to display a progress bar during the download.

## Usage

1. Run the script: `python main.py`
2. When prompted, enter the URL of the YouTube video you want to download.

## Code Overview

The main function `download_youtube_video(link)` takes a YouTube video URL as an argument. It creates a `YouTube` object and gets the highest resolution stream available for the video.

A progress bar is initialized with the total size of the video file. The `register_on_progress_callback` function of the `YouTube` object is used to update the progress bar during the download.

Once the download is complete, the progress bar is closed and a message is printed to the console.

## Dependencies

- pytube
- tqdm

Install them using pip:

```bash
pip install pytube tqdm
```
