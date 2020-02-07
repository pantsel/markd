""" Package tests	"""

import unittest
import os
import sys
import shutil

PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if not PATH in sys.path:
    sys.path.insert(1, PATH)
    from markd import Markdown
del PATH

class TestReports(unittest.TestCase):

    """ Package tests	"""

    def setUp(self):
        """
        Setup tests
        """
        folder = os.path.join(os.path.dirname(__file__), '..', 'test-output')
        self.output_folder = os.path.abspath(folder)
        self.trace = '''
        Traceback (most recent call last):
        File "t.py", line 6, in <module>
            raise TypeError("Oups!")
        TypeError: Oups!
        '''

    def tearDown(self):
        """
        Remove test folders after testing
        """
        shutil.rmtree(self.output_folder)

    def test_markdown_created(self):
        """
        Test that the markdown file was created
        """
        filename = self.output_folder + "/test.md"
        output = Markdown()
        output.add_header("This is a report h1")
        output.add_header("This is an h2", 2)
        output.add_text("Lorem ipsum text for the summary")
        output.add_blockquote("You can also add blockquotes!!")
        output.add_code(self.trace)
        output.add_horizontal_rule()
        output.save(filename)
        self.assertTrue(os.path.isdir(self.output_folder))
        self.assertTrue(os.path.isfile(filename))


if __name__ == '__main__':
    unittest.main()
