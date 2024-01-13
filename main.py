from pytube import YouTube
from tqdm import tqdm

def download_youtube_video(video_url):
    # Create a YouTube object
    yt = YouTube(video_url)

    # Function to handle the progress bar
    def progress_function(stream, chunk, bytes_remaining):
        total_size = stream.filesize
        bytes_downloaded = total_size - bytes_remaining 
        percentage_of_completion = bytes_downloaded / total_size * 100
        pbar.update(bytes_downloaded - pbar.n)

    # Get the highest resolution video stream
    video_stream = yt.streams.get_highest_resolution()

    # Initialize the progress bar
    pbar = tqdm(total=video_stream.filesize, unit='B', unit_scale=True, desc=yt.title)

    # Download the video with the progress bar
    yt.register_on_progress_callback(progress_function)
    video_stream.download()

    pbar.close()
    print("Download complete!")


link = input("Enter the YouTube video URL: ")
download_youtube_video(link)

print("Press any key to exit...")
input()
