import os,sys
#from string import Template
from jinja2 import Template

class GenerateMenu:
    def __init__(self):
        if len(sys.argv) is 3:
            self.menu = sys.argv[1]
            self.submenus = sys.argv[2].split(',')

            if not os.path.exists(self.menu):
                self.create_directories()
                self.create_menu()
                for submenu in self.submenus: self.create_submenu(submenu)
                self.display_help()
            else:
                print('component:%s already exist.'%self.menu)
        else:
            print('''please call with arguments(name of the menu, submenus), 
eg: python ng.py <component_name> '<subitem1>,<subitem2>,...<subitem10>''')
    

    def create_directories(self):
        # print ('generating directories.')
        for d in self.submenus:
            os.makedirs(os.path.join(self.menu,d,'components'))
            os.makedirs(os.path.join(self.menu,d,'pages'))

    def read_template(self,fname):
        # read template from file for eg: menu/component.ts
        contents = ""
        with open(fname) as f:
            for line in f.readlines():
                contents += line
        return Template(contents)

    def create_menu(self):
        # print('generating menu:', self.menu)
        fdata = ['.component.ts','.module.ts','-routing.module.ts'] 
        for i in fdata:
            self.create_file(                
                fn = os.path.join(self.menu, self.menu + i),
                temp = self.read_template(os.path.join('menu', i[1:])),
            ) 

    def create_file(self, fn, temp, sm = '',extra=''):
        filedata = temp.render(
            menu=self.menu,
            submenus = self.submenus,
            submenu = sm,    
            extra=extra,       
        )
        fp = open(fn, 'w')
        fp.write(filedata)        
        # print('%s created successfully.'%fn)
    
    def create_submenu(self,submenu):
        # print('generating submenu:', submenu)

        for i in ['.service.ts', '.module.ts', '-routing.module.ts']:
            self.create_file(
                sm = submenu,
                fn = os.path.join(self.menu,submenu,submenu + i),
                temp = self.read_template(os.path.join('submenu', i[1:])),
                extra = submenu.rstrip('s') # if last letter is s, remove it
            )
        self.create_components(submenu)

    def display_help(self):
        template = self.read_template('help.ts')
        print(template.render(menu = self.menu, submenus = self.submenus))

    def create_components(self,submenu):
        # create components and pages
        # there are 3 components for (submenu users) -> 
        #   1. users-cu.component.ts/html
        #   2. users-view.component.ts/html
        #   3. users.component.ts/html
        #template_name = lambda e: i[1:] + e # eg: cu.component.ts/cu.component.html

        create_file = lambda folder,fname,template_file: self.create_file(
            sm = submenu,
            fn = os.path.join(self.menu,submenu,folder,fname),
            temp = self.read_template(os.path.join('submenu',folder,template_file )),
            extra = submenu.rstrip('s') )

        for i in ['.component','-cu.component','-view.component']:
            # eg: submenu/components/component.ts, submenu/pages/component.html
            create_file('components', '%s%s.ts'%(submenu,i), i[1:] + '.ts')
            create_file('pages', '%s%s.html'%(submenu,i), i[1:] + '.html')                


if __name__=='__main__':
    c=GenerateMenu()
