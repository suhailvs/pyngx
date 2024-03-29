Now copy the folder "{{menu}}" to your project directory(src/app/modules/). 
Update src/app/modules/layout-routing.module.ts file::

const routes: Routes = [
    {       
        ...
        children: [
            ...
            { path: '{{ menu }}', loadChildren: () => import('./{{ menu }}/{{ menu }}.module').then((m) => m.{{ menu|title }}Module)},
        ]
    }
];

Update on BackEnd APP: dashboard/dashboard_menu.py::

SIDE_BAR_MENUS = [{
    ...
    {
        "menu_text": "{{ menu|title }}",
        "menu_icon": "fa fa-tasks",
        "role_type": ["SU", "A"],
        "sub_menu": [{
            "menu_text": "add_subtitle",
            "sub_sub_menu":[{% for submenu in submenus %}
                {"link": "/{{ menu }}/{{submenu}}", "menu_text": "{{ submenu|title }}", "role_type": ["SU", "A"]},{% endfor %}
            ]
        },{
            "menu_text": "if you want more subtitles",
            ...
        }]
    },
    ...
]

