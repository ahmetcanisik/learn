import sys
from pynput.keyboard import Key, Listener, KeyCode

def main():
    def on_press(key):
        if key == Key.enter or key == KeyCode.from_char('y'):
            print("Accepted!")
            sys.exit()
            
        else:
            print("Rejected!")
            sys.exit()
    
    def on_release(key):
        if key == Key.esc:
            return False  # Stop listener
        
    print("You can accept this license agreements? (y|Enter to accept, Esc to exit)")
    
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    main()