import os,sys
from string import Template
#from jinja2 import Template
from ng_templates import *

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

    def create_menu(self):
        print('generating menu:', self.menu)
        # os.makedirs(self.menu)
        fdata = [
            ('.component.ts', COMPONENT_TEMPLATE),
            ('.module.ts', MODULE_TEMPLATE),
            ('-routing.module.ts', ROUTING_TEMPLATE),
        ] 
        for i in fdata:
            self.create_file(                
                fn = os.path.join(self.menu, self.menu + i[0]),
                temp = Template(i[1]),
            ) 

    def create_file(self,fn,temp,m=None):
        if not m: m=self.submenus[0]
        
        temps = temp.safe_substitute(
            menu=self.menu, 
            cmenu=self.menu.capitalize(),
            submenu = m, 
            subcmenu = m.capitalize(),            
        )
        fp = open(fn, 'w')
        fp.write(temps)        
        print('%s created successfully.'%fn)
    
    def create_submenu(self,submenu):
        print('generating submenu:', submenu)        
        fdata = [
            ('.service.ts', SUB_SERVICE_TEMPLATE),
            ('.module.ts', SUB_MODULE_TEMPLATE),
            ('-routing.module.ts', SUB_ROUTING_TEMPLATE),
        ] 
        for i in fdata:
            self.create_file(
                m=submenu,
                fn = os.path.join(self.menu,submenu,submenu + i[0]),
                temp=Template(i[1])
            ) 
        # create components and pages
        for i in ['','-cu','-view']:
            
            self.create_file(
                m=submenu,                
                fn = os.path.join(self.menu,submenu,'components',submenu+i+'.component.ts'),
                temp=Template(SUB_COMPONENT_TEMPLATE)
            ) 
            self.create_file(
                m=submenu,                
                fn = os.path.join(self.menu,submenu,'pages',submenu+i+'.component.html'),
                temp=Template(SUB_HTML_PAGE)
            ) 

    def display_help(self):
        s = Template('''

----------------------------------------------------
Now copy the folder to your project directory(src/app/modules/). 

Update src/app/modules/layout-routing.module.ts file::

const routes: Routes = [
    {
        path: '',
        component: LayoutComponent,
        children: [
        ....
        { path: '${menu}', loadChildren: './${menu}/${menu}.module#${cmenu}Module'}


Update app/shared/menu/menu.component.html::

<li><a><i class="fa fa-home"></i> ${cmenu} <span class="fa fa-chevron-down"></span></a>
<ul class="nav child_menu">
    <li><a [routerLink]="'/${menu}/SUBMENU'">${cmenu}</a></li>
    <li>...sub menus...</li>
</ul>
</li>     
''')
        print(s.safe_substitute(menu = self.menu,cmenu=self.menu.capitalize()))
# please call with argument(name of the menu) eg: python ng.py controlpanel
if __name__=='__main__':
    c=GenerateMenu()
