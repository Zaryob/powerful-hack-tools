poimport library
================

.. image:: https://img.shields.io/badge/licence-AGPL%20(>%3D3)-blue
    :alt: License
    
It is a wrapper to use open `.po/.pot` files.

It is designed because of the other same reason libraries' 
difficulty.

* Using to read `.po/.pot` file:
```
>>> import poimport 
>>> po = poimport.Po()
>>> po.load("path_of_file")
>>> po.messages
    # It returns full list of po file's messages
```

* Getting several parameters of po file:
```
>>> po.messages[0].reference   # To get path of first expression
>>> po.messages[0].flags   # To get first flags' list
>>> po.messages[0].msgid   # To get first msgid 
>>> po.messages[0].msgstr  # To get first msgstr
```

* Using to create new `.po/.pot` file:
```
>>> import poimport
>>> po = poimport.Po(header=poimport.header_tmpl)
>>> msg = poimport.Message()
>>> msg.reference="Path/of/Expression"
>>> msg.flags=["some","different", "flags", "such as", "fuzzy"]
>>> msg.msgid = "Something"
>>> msg.msgstr = "Bir şey"
>>> po.messages = [msg]
```

### poimport.Message()
It is a list class for translation messages
```
        * reference: Path of Expression
        * flags: Flags of this po expression 
        * msgid: Non-Translated message
        * msgstr: Translated message
```

### poimport.Po()
It is wrapper class for `po` files.
```
        load: to load file
        save: to save file
        _escape: private function to fix strings
        _unescape: private function to fix strings
```



### poimport.header_tmpl
It is a template to create new `po` file. You can also use your own `po` template.
```
header_tmpl = """# SOME DESCRIPTIVE TITLE.
# Copyright (C) YEAR THE PACKAGE'S COPYRIGHT HOLDER
# This file is distributed under the same license as the PACKAGE package.
# FIRST AUTHOR <EMAIL@ADDRESS>, YEAR.
#
msgid ""
msgstr ""
"Project-Id-Version: PACKAGE VERSION\\n"
"Report-Msgid-Bugs-To: \\n"
"POT-Creation-Date: 2018-01-01 12:58+0200\\n"
"PO-Revision-Date: YEAR-MO-DA HO:MI+ZONE\\n"
"Last-Translator: FULL NAME <EMAIL@ADDRESS>\\n"
"Language-Team: LANGUAGE <LL@li.org>\\n"
"MIME-Version: 1.0\\n"
"Content-Type: text/plain; charset=UTF-8\\n"
"Content-Transfer-Encoding: 8bit\\n"
"""
```
