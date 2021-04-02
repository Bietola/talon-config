from talon import Module, Context

import os

mod = Module()
ctx = Context()

@mod.action_class
class Actions:
    def jojo():
        "Play Jojo themesong"
        os.system("mplayer /home/dincio/music/memes/jojo.opus")
