#!/usr/bin/env python
from nnt import Nnt
#from argparse import ArgumentParser

def main():
    NumNumText = Nnt()
    """
    parser = ArgumentParser(
        prog="NumNumText",
        description="Numbers to Text Numbers Converter"
    )
    
    parser.add_argument("folder", default='.', type=str, help="Specify the folder (default: ./)")
    
    args = parser.parse_args()
    """
    
    
    print(NumNumText.num2text(int(input("Num: "))))
    

if __name__ == "__main__":
    main()