import time
import requests
from bs4 import BeautifulSoup

def continue_crawl(search_history, target_url, max_steps=25):
    if search_history[-1] == target_url:
        print("We've found the target article!")
        return False
    elif len(search_history) > max_steps:
        print("The search has gone on suspiciously long; aborting search!")
        return False
    elif search_history[-1] in search_history[:-1]:
        print("We've arrived at an article we've already seen; aborting search!")
        return False
    else:
        return True﻿

def find_first_link(url):
    # return the first link as a string, or return None if there is no link

    # TODO:
    # get the HTML from "url", use the requests library
    # feed the HTML into Beautiful Soup
    # find the first link in the article
    # return the first link as a string, or return None if there is no links

while continue_crawl(article_chain, target_url):
    # TODO: download html of last article in article_chain
    # find the first link in that html
    first_link = find_first_link(article_chain[-1])
    # add the first link to article_chain
    article_chain.append(first_link)
    # delay for about two seconds
    time.sleep(2)
