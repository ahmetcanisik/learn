#!/usr/bin/env python3
import re


def main():
    sentence = input("Enter your sentence: ").strip()

    urls = parse_urls(sentence)

    print(urls)


def parse_urls(sentence: str = None) -> list[str]:

    if sentence is None:
        raise ValueError("please specify the sentence")

    return re.search(r"^(https?)://[\w-]+\.\w{2,4}$", sentence)


def is_valid_url(url: str = None) -> bool:

    if url is None:
        raise ValueError("please specify the url address")

    if re.search(r"^(https?)://[\w-]+\.\w{2,4}$", url):
        return True

    return False


if __name__ == "__main__":
    main()
