# Metabook төслийн REST API

# Төслийн файлуудыг өөрийн локал орчинд суулгахдаа дараах алхамуудыг дагаарай
[] git pull origin master
[] docker-compose run web django-admin startproject metabookcompany .
[] Хэрэв linux үйлдлийн систем хэрэглэж байгаа бол sudo chown -R $USER:$USER .
[] metabookcompany/settings.py дээр DATABASE хэсэг дээр дараах тохиргоог хийнэ
```
# settings.py
   
import os
   
[...]
   
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_NAME'),
        'USER': os.environ.get('POSTGRES_USER'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
        'HOST': 'db',
        'PORT': 5432,
    }
}
```
[] docker compose up коммандыг бичсэнээр 8000 порт дээр project маань асна