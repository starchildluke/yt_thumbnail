import streamlit as st
import regex as re
import requests
import argparse
import webbrowser

# Create CL argument for URLs
parser = argparse.ArgumentParser(description=None)
parser.add_argument("-u", "--url", type=str)
args = parser.parse_args()
url = args.url
cleaned_url = url.replace("\\", "")

def extract_video_id(url):
    # Regular expression pattern to match the video ID
    pattern = r"(?<=youtu.be/|watch\?v=|/videos/|embed\/|youtu.be\/|v=|\?v=|\&v=|\\embed\/)[^#\&\?\n]*"

    # Find all matches of the pattern in the URL
    matches = re.findall(pattern, url)

    if len(matches) > 0:
        return matches[0]

    return "Nothing found, try again."

video_id = extract_video_id(cleaned_url)

thumb = 'https://img.youtube.com/vi/' + video_id + '/maxresdefault.jpg'
thumb_hq = 'https://img.youtube.com/vi/' + video_id + '/hqdefault.jpg'

if requests.get(thumb).status_code == 200:
    webbrowser.open(thumb)
else:
    webbrowser.open(thumb_hq)
