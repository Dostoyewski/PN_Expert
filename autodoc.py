import os
import sys

sys.path.append(os.path.abspath('C:\\Users\\Федор\\Documents\\GIT\\PN_Expert'))  # path to your django project

# Specify settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PN_Expert.settings')

# Setup Django
import django

django.setup()

import pdoc

modules = ['PN_Expert', 'diagnostic', 'lk', 'media', 'pills', 'push_notifications', 'sheduling', 'survey',
           'video_proc']
context = pdoc.Context()

modules = [pdoc.Module(mod, context=context)
           for mod in modules]
pdoc.link_inheritance(context)


def recursive_htmls(mod):
    yield mod.name, mod.html()
    for submod in mod.submodules():
        yield from recursive_htmls(submod)


for mod in modules:
    for module_name, html in recursive_htmls(mod):
        with open(f"./docs/{module_name}.html", "w", encoding="utf8") as f:
            f.write(html)
