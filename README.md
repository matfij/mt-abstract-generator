# Machine-learning-based abstracting and interpretation of search engine results
Python web (Django) or console based application for generating an abstract (answer + summary) for a user input phrase, based on the text data scraped from the web (Scrapy).

## Console lookup

### Virtual environment
 - initialization: `py -m venv .venv`
 - starting: `.venv\Scripts\activate`
 - installing dependencies: `pip3 install -r requirements.txt`

### Docker
 - build image: `docker build .`
 - build image by compose: `docker-compose build`
 - start environment: `docker-compose up`

### Django
 - run command: `docker-compose run api sh -c "django-admin [command]"`
 - migrate: `docker-compose run api sh -c "python3 manage.py makemigrations core"`
 - start local server: `py app/manage.py runserver`

## Gunicorn
 - Worker class: `gthread` 
 - Number of workers should be adjusted to the device: `(2 x $num_cores) + 1`
 