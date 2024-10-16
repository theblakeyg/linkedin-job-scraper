from dotenv import load_dotenv
import os

load_dotenv()

username = os.getenv('LINKEDIN_USERNAME')
password = os.getenv('LINKEDIN_PASSWORD')