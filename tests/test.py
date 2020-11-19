from importlib import import_module
import unittest
import sys


class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def test_list(self):
        sys.path.append('..')
        flask_app = import_module('app')
        flask_app.app.testing = True
        with flask_app.app.test_client() as c:
            result = c.get('/week')
            # print(result.get_data(as_text=True))
            assert '<h3>月</h3>' in result.get_data(as_text=True)
            assert '<h3>火</h3>' in result.get_data(as_text=True)
            assert '<h3>水</h3>' in result.get_data(as_text=True)
            assert '<h3>木</h3>' in result.get_data(as_text=True)
            assert '<h3>金</h3>' in result.get_data(as_text=True)

    def test_dict(self):
        sys.path.append('..')
        flask_app = import_module('app')
        flask_app.app.testing = True
        with flask_app.app.test_client() as c:
            result = c.get('/week')
            assert '<h3>月</h3>' in result.get_data(as_text=True)
            assert '<h3>火</h3>' in result.get_data(as_text=True)
            assert '<h3>水</h3>' in result.get_data(as_text=True)
            assert '<h3>木</h3>' in result.get_data(as_text=True)
            assert '<h3>金</h3>' in result.get_data(as_text=True)
            assert '佐藤' in result.get_data(as_text=True)
            assert '鈴木' in result.get_data(as_text=True)
            assert '清水' in result.get_data(as_text=True)
            assert '中村' in result.get_data(as_text=True)
            assert '高橋' in result.get_data(as_text=True)


if __name__ == '__main__':
    unittest.main()
