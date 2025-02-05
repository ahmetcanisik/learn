use std::io::{self, Write};

fn converter(choice: &str, mut value: f32) -> f32 {
    if choice == "fahrenheit" {
        let fahrenheit = value;
        value = (value - 32.0) / 1.8;
        println!("\n{fahrenheit} fahrenheit -> {value} santigrat eder.");
    }
    if choice == "santigrat" {
        let santigrat = value;
        value = (value + 32.0) * 1.8;
        println!("\n{santigrat} santigrat -> {value} fahrenheit eder.");
    }
    value
}

fn main() {
    loop {
        println!("Sıcaklık Türü Dönüştürücü by ahmetcanisik.\n");

        println!(
            "Lütfen hangi türde bir değer gireceğinizi seçiniz. (ex: fahrenheit ise '1' yazınız.)"
        );
        println!("[1] fahrenheit");
        println!("[2] santigrat\n");

        let type_choice = loop {
            let mut your_choice = String::new();

            print!("Seçiminiz : ");
            io::stdout().flush().expect("Flush işlemi başarısız oldu.");
            io::stdin()
                .read_line(&mut your_choice)
                .expect("Geçersiz bir seçim yaptınız.");

            let your_choice: u8 = match your_choice.trim().parse() {
                Ok(value) if value == 1 || value == 2 => value,
                Ok(_) => {
                    println!("Sadece '1' (fahrenheit) ya da '2' (santigrat) yazınız!");
                    continue;
                }
                Err(_) => {
                    println!("Lütfen Geçerli bir sayı giriniz!");
                    continue;
                }
            };

            break if your_choice == 1 {
                "fahrenheit"
            } else {
                "santigrat"
            };
        };

        println!(
            "\n{} Dönüştürücü.",
            if type_choice == "fahrenheit" {
                "Fahrenheit -> Santigrat"
            } else {
                "Santigrat -> Fahrenheit"
            }
        );

        let type_loop = loop {
            print!("Dönüştürmek istediğiniz {type_choice} değerini giriniz : ");
            let mut piece = String::new();
            io::stdout().flush().expect("Flush işlemi başarısız oldu.");
            io::stdin()
                .read_line(&mut piece)
                .expect("Geçersiz sayı girişi!");

            match piece.trim().parse() {
                Ok(value) => converter(type_choice, value),
                Err(_) => continue,
            };

            let shall_we_continue: bool = loop {
                let mut choice = String::new();

                print!("Yeni bir dönüştürme işlemine başlamak istermisiniz ? (Y/n) : ");
                io::stdout().flush().expect("kullanıcıdan devam etme bilgisi alınırken flush işlemi esnasında bir sorun meydana geldi.");
                io::stdin()
                    .read_line(&mut choice)
                    .expect("Kullanıcı yanlış bir değer girdi.");

                if choice.trim() == "Y" || choice.trim() == "y" || choice.trim() == "" {
                    break true;
                } else if choice.trim() == "N" || choice.trim() == "n" {
                    break false;
                } else {
                    println!("Ne dediğinizi anlamadık ('y'(yes) yada 'n'(no) yazınız)");
                    continue;
                }
            };

            break shall_we_continue;
        };

        if type_loop {
            continue;
        }
        break;
    }
}
