# Задание 09 - Реализовать RLE сжатие файла

Выполнил: **Иванов Кирилл**

## Описание

Необходимо реализовать сжатие и распаковку файла с использованием алгоритма RLE (Run-Length Encoding).

## Пример использования:
```python
from solution import compress_RLE, decompress_RLE

# Сжатие файла
compress_RLE('input.txt', 'compressed.txt')

# Распаковка файла
decompress_RLE('compressed.txt', 'result.txt')
```