#!/usr/bin/python3
"""3. Count it"""


def count_words(subreddit, word_list, word_count={}, after=None):
    """prints a sorted count of given keywords"""
    
import requests

    resInf = requests.get("https://www.reddit.com/r/{}/hot.json"
                            .format(subreddit),
                            params={"after": after},
                            headers={"User-Agent": "My-User-Agent"},
                            allow_redirects=False)
    if resInf.status_code != 200:
        return None

    inf = resInf.json()

    hotL = [child.get("data").get("title")
             for child in inf
             .get("data")
             .get("children")]
    if not hotL:
        return None
