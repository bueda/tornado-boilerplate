#!/usr/bin/env python
import unittest

TEST_MODULES = [
    'list',
    'your',
    'test',
    'modules',
    'test.test_something',
]

def all():
    return unittest.defaultTestLoader.loadTestsFromNames(TEST_MODULES)

if __name__ == '__main__':
    import tornado.testing
    tornado.testing.main()
