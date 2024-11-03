# Бот для автопостинга в телеграм канале
## dev-версия
#### Установка и настройка
Скачайте код:
```sh
git clone https://github.com/elnarmen/sunna_100_bot.git
```
Установите Docker и Docker-compose.
Создайте файл .env в корневой директории со следующими настройками:
* `DEBUG`
* `SECRET_KEY`
* `TG_TOKEN=<Токен телеграм бота>`
* `CHAT_ID=<ID канала>`
* `CHAT_ID_FOR_LOGS=<Chat ID для отправки логов>`
* `POSTGRES_USER`
* `POSTGRES_PASSWORD`
* `POSTGRES_DB`;<br>

#### Запуск

Запустите <b>docker-compose</b>:
```
docker-compose -f docker-compose.dev.yml up -d --build
```

Дождитесь окончания установки и запустите миграции:
```
docker-compose -f docker-compose.dev.yml exec web python /app/sto_sunn/manage.py migrate
```

Создать супреюзера:
```
docker exec -it sto_sunn_web python /app/sto_sunn/manage.py createsuperuser
```

После создания суперюзера необходимо создать посты в админке и установить интервал между постами.

Затем можно запускать бота:
```
docker exec sto_sunn_web python /app/sto_sunn/manage.py run_bot
```

## prod-версия
Создайте файл .env в корневой директории со следующими настройками:
* `DEBUG`
* `SECRET_KEY`
* `TG_TOKEN=<Токен телеграм бота>`
* `CHAT_ID=<ID канала>`
* `CHAT_ID_FOR_LOGS=<Chat ID для отправки логов>`
* `POSTGRES_USER`
* `POSTGRES_PASSWORD`
* `POSTGRES_DB`;<br>

Запустите скрипт:
```
bash deploy.sh
```

Далее запустите команду:
```
docker exec -it sto_sunn_web sh
```

Создайте супреюзера:
```
docker exec -it sto_sunn_web python /app/sto_sunn/manage.py createsuperuser
```

После создания суперюзера необходимо создать посты в админке и установить интервал. По умолчанию установлен интервал 24 ч.

Затем можно запускать бота:
```
docker exec sto_sunn_web python /app/sto_sunn/manage.py run_bot
```
