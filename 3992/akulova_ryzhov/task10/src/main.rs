/// # Задание 10
/// 
/// Проверка IP-адреса
/// 
/// **Цель**: определить, является ли строка корректным IPv4 или IPv6 адресом
/// 
/// **Вывод**: IPv4, IPv6 или INVALID
/// 
/// **Бонус**: нормализовать IPv6 (убрать лишние нули)
fn main() {
    let _ip: &str = "2001:0db8:0042:0000:0000:8a2e:0370:7334";
    let ip = "::";

    if is_ipv4(ip) {
        println!("IPv4");
    } else if is_ipv6(ip) {
        println!("IPv6");
    } else {
        println!("INVALID");
    }
}

fn is_in_range_u8(s: &str) -> bool {
    match s.parse::<u8>() {
        Ok(_) => true,
        Err(_) => false
    }
}

fn is_hex_string(s: &str) -> bool {
    !s.is_empty() && s.chars().all(|c| c.is_ascii_hexdigit())
}

fn is_valid_hextet(h: &str) -> bool {
    !h.is_empty()
        && (1..=4).contains(&h.len())
        && is_hex_string(h)  
}

fn is_ipv4(s: &str) -> bool {
    let octets = s.split('.').collect::<Vec<_>>();
    
    if octets.len() != 4 {
        return false;
    }

    if octets.contains(&"") || octets.contains(&":") {
        return false;
    }


    for octet in octets {
        if octet.chars().count() > 1 && octet.starts_with("0") {
            return false;
        }

        if !is_in_range_u8(octet) {
            return false;
        }
    }

    true
}

fn is_ipv6(s: &str) -> bool {
    if s.contains('.') || s.contains(":::") {
        return false;
    }

    if s.contains("::") {
        let parts = s.split("::").collect::<Vec<&str>>();
        if parts.len() != 2 {
            return false;
        } else {
            let (left, right) = (parts[0], parts[1]);
            
             let left_parts = 
                if left.is_empty() { vec![] }
                else { left.split(':').collect::<Vec<_>>() };
            
            let right_parts = 
                if right.is_empty() { vec![] }
                else { right.split(':').collect::<Vec<_>>() };
            
            for i in &left_parts {
                if !is_valid_hextet(i) {
                    return false;
                }
            }

            for i in &right_parts {
                if !is_valid_hextet(i) {
                    return false;
                }
            }

            if left_parts.len() + right_parts.len() >= 8 {
                return false;
            }

        }
    } else {
        
        let hextets = s.split(':').collect::<Vec<_>>();
    
        if hextets.len() != 8 {
            return false;
        }
    
        if hextets.contains(&"") {
            return false;
        }
    
        for hextet in hextets {
            if !(1..=4).contains(&hextet.len()) {
                return false;
            }
        
            if !is_hex_string(hextet) {
                return false;
            }
        }
    }    
    true
}

/// Бонусное задание не доделал
fn _normalize_ipv6(_s: &str) -> &str {
    // let lowercase = s.to_lowercase();
    ""
}