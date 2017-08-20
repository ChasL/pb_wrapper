# PB_WRAPPER

A simple Pastebin wrapper written in Python 3.4

# Code examples:

<b>Create paste with no additional arguments:</b>
```python
from pb_api import PasteAPI

pb = PasteAPI('devkey', 'userkey') # userkey optional
pb.create_paste('Paste content')
```
<b>Create paste with a title, formatted for python, Private, and expiring in 1 hour:</b>
(see pb_lists.py for valid arguments for format, privacy, and expire)
```python
from pb_api import PasteAPI

pb = PasteAPI('devkey', 'userkey') # userkey optional
pb.create_paste('Paste content', title='Paste Title', format='python', privacy='2', expire='1H')
```

<b>List pastes made by the user:</b>
```python
from pb_api import PasteAPI

pb = PasteAPI('devkey', 'userkey') # userkey mandatory for list_user_pastes()
pb.list_user_pastes(limit=10) # limit argument optional. defaults to 50
```
# Requirements
The only requirement is the <b>requests</b> package

```pip3 install requests```
