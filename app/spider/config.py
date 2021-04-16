import os
from pathlib import Path
from dotenv import load_dotenv


BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv()


# SCRAPING
TAG_CONTENT = 'text()'
XPATH_HREF_TAGS = [
    '//a/@href'
]
XPATH_MAIN_TAGS = [
    '//div/',
    '//span/',
    '//p/'
]

# PROCESSING
SPAN_MIN_LENGTH = 200
CONTENT_LOW_LIMIT = 500
CONTENT_HIGH_LIMIT = 10000
