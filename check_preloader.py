import re
with open('live.html', 'r', encoding='utf-8') as f:
    html = f.read()

match = re.search(r'<p class="preloader__content__cover h1">(.*?)</p>', html, re.DOTALL)
if match:
    # Print repr to see non-breaking spaces
    print(repr(match.group(1).strip()))
