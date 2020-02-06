import unittest, os, time, sys, shutil

PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if not PATH in sys.path:
    sys.path.insert(1, PATH)
    from markd import Markdown
del PATH

class TestReports(unittest.TestCase):

    def setUp(self):
        self.output_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'test-output'))
        self.trace = '''
        Traceback (most recent call last):
        File "t.py", line 6, in <module>
            raise TypeError("Oups!")
        TypeError: Oups!
        '''

    def tearDown(self):
        shutil.rmtree(self.output_folder)
    
    def test_markdown_created(self):
        filename = self.output_folder + "/test.md"
        o = Markdown()
        o.add_header("This is a report h1")
        o.add_header("This is an h2", 2)
        o.add_text("Lorem ipsum text for the summary just to check how it works and if its possible")
        o.add_blockquote("You can also add blockquotes!!")
        o.add_code(self.trace)
        o.add_horizontal_rule()
        o.save(filename)
        self.assertTrue(os.path.isdir(self.output_folder))
        self.assertTrue(os.path.isfile(filename))
    

if __name__ == '__main__':
    unittest.main()