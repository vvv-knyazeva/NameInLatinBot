# NameInLatinBot
## Инструкция для работы с телеграмм-ботом

* Получить персональный токен у BotFather в telegram
* Вставить его в файлы requirements.txt и dockerfile
* В терминале VScode ввести команды: 
  - sudo docker build . 
  - sudo docker images (копируем id нужного образа)
  - sudo docker run -d -p 80:80 id нужного образа
* Проверяем запущен ли контейнер: sudo docker ps

* Чтобы остановить докер: sudo docker stop id контейнера
