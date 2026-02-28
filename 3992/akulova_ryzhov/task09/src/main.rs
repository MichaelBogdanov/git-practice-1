/// # Задание 9
/// 
/// Реализовать RLE-сжатие
/// 
/// Пример:
/// 
/// `AAABBBCCDAA → A3B3C2D1A2`
/// 
/// Требования
/// - Реализовать также декодирование
/// - Поддержка любых символов
fn main() {
    let test_string = String::from("AAAAAAAAAAAAAAAACCCCCCCCCBBB");

    println!("{}", decode(encode(test_string)));

    println!("{}", decode("A12B3".to_string()));
}

fn encode(iterable: String) -> String {
    
    if iterable.is_empty() {
        return iterable
    }
    
    let mut count = 0;
    let mut prev = iterable.chars().next().expect("checked non-empty string above");
    let mut result = String::new();
    
    for c in iterable.chars() {
        if c == prev {
            count += 1;
        } else {
            result.push_str(&format!("{}{}", prev, count));
            prev = c;
            count = 1;
        }
    }
    result.push_str(&format!("{}{}", prev, count));
    result
}



fn decode(iterable: String) -> String {
    let mut current_number = String::new();
    let mut result = String::new();

    let mut current_char: Option<char> = None;

    for c in iterable.chars() {
        if c.is_ascii_digit() {
            current_number.push(c);
        } else {
            if let Some(prev) = current_char {
                if current_number.is_empty() {
                    panic!("Invalid format: missing count for '{prev}'");
                }
                let count = current_number.parse::<usize>().expect("Parse error");
                for _ in 0..count {
                    result.push(prev);
                }
                current_number.clear();
            } else {
                current_number.clear();
            }

            current_char = Some(c);
        }
    }

    if let Some(prev) = current_char {
        if current_number.is_empty() {
            panic!("Invalid format: missing count for last symbol '{prev}'");
        }
        let count = current_number.parse::<usize>().expect("Parse error");
        for _ in 0..count {
            result.push(prev);
        }
    } else {
        if !current_number.is_empty() {
            panic!("Invalid format: has digits but no symbol");
        }
    }

    result
}
