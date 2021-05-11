#!/usr/bin/python3
"""0. How many subs"""

def number_of_subscribers(subreddit):
    """return the number of subscribers from an Reddit API"""

    import requests

    resInf = requests.get("https://www.reddit.com/r/{}/about.json"
                            .format(subreddit),
                            headers={"User-Agent": "My-User-Agent"},
                            allow_redirects=False)
    if resInf.status_code >= 300:
        return 0

    return resInf.json().get("data").get("subscribers")
