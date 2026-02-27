def remove_duplicates_keep_order(input_file, output_file=None):
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read().strip()
        items = content.split()
        #множество для отслеживания уже встреченных элементов
        
        seen = set()
        result = []
        
        for item in items:
            if item not in seen:
                #добавление дубликатов
                seen.add(item)
                #добавление уникальных
                result.append(item)
        
        result_str = ' '.join(result)
        
        if output_file:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(result_str)
            print(f"Результат сохранен в файл: {output_file}")
        else:
            print("Результат:")
            print(result_str)
            
        return result
        
    except FileNotFoundError:
        print(f"Ошибка: Файл '{input_file}' не найден")
        return None
    except Exception as e:
        print(f"Ошибка при обработке файла: {e}")
        return None


if __name__ == "__main__":
    remove_duplicates_keep_order("C:/Users/HP/OneDrive/Документы/input.txt")
