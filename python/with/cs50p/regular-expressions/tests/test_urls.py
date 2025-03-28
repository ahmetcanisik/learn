from validatev2 import is_valid_url
from twitterv2 import is_twitter_url

def test_is_valid_email():
    assert is_valid_url("https://ahmetcanisik.com") == True
    assert is_valid_url("http://ahmetcanisik.com") == True
    assert is_valid_url("https://ahmetcanisik.com") == True
    assert is_valid_url("ftp://ahmetcanisik.com") == False

def test_is_twitter_url():
    assert is_twitter_url("https://twitter.com") == True
    assert is_twitter_url("https://www.twitter.com") == True
    assert is_twitter_url("twitter.com") == True
    assert is_twitter_url("www.twitter.com") == True
    assert is_twitter_url("http://x.com") == True
    assert is_twitter_url("x.com") == True
    assert is_twitter_url("x.com/some-other-languages.html") == True
    assert is_twitter_url("x.com/acanisik") == True
    
    assert is_twitter_url("ftp://x.com") == False
    assert is_twitter_url("example.com") == False
    assert is_twitter_url("https://somedomain.com") == False
    assert is_twitter_url("https://.com") == False
    assert is_twitter_url("https://x.org/") == False