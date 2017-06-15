import requests
from bs4 import BeautifulSoup

def continue_crawl(search_history, target_url):
    if search_history[-1] == target_url:
        print("We've found the target article!")
        return False
    elif len(search_history) > 25:
        print("The search has gone on suspiciously long; aborting search!")
        return False
    elif search_history[-1] in search_history[:-1]:
        print("We've arrived at an article we've already seen; aborting search!")
        return False
    else:
        return True﻿
