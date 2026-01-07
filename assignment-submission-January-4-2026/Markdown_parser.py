import re

# Simple Markdown → HTML parser with user input
# Supports: # Heading, **bold**, *italic*, `code`, links [text](url)

def markdown_to_html(text):
    # Headings
    text = re.sub(r'^# (.+)$', r'<h1>\1</h1>', text, flags=re.MULTILINE)
    text = re.sub(r'^## (.+)$', r'<h2>\1</h2>', text, flags=re.MULTILINE)
    text = re.sub(r'^### (.+)$', r'<h3>\1</h3>', text, flags=re.MULTILINE)

    # Bold and italic
    text = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', text)
    text = re.sub(r'\*(.+?)\*', r'<i>\1</i>', text)

    # Inline code
    text = re.sub(r'`(.+?)`', r'<code>\1</code>', text)

    # Links
    text = re.sub(r'\[(.+?)\]\((https?://.+?)\)', r'<a href="\2">\1</a>', text)

    return text

markdown = input("Enter Markdown text: ")
html = markdown_to_html(markdown)

print("\nConverted HTML:\n")
print(html)
