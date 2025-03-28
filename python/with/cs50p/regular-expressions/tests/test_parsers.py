from parser import parse_emails, parse_urls
from twitterv2 import parse_user_name

"""
Test: Parse twitter user name in the text.
"""
def test_parse_twitter_user_name():
    assert parse_user_name("x.com/acanisik") == "acanisik"
    assert parse_user_name("twitter.com/@acanisik") == "@acanisik"

"""
Test: Parse email adresses in the text.
"""
def test_parse_emails():
    assert parse_emails(
        """
        imcanisik@gmail.com adlı gmail hesabım benim ana google hesabımdır.
        Aynı zamanda apple üzerinde de ana hesabımdır kendisi,
        yan hesap olarak ise can.isik.business@gmail.com adresini kullanmaktayım.
        Aynı zamanda protonmail sistemleri üzerinden aldığım
        secretly.sineks@proton.me ile de anonim işlemlerimi halletmekteyim.
        """
        ) == ["imcanisik@gmail.com", "can.isik.business@gmail.com", "secretly.sineks@proton.me"]



"""
Test: Parse url adresses in the text.
"""
def test_parse_urls():
    assert parse_urls(
        """
        Şahsi web sayfam olan https://ahmetcanisik.com adresine
        göz atmanızı şiddetle tavsiye eder ayriyeten http://canisik.me
        ve ahmetcanisik.github.io adreslerine de uğramanızı öneririm.
        """
        ) == ["https://ahmetcanisik.com", "http://canisik.me", "ahmetcanisik.github.io"]