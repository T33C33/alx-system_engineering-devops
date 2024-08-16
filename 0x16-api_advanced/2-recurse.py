#!/usr/bin/python3
import requests


"""
A recursive function that
queries the Reddit API
and returns a list containing the titles
of all hot articles for a given subreddit.
If no results are found for the given subreddit,
the function should return None.
"""


def recurse(subreddit, hot_list=[], next_page="", total_count=0):
    """Returns a list of titles of all hot posts on a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "after": next_page,
        "count": total_count,
        "limit": 100
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        return None

    data = response.json().get("data")
    next_page = data.get("after")
    total_count += data.get("dist")
    for child in data.get("children"):
        hot_list.append(child.get("data").get("title"))

    if next_page is not None:
        return recurse(subreddit, hot_list, next_page, total_count)
    return hot_list
