#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

def tag_finder(tag: str):
    matches = re.match(r"^<([a-z-0-9]+)\s{1,}", tag)
    if matches:
        return matches.group(1)


def forms(form: str):
    matches = re.match(r"^<form\s{1,}(?:(method|action|data-[a-z0-9-]+)=[\"\'](.+)[\"\']))?", form)
    if matches:
        return matches.groups()

def links(link: str):
    matches = re.match(r"^<a+\s{1,}href=[\"\'](.+)[\"\']>(.+)?<\/a>$", link)
    if matches:
        return matches.groups()

def main():
    #tag = "<a href='https://example.com'>Example</a>"
    tag = "<form action='click()' method='POST'>Example</form>"
    
    
    match tag_finder(tag):
        case "a":
            link, text = links(tag)
            print(f"Tag: {tag}\nLink: {link}\nText: {text}")
        case "form":
            action = forms(tag)
            print(f"Tag: {tag}\nAction: {action}")
        case _:
            print("Unknown tag")
    
if __name__ == "__main__":
    main()