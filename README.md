# Khoj

Khoj is a typeahead autocomplete service which gives suggestions sorted in the order of their popularity. It's powered by Django python framework and MYSQL DB.

***

## How to set up:
You need to have python3.7.3 virtual environment installed on your machine.
To install python3.7.3 virtual environment follow this link:
https://help.dreamhost.com/hc/en-us/articles/115000695551-Installing-and-using-virtualenv-with-Python-3 

After installing the virtual environment, go to the project folder and type: 

1. source <virtual_env_directory> activate
2. pip install -r requirements.txt
3. create Database named khoj with Encoding and Collation as utf8mb4 and utf8mb4_general_ci respectively
4. Create tables by running migration script

        python manage.py makemigrations main
        python manage.py migrate

5. Run the server by typing

            python manage.py runserver
6. Hit the below api for setting up the necessary data

        Assuming you are running this server on port 8000, so the url would be
        http://localhost:8000/add/
7. Voila! Everything is setup, Enjoy!!

## APIs

#### Overview
```
URL: /query?term=&count=&sort=

Method: GET

Params:
    term - A string which represents the query passed by the user (Required parameter otherwise, Error code 400 if not provided)
    count - Count of results the response data should limit to
    sort - Ordering the response based on some paramenter. (Right now only ordering by popularity is supported)
```

#### Error Codes
500 - Internal server error
400 - Invalid Request
404 - Request not found

#### Rate limit
This Api is rate limited based on IP to 20 request per minute. It uses Django ratelimit for achieving this.

## Test
Test cases are located at the <project_root>/main/tests.py
Run the test using the command below.
```
python manage.py test
```

## Project Structure
The project structure is inspired by Django project structure. All of the code resides in the main folder inside the project root.
main/controller - Contains API logic.
main/data - Contains Initial location data and data for the test cases.
main/migrations - Contains DB migrations
main/models - Contains DB model
main/serializers - Contains Request serializers
main/services - Contains business logic for APIs
main/utils - Contains utility classes such as api_response, api_filters, etc.

## Optimisations
As of now this application works fast (API response time is under 50ms) , but the case won't be the same when data gets huge (say 1 million rows in DB). To optimise this and still achieve faster query then we can consider putting our data in the Elastic search.

## Caching
This application uses default local memory caching that comes with Django. This cache gives the speed advantages of in-memory caching and its per-process and thread-safe. It uses a least-recently-used (LRU) culling strategy.
We can use Memcache for better caching strategy. Its a memory based cache and we can configure RAM and can allocate a seperate daemon process to it.

## Who do I talk to? 
Tarun Chaudhary (http://curioustechie.in)
