from dotenv import load_dotenv
load_dotenv()
import os
SECRET_KEY = os.getenv("KEY")
print(SECRET_KEY)
