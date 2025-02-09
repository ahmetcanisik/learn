use rand::Rng;
use std::cmp::Ordering;
use std::io::{self, Write};

fn main() {
    println!("Sayıyı Tahmin Et!\n Pes etmek isterseniz 'yeter' demeniz yeterlidir.");

    let secret_number = rand::thread_rng().gen_range(1..=100);

    loop {
        io::stdout().flush().expect("Tahmin uyarısı verilirken flush işleminde bir sorun meydana geldi!");
        print!("Tahmininizi giriniz.");

        let mut guess = String::new();

        io::stdin()
            .read_line(&mut guess)
            .expect("Satır okunurken bir sorun oluştu!");

        
        if guess.trim() == "yeter" {
            println!("Gizli sayı : {secret_number}");
            break;
        }

        let guess: u32 = match guess.trim().parse() {
            Ok(num) => num,
            Err(_) => continue,
        };

        println!("Tahmininiz: {guess}");

        match guess.cmp(&secret_number) {
            Ordering::Less => println!("Çok küçük!"),
            Ordering::Greater => println!("Çok büyük!"),
            Ordering::Equal => {
                println!("Kazandınız!");
                break;
            }
        }
    }
}
