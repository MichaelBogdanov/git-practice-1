use std::fs;

/// # Задание 3
/// 
/// Перевернуть порядок слов в тексте
/// 
/// Требования:
/// - Считать файл
/// - Сохранить слова как блоки
/// - Удалить лишние пробелы и оставить между словами ровно один
fn main() {
    let content = fs::read_to_string("words.txt").expect("Не удалось прочитать файл");

    println!("{}", content);

    let lines = content
        .split_whitespace()
        .rev()
        .collect::<Vec<&str>>()
        .join(" ");
        
    
    println!("{:?}", lines);


}