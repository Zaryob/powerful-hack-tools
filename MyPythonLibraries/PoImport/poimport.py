# -*- coding: utf-8 -*-
import re

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

class Message:
    def __init__(self):
        self.reference = None
        self.flags = []
        self.msgid = None
        self.msgstr = None


class Po:
    def __init__(self, messages = None, header = None):
        self.messages = messages or []
        self.header = header or header_tmpl

    def _escape(self, str):
        if not str:
            return '""'

        str = re.sub('"', '\\"', str)

        parts = str.split("\n")

        if len(parts) == 1:
            return '"{}"'.format(parts[0])

        if str.endswith("\n"):
            parts = parts[:-1]

        ret = '""' + "".join(map(lambda x: '\n"{}\\n"'.format(x), parts))

        return ret

    def save(self, filename):
        f = open(filename, "w")
        f.write(self.header)
        for msg in self.messages:
            po_entry = "\n#: {}\n".format(msg.reference)
            if msg.flags:
                po_entry += "#, " + ", ".join(msg.flags) + "\n"
            po_entry += "msgid {}\n".format(self._escape(msg.msgid))
            po_entry += "msgstr {}\n".format(self._escape(msg.msgstr))
            f.write(po_entry)
        f.close()

    def _unescape(self, str):
        str = re.sub('\\\\"', '"', str)
        str = re.sub('\\\\n', '\n', str)
        return str

    def load(self, filename):
        sHeader, sSkip, sComment, sId, sMsg = range(5)
        self.messages = []
        self.header = ""
        msg = None
        state = sHeader
        # Silly state machines are easier to code than dealing with regexps
        for line in open(filename):
            line = line.rstrip("\n")

            if state == sHeader:
                if len(line.split()) == 0:
                    state = sSkip
                else:
                    self.header += line + "\n"
                continue

            if state == sSkip:
                if len(line.split()) != 0:
                    msg = Message()
                    state = sComment
                else:
                    continue

            if state == sComment:
                if line.startswith("#: "):
                    msg.reference = line[3:]
                    continue
                elif line.startswith("#, "):
                    msg.flags = line[3:].split(',')
                    continue
                elif line.startswith("msgid "):
                    state = sId
                else:
                    continue

            if state == sId:
                if line.startswith("msgstr "):
                    state = sMsg
                else:
                    if line == 'msgid ""':
                        continue
                    if not msg.msgid:
                        msg.msgid = ""
                    msg.msgid += line[line.find('"')+1:line.rfind('"')]

            if state == sMsg:
                if len(line.split()) == 0:
                    msg.msgid = self._unescape(msg.msgid)
                    msg.msgstr = self._unescape(msg.msgstr)
                    self.messages.append(msg)
                    state = sSkip
                else:
                    if not msg.msgstr:
                        msg.msgstr = ""
                    if line == 'msgstr ""':
                        continue
                    msg.msgstr += line[line.find('"')+1:line.rfind('"')]
