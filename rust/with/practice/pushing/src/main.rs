use std::env;

fn main() {
    let mut manifest = env::current_dir().unwrap();
    manifest.push("test.rs");
}
