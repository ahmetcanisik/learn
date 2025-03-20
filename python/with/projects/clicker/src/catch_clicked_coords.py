#!/usr/bin/env python3
from pynput.mouse import Listener

def on_clicked_screen(x, y, button, pressed):
    if pressed:
        print("clicked screen coors: ", x, y)

with Listener(on_click=on_clicked_screen) as listener:
    listener.join()

def main():
	on_clicked_screen()
	
if __name__ == "__main__":
	main()