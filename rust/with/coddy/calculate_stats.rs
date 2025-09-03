use std::io;
use std::convert::TryInto;

fn calculate_stats(arr: [i32; 8]) -> [f64; 4] {
    // Write your code here
    let mut sum = arr[0];
    let mut max = arr[0];
    let mut min = arr[0];
    for &num in &arr[1..] {
        sum += num;
        if num > max {
            max = num;
        }
        if num < min {
            min = num;
        }
    }
    let average = sum as f64 / arr.len() as f64;
    [sum as f64, average, max as f64, min as f64]
}

fn main() {
    let mut input_str_arr = String::new();
    io::stdin().read_line(&mut input_str_arr).unwrap();
    let numbers: [i32; 8] = input_str_arr.split(',').map(|s| s.parse::<i32>().unwrap()).collect::<Vec<i32>>().try_into().unwrap();
    let stats = calculate_stats(numbers);
    println!("Sum: {}", stats[0]);
    println!("Average: {}", stats[1]);
    println!("Maximum: {}", stats[2]);
    println!("Minimum: {}", stats[3]);
}
