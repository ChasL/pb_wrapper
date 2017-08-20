# PB_WRAPPER

A simple Pastebin wrapper written in Python

# Code examples:

Create anonymous paste:
```python
>>>create_paste('yourdevkey', 'Paste content here')`
```
Create user paste with a title, formatted for python, Private, and expiring in 1 hour:

(see pb_lists.py for accepted arguments for format, privacy, and expire)
```python
>>>create_paste('devkey', 'Paste content', 'userkey', title='Paste Title', format='python', privacy='2', expire='1H')
```
