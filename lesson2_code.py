# -*- coding: utf-8 -*-
"""
Created on Sun Jan 01 16:30:40 2017

@author: MAHE
"""
def get_next_target(page):
    start_link = page.find('<a href=')

    #Insert your code below here
    if(start_link==-1):
        return None,0
    else:
        start_quote = page.find('"', start_link)
        end_quote = page.find('"', start_quote + 1)
        url = page[start_quote + 1:end_quote]
        return url, end_quote

def print_all_links(page):
    while True:
        url,endpos=get_next_target(page)
        if url:
            print url
            page=page[endpos:]
        else:
            break