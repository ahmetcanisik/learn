from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json
import time

def search_pornhub(query: str, page: int = 1):
    options = Options()
    options.headless = True
    options.add_argument("--disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(options=options)

    url = f"https://www.pornhub.com/webmasters/search?search={query}&page={page}"
    driver.get(url)

    time.sleep(5)  # JavaScript çözmesi için bekleme
    source = driver.find_element("tag name", "pre").text

    driver.quit()

    try:
        data = json.loads(source)
        return data
    except json.JSONDecodeError:
        print("JSON çözümlenemedi.")
        return None

def main():
    query = "chechick"
    results = search_pornhub(query)

    if results["videos"]:
        for video in results["videos"]:
            print(f"{video["duration"]} {video["title"]}")
    else:
        print("Hiç sonuç alınamadı.")

if __name__ == "__main__":
    main()