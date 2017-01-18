import os
import unittest

import sys
sys.path.append("src/crabblerweb")
import crabblerweb 

class Crabblerweb_Root(unittest.TestCase):

    def test_root(self):
        self.app = crabblerweb.app.test_client()
        out = self.app.get('/')        
        assert '200 OK' in out.status
#        assert 'charset=utf-8' in out.content_type
#        assert 'text/html' in out.content_type


class Crabblerweb_Up(unittest.TestCase):

    def test_up(self):
        
        self.app = crabblerweb.app.test_client()
        out = self.app.get('/up')
        assert '200 OK' in out.status
        #assert 'charset=utf-8' in out.content_type
        #assert 'text/html' in out.content_type


if __name__ == "__main__":
    unittest.main()
    

