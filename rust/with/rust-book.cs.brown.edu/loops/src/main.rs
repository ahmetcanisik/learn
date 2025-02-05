fn loop_with_loop() {
    let mut count = 0;
    'counting_up: loop {
        println!("count = {count}");
        
        let mut remaining: i8 = 10;

        loop {
            println!("remaining = {remaining}");
            if remaining == 0 {
                break;
            }
            if count == 2 {
                break 'counting_up;
            }
            remaining -= 1;
        }

        count += 1;
    };
    println!("End count = {count}");
}

fn loop_with_while() {
    let mut number: i8 = 3;

    while number != 0 {
        println!("{number}");

        number -= 1;
    };

    println!("lifetime of!");

    let a: [i8; 5] = [10, 20, 30, 40, 50];
    let mut index = 0;

    println!("looping with while!");
    while index < 5 {
        println!("the value is: {}", a[index]);

        index += 1;
    }
}

fn loop_with_for() {
    let a: [i8; 5] = [10, 20, 30, 40, 50];

    println!("looping with for!");
    for element in a {
        println!("the value is {element}");
    }

    // reversed numbers in for loop
    for numb in (1..4).rev() {
        println!("{numb}!");
    }
    println!("LIFETIME OFF!!!");
}

fn main() {
    loop_with_loop();
    loop_with_while();
    loop_with_for();
}
