# Ответы на вопросы
![image](https://user-images.githubusercontent.com/72907013/217603119-f0efaff3-f7e4-46da-b7c6-30e380187548.png)
1. Ошибка 500 означает, что проблема в коде функции данного запроса. Посмотрела бы код, запустила бы запрос на стороне сервера и посмотрела бы в консоль.
2. Проблема в том, что значения step сохраняются в одну ячейку памяти и поэтому по завершении функции create_handlers() в массиве находится 5 хэндлеров с аргументом 4. Чтобы устранить проблему, в качестве хэндлеров нужно использовать объект класса с заданными значениями callback и step.
3. В коде главной страницы гринатома 780 HTML-тегов и 482 из них содержит атрибуты.
Код ко всем заданиям (кроме 1) лежит в папке src
