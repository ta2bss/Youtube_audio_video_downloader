from pytube import YouTube
import os


def download_youtube_audio(url):
    try:
        yt = YouTube(url)

        # Select the audio stream with the highest quality
        audio_stream = yt.streams.filter(only_audio=True).order_by('abr').desc().first()

        # Download the audio stream
        output_file = audio_stream.download()

        # Save as MP3
        base, ext = os.path.splitext(output_file)
        new_file = base + '.mp3'
        os.rename(output_file, new_file)

        print(f"Downloaded audio: {new_file}")
    except Exception as e:
        print(f"An error occurred: {e}")


def download_youtube_video(url):
    try:
        yt = YouTube(url)

        # Select the highest resolution stream available
        video_stream = yt.streams.get_highest_resolution()

        # Download the video
        video_stream.download()

        print(f"Downloaded video: {yt.title}")
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    youtube_link = input("Enter the YouTube video link: ")
    download_option = input("Download as audio (mp3) or video (mp4)? Enter 'audio' or 'video': ").lower()

    if download_option == 'audio':
        download_youtube_audio(youtube_link)
    else:
        download_youtube_video(youtube_link)


if __name__ == "__main__":
    main()

