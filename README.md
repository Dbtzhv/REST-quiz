1. Для начала, заходим в консоль, проходим в папку с Dockerfile и docker-compose <br/>
2. используем команду docker-compose build <br/>
3. используем команду docker-compose up (тут приложение должно полностью запуститься по адресу localhost:8000) <br/>
4.  другую вкладку консоли и пишем docker-compose exec <container> bash (После выполнения этой команды вы будете перенаправлены в интерактивную оболочку контейнера)<br/>
5. в интерактивной оболочке выполняем миграции (python manage.py migrate) <br/>
6. перезапускаем контейнер <br/>
7. переходим в postman и в POST-запросе отправляем в body(form-data): key:questions_num , value:1/2/3/4 etc. на адрес localhost:8000/questions/ <br/>
