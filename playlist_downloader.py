import tkinter as tk
from tkinter import filedialog
from pytube import Playlist
from menu import *
import os

# Create the main window
window = tk.Tk()
window.title("Youtube playlist downloader")

# Create a label for the entry field
entry_label = tk.Label(window, text="Enter playlist url:")
entry_label.pack()

# Create an entry field
entry = Menu_Entry(window, width=100)
entry.pack()

# Create a button to download the url
def download():
    # Get the url from the entry field
    url = entry.get()
    # create a playlist object
    playlist = Playlist(url.strip())
    # get the destination
    destination = filedialog.askdirectory()

    counter = 1
    for video in playlist.videos:       
        # Append the url to the text area
        text_area.insert(tk.END, video.title + "\n")
        # download the highest resolution video to destination
        video = video.streams.get_highest_resolution()
        video.download(destination)
        # prefix videos in the order the appear
        old_name = destination + '/' + video.default_filename
        prefix = str(counter) + ' - '
        new_name = destination + '/' + prefix + video.default_filename
        os.rename(old_name, new_name)
        counter += 1

    text_area.insert(tk.END, "\nDone.")


download_button = tk.Button(window, text="download", command=download)
download_button.pack()

# Create a text area to display the messages
text_area = Menu_Text(window)
text_area.pack()

# Run the main loop
window.mainloop()
