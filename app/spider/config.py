import os
from pathlib import Path
from dotenv import load_dotenv


BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv()


# TAGS
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
CONTENT_LOW_LIMIT = 400
CONTENT_HIGH_LIMIT = 10000

# FILES
DATA_FILE = 'app/common/data/data.json'
RESULT_FILE = 'app/common/data/results.csv'
RATED_DATA_FILE = 'app/common/data/rated_data.json'
