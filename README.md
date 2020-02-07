# Markd

A simple python package that faciliates the generation of markdown flavoured files

## Installation

```code
$ pip install markd
```

## Methods

### Add block methods

#### add_header(text, htype=1)

Adds an `htype` header block to the content  

ex: `add_header("H1"), add_header("H2", 2)`

#### add_text(text)

Adds a text block to the content

#### add_list_item(text, depth=None)

Adds a list item to the content with the specified `text` and intentation `depth`

ex: `add_list_item("List item 1"), add_list_item("List item 1.1", 1)`

#### add_linebreak()

Adds a linebreak block

#### add_blockquote(text)

Adds a blockquote with the specified `text`

#### add_horizontal_rule()

Adds a horizontal rule block

#### add_code(code)

Adds a code block

#### add_image(url, alt_text)

Adds an image using the specified `url` and `alt_text`

### Utility methods

#### link(url, text=None)

#### emphasis(text)

#### italics(text)

## Full Example

```code
from markd import Markdown()

if __name__ == '__main__':
    markd = Markdown()
    markd = Markdown()
    markd.add_header("This an H1 headers")
    markd.add_header("This is an H2 header", 2)
    markd.add_text("Lorem ipsum text")
    markd.add_blockquote("You can also add blockquotes!!")
    markd.add_text(markd.link("https://google.com"))
    markd.add_text(markd.link("https://google.com", "Link to google"))
    markd.add_list_item("List item 1")
    markd.add_list_item("List item 1.1", 1) # Sublist item
    markd.add_list_item("List item 1.1.1", 2) # Sublist item
    markd.add_list_item("List item 2")
    markd.add_list_item(markd.link("http://test.com","List item link"))
    markd.add_linebreak()
    markd.add_code("Some code here")
    markd.add_image("https://link.to/image.jpg", "alt-text")
    markd.add_horizontal_rule()
    print(markd.content) # Get the content
    markd.save("/path/to/save/the/file.md")
```
