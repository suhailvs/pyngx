from jinja2 import Template
def read_template(fname='help.ts'):
    contents = ""
    with open(fname) as f:
        for line in f.readlines():
            contents += line
    print (contents)
    s = Template(contents)
    print(s.render(menu = 'xx',submenus = ['some1','some2'],submenu=''))

read_template()