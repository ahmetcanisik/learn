#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests
import webbrowser
import customtkinter

"""
Find the HDFilmCehennemi embed URL.
Example URL: https://www.hdfilmcehennemi.nl/1-the-hobbit-smaugun-corak-topraklari-hdf-5/
"""


def find_embed_url(url: str):
    res = requests.get(url)
    if res.status_code == 200:
        soup = BeautifulSoup(res.content, "html.parser")
        if soup.iframe:
            return soup.iframe.get("data-src")  # Use `.get()` to avoid KeyError
    return None  # Return None if no iframe is found


def open_in_browser(entry):
    url = entry.get()  # Get the URL from the Entry field
    if url:
        parsed_url = find_embed_url(url)
        if parsed_url:  # Check if URL was found
            webbrowser.open_new_tab(parsed_url)
        else:
            print("No embed URL found.")


def main():
    app = customtkinter.CTk()
    app.title("HDFilmCehennemi Embed Finder")
    app.minsize(width=400, height=200)
    app.maxsize(width=400, height=200)
    app.geometry("400x200")
    app.grid_columnconfigure(0, weight=1)

    title = customtkinter.CTkLabel(
        app, text="HDFilmCehennemi Embed Finder", font=("system", 20)
    )
    title.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    description = customtkinter.CTkLabel(
        app, text="Enter your hdfilmcehennemi url here and click 'Find' button."
    )
    description.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

    entry = customtkinter.CTkEntry(
        app,
        placeholder_text="https://www.hdfilmcehennemi.nl/1-the-hobbit-smaugun-corak-topraklari-hdf-5/",
    )
    entry.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

    # ✅ Pass a lambda to avoid executing the function immediately
    button = customtkinter.CTkButton(
        app, text="Find", command=lambda: open_in_browser(entry)
    )
    button.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

    app.mainloop()


if __name__ == "__main__":
    main()
