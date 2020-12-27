
import datetime
from libs.Google import Create_Service
from googleapiclient.http import *
from tkinter import *
from tkinter import filedialog 
#Also this file is here just to simplify my code.

def Upload_Video(Title,Description,selfDeclaredMadeForKids,filename):
    try:
        SCOPES=["https://www.googleapis.com/auth/youtube.upload"]
        API_NAME = 'youtube'
        API_VERSION = 'v3'
        youtube=Create_Service("secret_file.json",API_NAME,API_VERSION,SCOPES)
        video_properties={
            'snippet':{
                'title':Title,
                'descripition':Description
        },
            'status':{
                'privacyStatus': 'unlisted',
                'selfDeclaredMadeForKids':selfDeclaredMadeForKids
            }
        }
        mediafile=MediaFileUpload(filename)
        response_upload = youtube.videos().insert(
            part='snippet,status',
            body=video_properties,
            media_body=mediafile
        ).execute()
    except:
        print("hahaha")



