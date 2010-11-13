from handlers import FooHandler

url_patterns = [
    (r"/foo/([^/]+)/", FooHandler),
]
