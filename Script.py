import requests
import re
import os
import tkinter as tk

def get_video_info():
    link = entry.get()

    url = "https://tiktok-video-no-watermark2.p.rapidapi.com/"
    querystring = {"url": link,"hd":"0"}
    headers = {
        "X-RapidAPI-Key": "API key",
        "X-RapidAPI-Host": "tiktok-video-no-watermark2.p.rapidapi.com"
    }

    info = requests.request("GET", url, headers=headers, params=querystring)

    print(info.text)

    regex = r'"title":"(.*?)"'
    match = re.search(regex, info.text)

    if match:
        title = match.group(1)
        print(title)
    else:
        print("Title not found.")
    
    def get_video_link():
        url = "https://tiktok82.p.rapidapi.com/getDownloadVideoWithoutWatermark"

        querystring = {"video_url": link}

        headers = {
            "X-RapidAPI-Key": "API key",
            "X-RapidAPI-Host": "tiktok82.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        print(response.text)

        regex = r'"video_url":"(.*?)"'
        match = re.search(regex, response.text)

        if match:
            video_link = match.group(1)
            print(video_link)
        else:
            print("Video URL not found.")
            return

        video_mp4 = requests.get(video_link)

        if video_mp4.status_code == 200:
            with open(f'{title}.mp4', 'wb') as f:
                f.write(video_mp4.content)
            print("Video downloaded successfully!")
        else:
            print("Failed to download video.")

        old_filename = f'{title}.mp4'
        new_filename = f"{title}.mp4"

        try:
            os.rename(old_filename, new_filename)
            print("File renamed")
        except OSError:
            print("Failed to rename")

    get_video_link()


root = tk.Tk()
root.title("TikTok Video Downloader")

input_frame = tk.Frame(root)
input_frame.pack(side=tk.TOP, pady=10)

url_label = tk.Label(input_frame, text="Enter TikTok video URL:")
url_label.pack(side=tk.LEFT)

entry = tk.Entry(input_frame)
entry.pack(side=tk.LEFT)

download_button = tk.Button(root, text="Download", command=get_video_info)
download_button.pack(pady=10)

status_label = tk.Label(root, text="")
status_label.pack()

root.mainloop()
