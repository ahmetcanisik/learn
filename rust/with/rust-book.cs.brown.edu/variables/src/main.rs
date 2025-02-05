fn basic_variables() {
    let x = 5;

    let x = x + 1;
    {
        let x = x * 2;
        println!("x'in inner scope değeri\t: {x}");
    }

    println!("x'in değeri\t\t: {x}");

    let floater_x = 2.0;
    println!("your floater_x {floater_x}");

    let floater_y: f32 = 3.0;
    println!("your floater_y {floater_y}");

    let is_true = true;
    println!("is true? {is_true}");

    let is_true: bool = false;
    println!("is true bool? {is_true}");

    let character = 'Z';
    println!("{character}");

    let character: char = 'a';
    println!("{character}");

    let character = '😂';
    println!("{character}");
}

fn mathmatical() {
    // toplama (addition)
    let sum = 5 + 10;

    // çıkarma (subtraction)
    let difference = 95.4 - 4.2;

    // çarpma (multiplication)
    let product = 4 * 30;

    // bölme (division)
    let quotient = 56.7 / 32.2;
    let truncated = -5 / 3;

    // kalna (remainder)
    let ramainder = 43 % 5;

    println!("sum: {sum}, difference: {difference}, product: {product}, quotient: {quotient}, truncated: {truncated}, ramainder: {ramainder}");
}

fn tuples() {
    let tup = (500, 6.4, 1);

    let (x, y, z) = tup;
    println!("x: {x}, y: {y}, z: {z}");

    let x: (i32, f64, u8) = tup;

    let five_hundered = x.0;

    let six_point_four = x.1;

    let one = x.2;

    println!("five hundered is {five_hundered}, six point four is {six_point_four}, one is {one}");

    let mut x: (i32, i32) = (1, 2);

    x.0 = 5;
    x.1 += 20;

    println!("{x:?}");
}

fn arrays() {
    let a = [1, 2, 3, 4, 5];
    println!("{a:?}");

    let months = ["January", "February", "March", "April", "May", "June", "July",
              "August", "September", "October", "November", "December"];
    println!("{months:?}");

    let a: [i32; 5] = [1, 2, 3, 4, 5];
    println!("{a:?}");

    let multiple_arrays_elem = [3; 5];
    println!("{multiple_arrays_elem:?}");

    let first = a[0];
    let second = a[1];

    println!("{first}, {second}");
}

fn another_function(x: i32, unit_label: char, mystr: &str) {
    println!("başka bir fonksiyon örneği. İşte parametre olarak verilen x değeri {x} and unit label : {unit_label}, my string value : {mystr}");

    let y = {
        let x = 3;
        x + 1
    };

    println!("The value of y is: {y}");
}

fn five() -> u8 {
    5
}

fn addition(a: i32, b: i32) -> i32 {
    // verilen iki parametrenin toplamını döndürür.
    a + b
}

fn if_expression() {
    let number: u8 = 3;

    if number < 5 {
        println!("Sayı 5 ten küçük!");
    } else {
        println!("Sayı 5 ten küçük değil.")
    }

    if number != 0 {
        println!("Sayı 0 değil. Endişelenmeyin bu sadece bir kontroldü.");
    }

    let number: u8 = 6;

    if number % 4 == 0 {
        println!("{number}'ın 4 ten kalanı 0 dır.");
    } else if number % 3 == 0 {
        println!("{number}'ın 3 ten kalanı 0 dır.");
    } else if number % 2 == 0 {
        println!("{number}'ın 2 den kalanı 0 dır.");
    } else {
        println!("{number} sayısı 4, 3 ve 2 sayılarına bölümünden herhangi bir kalan sahip değildir.");
    }

    let condition: bool = true;

    let number = if condition { 5 } else { 6 };
    
    println!("number is {number}");

    let x: u8 = 1;
    if x == x {
        println!("{x} eşittir {x}'e");
    } else {
        println!("{x} eşit değildir {x}'e");
    }
}

fn main() {
    basic_variables();
    mathmatical();
    tuples();
    arrays();
    another_function(5, 'k', "selamlar ben ahmet");

    let x: u8 = five();
    println!("{x}");

    let sum = addition(3, 5);
    println!("{sum}");

    if_expression();
}
