import re
from pathlib import Path
from talon import Context, Module

ULTISNIPS_FOLDER = Path('/config/dotfiles/nvim/UltiSnips/')

mod = Module()
ctx = Context()

mod.list('ultisnips',
         desc='All the snippets coming from the ultisnips snips vim plugin')

snip_name_re = re.compile(r'^snippet\s*(\w+)\s')

snip_names = []
with open(ULTISNIPS_FOLDER / Path('python.snippets')) as f:
    for line in f:
        line = line.strip()

        if m := snip_name_re.match(line):
            snip_name = m.group(1)

            snip_names.append(snip_name)

snip_aliases = {
    'forstd': 'forshell'
}

ctx.lists['self.ultisnips'] = {
    # If no alias just use snip name as its alias
    snip_aliases.get(snip, snip): snip
    for snip in snip_names
}
