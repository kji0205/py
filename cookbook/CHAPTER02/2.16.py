"""텍스트 열의 개수 고정"""
import textwrap
import os

s = "Lec 1 | MIT 6.00 Introduction to Computer Science and Programming, Fall 2008 Lecture 1: Goals of the course; what is computation; introduction to data ty"
print(textwrap.fill(s, 70))
print(textwrap.fill(s, 40))
print(textwrap.fill(s, 40, initial_indent='    '))
print(textwrap.fill(s, 40, subsequent_indent='    '))

# print(os.get_terminal_size().columns)
