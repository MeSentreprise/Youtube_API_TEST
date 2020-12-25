import speech_recognition as micro
import datetime
from Google import Create_Service
from googleapiclient.http import *
import cv2
from tkinter import *
from tkinter import filedialog 

def Upload_Video(Title,Description,selfDeclaredMadeForKids):
    SCOPES=["https://www.googleapis.com/auth/youtube.upload"]
    API_NAME = 'youtube'
    API_VERSION = 'v3'
    youtube=Create_Service("client_secret.json",API_NAME,API_VERSION,SCOPES)
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
    filename = filedialog.askopenfilename(title="Select a Video File")
    mediafile=MediaFileUpload(filename)
    response_upload = youtube.videos().insert(
        part='snippet,status',
        body=video_properties,
        media_body=mediafile
    ).execute()

Upload_Video('Test',"Good Video",True)


