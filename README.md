# A personal blog, the first step in Django.


![](/screenshot.png)

If you are taking the first steps in **Django**, go step by step to the release of this project based on **[learnpy.ru](https://learnpy.ru/)*** posts.

If you're just poking with a stick, follow the instructions below.

## Instructions

```bash
~ git clone https://github.com/anton-savenchuk/personal-blog.git
~ cd personal-blog
```

In the application folder `app`, change the file `.env.example` by filling in the environment variables and rename it to `.env.dev`

```
#env/.env.dev

SECRET_KEY="copy the key from core/settings.py"
DEBUG="True"
ALLOWED_HOSTS="127.0.0.1 localhost"
INTERNAL_IPS="127.0.0.1 localhost"
CSRF_TRUSTED_ORIGINS="http://127.0.0.1 http://localhost"
POSTGRES_DB="<dbname>"
POSTGRES_USER="<dbuser>"
POSTGRES_PASSWORD="<password>"
POSTGRES_HOST="postgres"
POSTGRES_PORT=5432
```


## Build and run docker-compose

```bash
~ cd personal-blog
~ docker compose -f docker-compose.dev.yml up --build
```


## Enjoy using it...
