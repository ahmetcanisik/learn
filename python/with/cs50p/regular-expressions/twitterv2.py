#!/usr/bin/env python3
import re


def main():
    url = input("Enter your twitter url: ").strip()
    print(parse_user_name(url))


def parse_user_name(url: str | None = None) -> str | None:

    if url is None or not url:
        raise ValueError("Please specify the twitter url!")

    if not is_twitter_url(url):
        return None

    if match := re.search(
        r"^(?:https?:\/\/)?(?:www\.)?(?:twitter|x)\.com\/([\w@]+)", url.strip().lower()
    ):
        return match.group(1)

    return None


def is_twitter_url(url: str | None = None) -> bool:

    if url is None or not url:
        raise ValueError("Please specify the twitter url!")

    """
    currently not allows the subdomains.
    """
    if re.search(
        r"^(https?:\/\/)?([a-zA-Z0-9-]+\.)?(twitter|x)+\.com+(\/.*)?$",
        url.strip().lower(),
    ):
        return True

    return False


if __name__ == "__main__":
    main()
