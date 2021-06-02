import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { {{ menu|title }}Component } from './{{ menu }}.component';

const routes: Routes = [
    {
        path: '',
        component: {{ menu|title }}Component,
        children: [
            {% for submenu in submenus %}
            { path: '{{ submenu }}', loadChildren: () => import('./{{ submenu }}/{{ submenu }}.module').then((m) => m.{{ submenu|title }}Module)},{% endfor %}
        ]
    }
];

@NgModule({
    imports: [RouterModule.forChild(routes)],
    exports: [RouterModule]
})
export class {{ menu|title }}RoutingModule {}
