Для начала, заходим в консоль, проходим в папку с Dockerfile и docker-compose <br/>
используем команду docker-compose build <br/>
используем команду docker-compose up (тут приложение должно полностью запуститься по адресу localhost:8000) <br/>
переходим в postman и в POST-запросе отправляем в body(form-data): key:questions_num , value:1/2/3/4 etc. на адрес localhost:8000/questions/ <br/>
