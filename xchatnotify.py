__module_name__         = "Xchatnotify" 
__module_version__      = "1.0" 
__module_description__  = "Pops up libnotify messages based on regular expressions"
__module_author__       = "Jonty Wareing <jonty@jonty.co.uk>"

import os, re, xchat, pynotify
pynotify.init("Xchatnotify")
regexes = []

EVENTS = [
    "Channel Action",
    "Channel Action Hilight",
    "Channel Message",
    "Channel Msg Hilight",
    "Channel Notice",
    "Generic Message",
    "Private Message",
    "Private Message to Dialog",
]

def parse(word, word_eol, extra):
    if len(word) == 2:
        for pattern in regexes:
            if pattern.search(word[1]):
                notification = pynotify.Notification(word[0], word[1])
                notification.show()
                break

    return xchat.EAT_NONE

path = os.path.expanduser("~") + "/.xchatnotify";
if os.path.exists(path):
    file = open(path ,"r")
else:
    print "Could not open ~/.xchatnotify regular expression file"

for pattern in file:
    compiled = re.compile(pattern.strip(), re.IGNORECASE)
    regexes.append(compiled)

for event in EVENTS:
    xchat.hook_print(event, parse)

print "Xchatnotify plugin loaded (%d rules found)" % (len(regexes), )

# vim:ts=4:sw=4:et
