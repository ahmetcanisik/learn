use std::io::{self, Write};

fn day_prefix(this_day: &str, add_line: &str) -> String {
    format!(
        "On the {} day of Christmas,\n{}And a partridge in a pear tree.\n\n",
        this_day, add_line
    )
}

fn main() {
    let days: [&str; 12] = [
        "first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth",
        "tenth", "eleventh", "twelfth",
    ];
    let in_days: [&str; 12] = [
        "my true love gave to me",
        "Two turtle doves,",
        "Three French hens,",
        "Four calling birds,",
        "Five golden rings,",
        "Six geese a-laying,",
        "Seven swans a-swimming,",
        "Eight maids a-milking,",
        "Nine ladies dancing,",
        "Ten lords a-leaping,",
        "Eleven pipers piping,",
        "Twelve drummers drumming,",
    ];

    let mut lyrics = String::new();

    for (index, day) in days.iter().enumerate() {
        let mut this_piece = String::new();
        let mut day_index = 0;
        while day_index <= index {
            this_piece += &format!("{}\n", in_days[day_index]);
            day_index += 1;
        }
        lyrics += &day_prefix(day, &this_piece);
    }

    println!(
        "The Twelve Days of Christmas!\nSong Lyrics...\n\n{}",
        lyrics
    );

    print!("Çıkmak için 'Enter' tuşuna basınız...");
    io::stdout()
        .flush()
        .expect("flush işlemi esnasında bir sorun meydana geldi!");
    io::stdin()
        .read_line(&mut String::new())
        .expect("Sadece Enter tuşuna basınız lütfen!!");
}
