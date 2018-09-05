# -*- coding: utf-8 -*-


class Paste(object):

    def __init__(self, key, title, user, size, date, expire, syntax, scrape_url, full_url):
        self.key = key
        self.title = title
        self.user = user
        self.size = size
        self.date = date
        self.expire = expire
        self.syntax = syntax
        self.scrape_url = scrape_url
        self.full_url = full_url
        self.body = None

    def set_body(self, body):
        self.body = body