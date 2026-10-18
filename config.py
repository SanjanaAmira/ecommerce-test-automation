
import os
from dotenv import load_dotenv

load_dotenv()

TEST_EMAIL = os.getenv("TEST_EMAIL")
TEST_PASSWORD = os.getenv("TEST_PASSWORD")

BASE_URL = "https://automationexercise.com"
