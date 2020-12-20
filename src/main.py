from googleapiclient.discovery import build
import os
print(os.getenv("KEY"))
def main():
    SECRET_KEY = 'AIzaSyAvYTXG3zm_YOLfI1h7Xsuy2LctFVqEB-Q'
    service=build('youtube','v3',developerKey=SECRET_KEY)
    request=service.channels().list(part='statistics' ,forUsername='schafer5')
    response=request.execute()
    return response

a=main()

print(a)

