# SCRAPING
MIN_PAGE_NUMBER = 20
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
SPAN_MIN_LENGTH = 100
CONTENT_MIN_LIMIT = 3000
CONTENT_MAX_LIMIT = 50000
TOTAL_CONTENT_MAX_LIMIT = 250000
DISALLOWED_TOKENS = [
    '//', '<<', '>>', '\\\\', '@'
]
FILLER_TOKENS = [
    u"\n", u"\t", u"\r", u"\"", '  ', '\\"',
    '+', '<', '[', '>', ']', '&', '—', '}', '{', '|', '‘', '=', '~', '(', '/', '~', ')', '..', '@', '#', '$', '*', ',,',
    '--', '...', ';', ':', '^', '//', '\\'
]

# RATING
DESIRED_DOMAINS = [
    'org', 'int', 'edu', 'gov', 'mil', 'eu', 'us', 'wiki', 'review'
]
AVERAGE_DOMAINS = [
    'com', 'net', 'ai', 'au', 'ca', 'academy', 'cern', 'clinic', 'codes', 'health',
    'management', 'media', 'mobi', 'tech', 'technology', 'study', 'co'
]
DISALLOWED_DOMAINS = [
    'pl', 'it', 'de'
]
