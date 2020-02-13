# Markd

A simple python3 package that facilitates the generation of markdown flavoured files

## Installation

```code
pip install markd
```

## Usage

### Initialize the module

```python
from markd import Markdown()

markd = Markdown()
```

### Add content blocks

#### add_header(text, htype=1)

Adds an `htype` header block to the content

```python
markd.add_header("H1")
markd.add_header("H2", 2)
```

#### add_text(text)

Adds a text block to the content

```python
markd.add_text("Sample text")
```

#### add_list_item(text, depth=None)

Adds a list item to the content with the specified `text` and intentation `depth`.
The `depth` parameter is used to create sublists.

```python
markd.add_list_item("List item 1")
markd.add_list_item("List item 1.1", 1)
markd.add_list_item("List item 1.2", 1)
markd.add_list_item("List item 1.2.1", 2)
```

#### add_linebreak()

Adds a linebreak block

```python
markd.add_linebreak()
```

#### add_blockquote(*lines)

Adds a blockquote with the specified `lines` of text

```python
markd.add_blockquote("This is a blockquote")
markd.add_blockquote("This is a", "multi line", "block quote")
```

#### add_horizontal_rule()

Adds a horizontal rule block

```python
markd.add_horizontal_rule()
```

#### add_code(code)

Adds a code block

```python
trace = '''
Traceback (most recent call last):
File "t.py", line 6, in <module>
    raise TypeError("Oups!")
TypeError: Oups!
    '''

markd.add_code(trace)
```

#### add_image(url, alt_text)

Adds an image using the specified `url` and `alt_text`

```python
markd.add_image("https://myimage.link/image.png", "my image")
```

#### add_table(\*rows)

Adds a table to the content provided a list of table `rows`.
The first row in the list, is considered to be the header.

```python
markd.add_table(
    ["Header cell 1", "Header cell 2", "Header cell 3"],
    ["Row 1 cell 1", "Row 1 cell 2", "Row 1 cell 3"],
    ["Row 2 cell 1", "Row 2 cell 2", "Row 2 cell 3"],
    )
```

### Utility methods

#### link(url, text=None)

Creates a markdown link that can be added in the content using the available add_* methods

```python
markd.add_text(markd.link("https://test.com", "test"))

```

#### emphasis(text)

Emphasizes a given text

```python
markd.add_text(markd.emphasis("Text to be emphasized"))
```

#### italics(text)

 Wraps the given text in italics

```python
markd.add_text(markd.italics("Enter text here"))
```

#### save(filename)

Saves the file to the specified path

```python
markd.save("/path/to/save/the/file.md")
```

## Full Example

```code
from markd import Markdown()

if __name__ == '__main__':
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
    markd.add_table(
    ["Header cell 1", "Header cell 2", "Header cell 3"],
    ["Row 1 cell 1", "Row 1 cell 2", "Row 1 cell 3"],
    ["Row 2 cell 1", "Row 2 cell 2", "Row 2 cell 3"],
    )
    markd.add_horizontal_rule()
    print(markd.content) # Get the content
    markd.save("/path/to/save/the/file.md")
```

## License

[GNU General Public License v3 (GPLv3)](https://github.com/panstel/markd/blob/master/LICENSE)
