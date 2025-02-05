#[derive(Debug)]
struct Rectangle {
    width: u32,
    height: u32
}

impl Rectangle {
    fn area(&self) -> u32 {
        self.width * self.height
    }

    fn width(&self) -> bool {
        self.width > 0
    }

    fn set_width(&mut self, width: u32) {
        self.width = width;
    }

    fn can_hold(&self, other: &Rectangle) -> bool {
        self.width > other.width && self.height > other.height
    }

    fn square(size: u32) -> Self {
        Self {
            width: size,
            height: size
        }
    }
}

fn main() {
    let rect1 = Rectangle {
        width: 30,
        height: 50,
    };

    let mut rect2 = Rectangle {
        width: 10,
        height: 40,
    };

    let mut rect3 = Rectangle {
        width: 60,
        height: 45,
    };


    // like, String::from("hello, world!");
    let square = Rectangle::square(30);

    println!("Square size is {square:?}");


    if rect1.width() {
        println!("The rectangle has a nonzero width; it is {}", rect1.width);
    }

    println!(
        "The area of rectangle is {} square pixels.",
        rect1.area()
    );

    rect2.set_width(154);
    rect3.set_width(12);

    println!("Can rect1 hold rect2? {}", rect1.can_hold(&rect2));
    println!("Can rect1 hold rect3? {}", rect1.can_hold(&rect3));

    let test_area_length = Rectangle::area(&rect2);
    println!("{}", test_area_length);

    println!("{}", String::from("hello"));

}