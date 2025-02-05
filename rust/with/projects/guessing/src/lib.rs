pub mod game;

#[cfg(test)]
mod tests {
    use super::game::GuessingGame;

    #[test]
    fn it_works() {
        let mut game = GuessingGame {
            title: String::from("Test"),
            text: String::from("/test"),
            attempts_left: 1,
            guess_range: (0, 1),
        };
        
        assert_eq!(game.play(), "test passed!");
    }
}