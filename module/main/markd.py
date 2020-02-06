import os, time
import inspect

class Markdown():
    
    def __init__(self):
        self.content = ""

    def add_text(self, text):
        self.content += self.__create_block(text, 2)
        return self

    def add_list_item(self, text):
        self.content += self.__create_block("- {}".format(text))
        return self
    
    def add_linebreak(self):
        self.content += self.__create_block("", 1)
        return self
    
    def add_blockquote(self, text):
        self.content += self.__create_block("> " + text, 2)
        return self

    def add_header(self, text, h=1):
        string = "".join(["#"] * h) + " {t}".format(t=text)
        self.content += self.__create_block(string, 2)
        return self
    
    def add_horizontal_rule(self):
        self.content += self.__create_block("___")
        return self
    
    def add_code(self, code):
        codeblock = inspect.cleandoc(
            """```code
            {c}
            ```""").format(c=code.lstrip().rstrip())
        self.content += self.__create_block(codeblock, 2)
        return self

    def add_image(self, url, alt_text):
        self.content += self.__create_block("![{}]({})".format(alt_text, url), 2)
        return self

    def link(self, link, text=None):
        t = text if text is not None else link
        return "[{}]({})".format(t, link)

    def emphasis(self, text):
        return "**{}**".format(text)
    
    def italics(self, text):
        return "*{}*".format(text)

    def __create_block(self, text='', times=1):
        return text + "".join(['\n'] * times)
    
    def save(self, filename):
        if not os.path.exists(filename):
            try:
                os.makedirs(os.path.dirname(filename), exist_ok=True)
            except OSError as exc: # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise
                
        f = open(filename, "w")
        f.write(self.content)
        f.close()