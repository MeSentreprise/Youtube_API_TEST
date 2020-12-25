from googleapiclient.discovery import build

def main():
    SECRET_KEY = ''
    service=build('youtube','v3',developerKey=SECRET_KEY)
    request=service.channels().list(part='statistics' ,forUsername='schafer5')
    response=request.execute()
    return response

a=main()

print(a)

