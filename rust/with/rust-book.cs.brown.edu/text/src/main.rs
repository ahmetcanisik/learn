#[derive(Debug)]
struct Text {
    value: String,
}

impl Text {
    fn from(text: &str) -> Self {
        Self {
            value: text.to_string()
        }
    }

    fn length(&self) -> usize {
        self.value.len()
    }
}

fn main() {
    let text1 = Text::from("Hello");
    let text2 = Text {
        value: String::from("world!"),
    };

    println!("{}, {}", text1.value, text2.value);
    println!("text1 length is {}, text2 length is {}", text1.length(), text2.length());
}
