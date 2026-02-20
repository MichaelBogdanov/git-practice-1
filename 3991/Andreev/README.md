Задача 01 - Проверка правильности скобок

Участники группы
Андреев А. С.

Описание решения
Использована событийная модель обработки символов. Каждый символ строки генерирует событие, которое обрабатывается в зависимости от типа скобки.
Очередь обработки событий реализована через стек (LIFO), что соответствует природе вложенных структур — последняя открытая скобка должна быть закрыта первой.

Как запустить
python task1.py tests/test1.txt
python task1.py tests/test2.txt
python task1.py tests/test3.txt
python task1.py tests/test4.txt
python task1.py tests/test5.txt
python task1.py tests/test6.txt
python task1.py tests/test7.txt
python task1.py tests/test8.txt
python task1.py tests/test9.txt
python task1.py tests/test10.txt