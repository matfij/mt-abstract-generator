# Machine-learning-based abstracting and interpretation of search engine results
Python web or console based application for generating an abstract (answer + summary) for a user input phrase, based on the text data scraped from the web

## Console lookup

### Virtual environment
 - initialization: `py -m venv .venv`
 - starting: `.venv\Scripts\activate`
 - 

### Docker
 - build image: `docker build . -f docker/Dockerfile`
 - build image by compose: `docker-compose build -f docker/docker-compose.yml`
 - run project: `docker-compose up -f docker/docker-compose.yml`
 