# TestDjangoDRF

получилось только собрать и запустить добавление категории и добавление 
продукта. Фильтрацию с помощью инструментов Django и DRF сделать не получилось. 
В предыдущих проектах я пользовался подключением к базе данных напрямую или с 
помощью Pandas и SQLAlhcemy  и фильтровал выдачу, а затем выводил с помощью 
"from django.http import JsonResponse". В данном случае нужно более подробно 
изучать документацию. Попробовал поиграться с решениями Django и DRF, но не 
получилось.

Использовал Conda / Python 3.9

После запуска проекта нужно перейти на страницу

http://127.0.0.1:8000/api/v1/foods/

на ней отобразятся все категории и продукты внутри них

создать категорию на странице

http://127.0.0.1:8000/api/v1/foods/food_category/create/

создать продукт на странице

http://127.0.0.1:8000/api/v1/foods/food/create/

