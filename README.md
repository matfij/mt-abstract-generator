# Machine-learning-based abstracting and interpretation of search engine results
Python web or console based application for generating an abstract (answer + summary) for a user input phrase, based on the text data scraped from the web

## Console lookup

### Virtual environment
 - initialization: `py -m venv .venv`
 - starting: `.venv\Scripts\activate`
 - installing dependencies: `pip3 install -r requirements.txt`

### Docker
 - build image: `docker build .`
 - build image by compose: `docker-compose build`
 - run command: `docker-compose run api sh -c "django-admin [command]"`
 - start environment: `docker-compose up`
