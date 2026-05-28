#!/usr/bin/env python
from sys import argv
from html import escape
from textwrap import indent
from tkinter import Tk
from typing import Final

tk: Final[Tk] = Tk()
tk.withdraw()
tk.clipboard_clear()
with open(argv[1]) as f:
    tk.clipboard_append(
        escape(indent(f.read(), " ", lambda line: True), quote=True).replace(
            "&#x27;", "&apos;"
        )
    )
tk.update()
tk.destroy()
