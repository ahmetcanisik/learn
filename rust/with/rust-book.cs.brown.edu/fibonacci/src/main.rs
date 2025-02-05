use std::io::{self, Write};

fn fib(n: i32) {
    let mut a = 0;
    let mut b = 1;

    while (b - 1) < n {
        print!("{a} + ");
        print!("{b} = ");
        let c = a + b;
        print!("{c}\n");

        a = b;
        b = c;
    }
}

fn main() {
    println!("N'inci Fibonacci sayısını oluşturun.");

    loop {
        let mut n = String::new();
        print!("\nGireceğiniz değere kadar olan fibonacci sayıları hesaplanacak.\nLütfen bir değer giriniz (ex: 10) : ");
        io::stdout()
            .flush()
            .expect("flush işlemi esnasında bir sorun meydana geldi!");
        io::stdin()
            .read_line(&mut n)
            .expect("Kullanıcı girişinde bir sorun meydana geldi.");

        match n.trim().parse() {
            Ok(value) => fib(value),
            Err(_) => {
                println!("!!!Lütfen geçerli bir değer giriniz. (ex: 10)");
                continue;
            }
        }

        let want_quit = loop {
            let mut _exit = String::new();
            print!("Yeniden bir değer girmek istermisiniz? (Y/n) : ");
            io::stdout()
                .flush()
                .expect("flush işlemi esnasında bir sorun meydana geldi!");
            io::stdin()
                .read_line(&mut _exit)
                .expect("Kullanıcıdan değer alınırken bir sorun meydana geldi.");

            if n.trim() == "Y" || _exit.trim() == "y" || _exit.trim() == "" {
                break false;
            } else if _exit.trim() == "N" || _exit.trim() == "n" {
                break true;
            } else {
                println!("!!!Lütfen geçerli bir yanıt veriniz (Y = yes, n = no)");
                continue;
            }
        };

        if want_quit {
            break;
        }
    }
}
