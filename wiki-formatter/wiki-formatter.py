#!/usr/bin/env python
from sys import argv
from html import escape
from tkinter import Tk
from typing import Final

tk: Final[Tk] = Tk()
tk.withdraw()
tk.clipboard_clear()
with open(argv[1]) as f:
    tk.clipboard_append("<pre><nowiki>\n")
    tk.clipboard_append(escape(f.read()).removesuffix("\n"))
    tk.clipboard_append("\n</nowiki></pre>")
tk.update()
tk.destroy()
