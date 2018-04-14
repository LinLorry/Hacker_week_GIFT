# !/bin/python3
# -*- coding:utf8 -*-

from project import create_app

app = create_app("Test")

if __name__ == '__main__':
    app.run()

