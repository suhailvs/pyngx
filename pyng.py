import os,sys
from string import Template
# from jinja2 import Template
from ng_templates import *

class GenerateMenu:
    def __init__(self):
        if len(sys.argv) is 2:
            self.menu = sys.argv[1]
            if not os.path.exists(self.menu):
                 self.create_menu()              
            else:
                print('component already exist.')
        else:
            print('''please call with argument(name of the menu) eg: python ng.py controlpanel''')
    
    def create_menu(self):
        print('generating menu:', self.menu)
        os.makedirs(self.menu)
        fdata = [
            ('.component.ts', COMPONENT_TEMPLATE),
            ('.module.ts', MODULE_TEMPLATE),
            ('-routing.module.ts', ROUTING_TEMPLATE),
        ] 
        for i in fdata:
            self.create_file(fname = self.menu + i[0],temp=Template(i[1])) 

    def create_file(self,fname,temp):        
        cmenu = self.menu.capitalize()
        fp = open(os.path.join(self.menu,fname), 'w')
        fp.write(temp.substitute(name=self.menu,cname = cmenu))        
        print('%s created successfully.'%fname)
    
    def create_submenus(self,f):
        print('generating menu:', self.menu)
        os.makedirs(self.menu)
        for i in 'cmr':
            self.create_file(flag=i) 
        #module = open(os.path.join(f,f+'module.ts'), 'w')
        #component = open(os.path.join(f,f+'component.ts'), 'w')
        #routing = open(os.path.join(f,f+'-routing.module.ts'), 'w')
        
        pass

# python ng.py <component_name> '<subitem1>,<subitem2>,...<subitem10>'
if __name__=='__main__':
    c=GenerateMenu()
