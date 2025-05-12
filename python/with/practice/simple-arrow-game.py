#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class ArrowGame:
    def __init__(self):
        self.arrow_position = 0
        self.arrow_direction = 1  # 1 for right, -1 for left
        self.arrow_length = 5
        self.game_over = False

    def move_arrow(self):
        if not self.game_over:
            self.arrow_position += self.arrow_direction
            if self.arrow_position < 0 or self.arrow_position >= 10:
                self.game_over = True

    def change_direction(self):
        if not self.game_over:
            self.arrow_direction *= -1

    def display(self):
        arrow_line = ["-" for _ in range(10)]
        arrow_line[self.arrow_position] = ">"
        print("".join(arrow_line))

    def play(self):
        while not self.game_over:
            self.display()
            command = input("Press 'm' to move, 'c' to change direction, 'q' to quit: ")
            if command == "m":
                self.move_arrow()
            elif command == "c":
                self.change_direction()
            elif command == "q":
                break
            else:
                print("Invalid command. Try again.")
        print("Game Over!")


def main():
    game = ArrowGame()
    game.play()


if __name__ == "__main__":
    main()
