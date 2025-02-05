struct User {
    active: bool,
    username: String,
    email: String,
    sign_in_count: u64
}

struct Color(u8, u8, u8);
struct Coordinate(i32, i32, i32);

struct Point { x: i32, y: i32 }

struct AlwaysEqual;

fn build_user(email: String, username: String) -> User {
    User {
        active: true,
        username,
        email,
        sign_in_count: 1,
    }
}

fn print_point(p: &Point) {
    println!("{}, {}", p.x, p.y);
}


fn pointer() {
    let mut p = Point { x: 0, y: 0 };
    print_point(&p);

    let x = &mut p.x;
    *x += 1;
    println!("{x}");
}

fn main() {
    let mut user1 = build_user(String::from("imcanisik@gmail.com"), String::from("canisik"));
    user1.email = String::from("can.isik.business@gmail.com");

    let user2 = User {
        email: String::from("ahmetcanisik35@gmail.com"),
        ..user1
    };

    println!("Okay! {}, email was sending you! check your inbox {}", user2.username, user2.email);

    // mean RGB
    let black = Color(0, 0, 0);
    let coordinate = Coordinate(0, 0, 0);

    println!("your first color codes is {}, your first coordinate is {}", black.0, coordinate.0);

    let subject = AlwaysEqual;

    pointer();
}
