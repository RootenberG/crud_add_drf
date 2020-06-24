## crud_app_drf
# Quick start

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