Now copy the folder to your project directory(src/app/modules/). 
Update src/app/modules/layout-routing.module.ts file::

const routes: Routes = [
    {
        path: '',
        component: LayoutComponent,
        children: [
        ....
        { path: '{{ menu }}', loadChildren: './{{ menu }}/{{ menu }}.module#{{ menu|title }}Module'},

Update app/shared/menu/menu.component.html::

<li>
    <a><i class="fa fa-home"></i> {{ menu|title }} <span class="fa fa-chevron-down"></span></a>
    <ul class="nav child_menu">
	{% for submenu in submenus %}<li><a [routerLink]="'/{{ menu }}/{{submenu}}'">{{ submenu|title }}</a></li>        
    {% endfor %}</ul>
</li>