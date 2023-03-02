# fastapi-auth

This repository provides an example implementation of authentication using FastAPI. It includes a user authentication API endpoint with token-based authentication using JWT (JSON Web Tokens) and bcrypt password hashing.

## Requirements

- python 3.10

## Getting started

1. Clone repository

```
git clone https://github.com/ydaigo/fastapi-auth.git
cd fastapi-auth
```

2. Install dependencies


```
pip install -r requirements.txt
```

3. Run application



```
uvicorn main:app --reload --port 5000
```

4. visit http://127.0.0.1:5000/docs
