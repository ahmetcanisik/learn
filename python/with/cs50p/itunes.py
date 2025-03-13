#!/usr/bin/env python3
import requests
import json
import sys

def main():
    if len(sys.argv) != 2:
        fa = input("Who is your favorite artist? ")
    else:
        fa = sys.argv[1]

    songs = req_itunes(fa)

    print(f"{fa} song list below:")
    
    for song in songs["results"]:
        print(f"{song["trackName"]}")
    
def req_itunes(artist: str = None):
    try:
        if artist is None:
            raise ValueError("Please specify the artist name!")
        
        res = requests.get(f"https://itunes.apple.com/search?entity=song&limit=1&term={artist}")
        
        if res.status_code == 200:
            return res.json()
    except Exception as err:
        print("-> Something went wrong on requesting itunes server!\n", err)
    
if __name__ == "__main__":
    main()