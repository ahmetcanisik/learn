# from word2number import w2n
# w2n.word_to_num(input("What is the answer to the Great Question of Life, the Universe and Everything? "))
answer = (
    input(
        "What is the answer to the Great Question of Life, the Universe and Everything? "
    )
    .strip()
    .lower()
)

if answer == "42" or answer == "forty-two" or answer == "forty two":
    print("Yes")
else:
    print("No")
