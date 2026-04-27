
import re
from bs4 import BeautifulSoup

with open('index.html', 'r', encoding='utf-8') as f:
    html_bad = f.read()

with open('live.html', 'r', encoding='utf-8') as f:
    html_good = f.read()

soup_bad = BeautifulSoup(html_bad, 'html.parser')
soup_good = BeautifulSoup(html_good, 'html.parser')

bad_nodes = soup_bad.find_all(string=lambda t: '\uFFFD' in t if t else False)
good_nodes = soup_good.find_all(string=lambda t: t.strip() != '' if t else False)

# This might be hard to align. Let's try a simpler approach.
# Find all text nodes in good_soup.
# We can just replace the whole body from good_soup, but we need to fix the asset paths.

