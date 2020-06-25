## crud_app_drf
# Quick start
## Live
https://fierce-thicket-33452.herokuapp.com/api/v1/
(does not work completely)
### setup environment:
```
virtualenv -p python3.7 .venv
source .venv/bin/activate
pip install -r requirements.txt
```
## Run app
```
python manage.py runserver
```

# Usage
```
upvote endpoint
http://localhost:8000/api/v1/posts/id/like/
```
# Test requests
```
 http -a user:password POST "http://localhost:8000/api/v1/posts/id/like/" - upvote
 http GET "http://localhost:8000/api/v1/posts/id/" - simple get request
```
## If "no such table" problem appears try:
```
python manage.py makemigrations

python manage.py migrate --run-syncdb
```