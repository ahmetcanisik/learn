use std::io::{self,Write};

fn input(msg: &str) -> String {
    let mut input = String::new();
    print!("{}", msg);
    io::stdout().flush().unwrap();
    io::stdin().read_line(&mut input).expect("Failed to read line");
    input.trim().to_string()
}

fn hello(to: &str) {
    println!("Hello, {}!", to);
}

fn main() {
    let name: String = input("Enter your name: ");
    hello(&name);

    match name.as_str() {
        "Ahmet" => println!("Your welcome Ahmet!"),
        "Mehmet" => println!("Your welcome Mehmet!"),
        _ => println!("Your welcome!"),
    }

    loop {
        // how can i convert str to i32?
        let num_str = input("Enter a number: ");
        match num_str.parse::<i32>() {
            Ok(num) => {
                println!("You entered the number: {}", num);
                break; 
            },
            Err(_) => {
                println!("That's not a valid number!");
                continue;
            }
        }
    }
}
