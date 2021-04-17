import os
from pathlib import Path
from dotenv import load_dotenv


BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv()


# SCRAPING
MIN_PAGE_NUMBER = 10
MAX_PAGE_NUMBER = 50
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
CONTENT_MIN_LIMIT = 500
CONTENT_MAX_LIMIT = 10000
TOTAL_CONTENT_MAX_LIMIT = 100000

# RATING

