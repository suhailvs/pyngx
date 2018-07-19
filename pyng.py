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
                print('component already exist.')
        else:
            print('''please call with arguments(name of the menu, submenus), 
eg: python ng.py <component_name> '<subitem1>,<subitem2>,...<subitem10>''')
    

    def create_directories(self):
        print ('generating directories.')
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

    #print(s.render(menu = 'xx',submenus = ['some1','some2'],submenu=''))

    def create_menu(self):
        print('generating menu:', self.menu)
        # os.makedirs(self.menu)
        fdata = ['.component.ts','.module.ts','-routing.module.ts'] 
        for i in fdata:
            self.create_file(                
                fn = os.path.join(self.menu, self.menu + i),
                temp = self.read_template(os.path.join('menu', i[1:])),
            ) 

    def create_file(self, fn, temp, sm = [],extra=''):
        filedata = temp.render(
            menu=self.menu,
            submenus = self.submenus,
            submenu = sm,    
            extra=extra,       
        )
        fp = open(fn, 'w')
        fp.write(filedata)        
        print('%s created successfully.'%fn)
    
    def create_submenu(self,submenu):
        print('generating submenu:', submenu)        
        fdata = ['.service.ts', '.module.ts', '-routing.module.ts']

        for i in fdata:
            self.create_file(
                sm = submenu,
                fn = os.path.join(self.menu,submenu,submenu + i),
                temp = self.read_template(os.path.join('submenu', i[1:])),
            ) 
        # create components and pages
        for i in ['.component','-cu.component','-view.component']:
            
            self.create_file(
                sm = submenu,                
                fn = os.path.join(self.menu,submenu,'components','%s%s.ts'%(submenu,i)),
                temp = self.read_template(os.path.join('submenu', 'component.ts')),
                extra = i.split('.')[0][1:],
            ) 
            self.create_file(
                sm = submenu,                
                fn = os.path.join(self.menu,submenu,'pages','%s%s.html'%(submenu,i)),
                temp = self.read_template(os.path.join('submenu', 'component.html')),
            ) 

    def display_help(self):
        temp = self.read_template('help.ts')
        print(temp.render(menu=self.menu,submenus = self.submenus))

# please call with argument(name of the menu) eg: python ng.py controlpanel
if __name__=='__main__':
    c=GenerateMenu()
