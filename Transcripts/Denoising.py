import sys
import shutil
import os
import datetime
import yt_dlp
import json
import argparse
from pathlib import Path
import pandas as pd

global dict_output
global test_path
global ACTOR_NAME
# test_path = "_test"
test_path = ""
dict_output = []
# All the urls to be downloaded are saved in All_video_links.txt
# If the urls are already downloaded, it ignores to re-download.
URLS = open("All_video_links.txt").readlines()


def read_json(file_name):
    f = open(file_name, 'r')
    data = json.load(f)
    return data


def build_dict(temp_dict):
    id_unique = []
    new_dict = {}
    # Appending all Ids into id_unique, to find max of ids.
    for data in dict_output:
        for key, value in data.items():
            id_unique.append(int(key))

    # If JSON file is empty, manually create id = 0.
    if len(id_unique) == 0:
        id_unique.append(0)
    new_dict[int(max(id_unique) + 1)] = temp_dict
    # Appending all the data to dict_output
    dict_output.append(new_dict)


# Writing dict objects to JSON.
def write_to_json(dict_out):
    json_object = json.dumps(dict_out, indent=4, ensure_ascii=False)
    with open(f"{Path(__file__).resolve().parent}/json/{ACTOR_NAME}/videos_metadata.json", "w+",
              encoding='utf-8') as jsonoutfile:
        jsonoutfile.write(json_object)
        jsonoutfile.write("\n")


# After downloading the videos, This def triggers.
# All the metadata available, formed as dict.
def postprocess_hook(d):
    if d['status'] == "finished":
        dictionary = {
            "url": d['info_dict']['webpage_url'],
            "fulltitle": d['info_dict']['fulltitle'],
            "filepath": d['filename'],
            "duration": d['info_dict']['duration_string'],
            "format": d['info_dict']['format'],
            "file_code": d['info_dict']['epoch'],
            "audio_ext": d['info_dict']['ext'],
            "Video_upload_date": d['info_dict']['upload_date'],
            "display_id": d['info_dict']['display_id'],
            "Sample_rate": d['info_dict']['asr'],
            "Downloaded": {
                "date": datetime.datetime.now().strftime("%d-%m-%y"),
                "time": datetime.datetime.now().strftime("%H:%M:%S")
            },
            "DownloadedBy": 'Vamsi',
            "Enhanced": False,
            "Assignedto": False,
            "aupfilename": False,
            "clips": False,
            "totalclips": False,
        }
        # This builds a dictionary
        build_dict(dictionary)
    elif d['status'] == 'error':
        print(f'------------> {d}')


# Define ytdlp options here.
def youtube_options():
    ydl_opts = {
        'sleep_interval': 5,
        'ignoreerrors': 'only_download',
        'retries': 200,
        'encoding': 'utf-8',
        'format': '140',
        'paths': {'home': f'{Path(Path(__file__).resolve().parent, "youtube_downloads_stereo_original", ACTOR_NAME)}'},
        'outtmpl': '%(epoch)s_%(title)s_%(id)s.%(ext)s',
        # archive.txt saves all the youtube urls downloaded till date.
        'download_archive': 'archive.txt',
        'quiet': True,
        'noplaylist': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
            'preferredquality': '320',
        }],
        'progress_hooks': [postprocess_hook]
    }
    return ydl_opts


ACTOR_NAME = 'Harish Rao'
Path(Path(__file__).resolve().parent, 'youtube_downloads_stereo_original', ACTOR_NAME).mkdir(exist_ok=True,
                                                                                             parents=True)
Path(Path(__file__).resolve().parent, 'json', ACTOR_NAME).mkdir(parents=True, exist_ok=True)
# Initially read Json, to get max of Ids.
try:
    dict_output = read_json(f"{Path(__file__).resolve().parent}/json/{ACTOR_NAME}/videos_metadata.json")
except Exception as E:
    print("\nException: ", E)

with yt_dlp.YoutubeDL(youtube_options()) as ydl:
    ydl.download(URLS)

write_to_json(dict_output)
