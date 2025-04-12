# CopyPaste 🖋️

A simple Python CLI clipboard simulator using file I/O.  
Built for the terminal warriors who want `copy`, `paste`, `pin`, `unpin`, and `show_pin` features directly in their code life.

## Features
- 📋 `copy()`: Save something to file like it's your brain.
- 📤 `paste()`: Recall what you copied anytime.
- 📌 `pin()`: Save extra stuff at the bottom of the file.
- ❌ `unpin()`: Remove specific pins when you’re done.
- 🔍 `show_pin()`: View all pinned items matching a keyword.

## How to Use

```python
r = CopyPaste()
r.copy("Something")
print(r.paste())
r.pin("Important")
r.unpin("Important")
print(r.show_pin("SomeKeyword"))
