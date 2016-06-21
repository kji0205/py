"""HTML과 XML 엔티티 처리"""
import html
from html.parser import HTMLParser
from xml.sax.saxutils import unescape

s = 'Elements are written an "<tag>text</tag>"'
print(s)
print(html.escape(s))
print(html.escape(s, quote=False))

#
s = 'spicy jalapeno'
print(s.encode('ascii', errors='xmlcharrefreplace'))
s = 'spicy &quot;jalapeno241;o&quot.'
p = HTMLParser(s)
print(p.unescape(s))

#
t = 'The prompt is &gt;&gt;&gt;'
print(unescape(t))
