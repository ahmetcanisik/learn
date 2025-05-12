from fouri.ai import send_prompt
from fouri.repo import update_repo
from fouri.tweet import get_last_tweet
from re import fullmatch as re_fullmatch


def find_dizipal():
    last_tweet = get_last_tweet("5dizipal5")
    if last_tweet:
        send_text = f"{last_tweet}\nParse this text in URL, add 'https://' at the beginning, and '.com' at the end. Return only the raw URL."
        ai_res = send_prompt(send_text)

        if ai_res:
            ai_res = ai_res.strip()
            try:
                if re_fullmatch(r"https?://dizipal\d+\.\w+", ai_res):
                    update_repo(ai_res)
                else:
                    print("⚠️ AI response is not a valid URL format!")
            except Exception as err:
                print("❌ Error! New URL was not uploaded to GitHub!", err)
        else:
            print("⚠️ AI response not found!")

    else:
        print("⚠️ Latest tweet not found!")
