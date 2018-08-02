import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { {{ menu|title }}Component } from './{{ menu }}.component';

const routes: Routes = [
    {
        path: '',
        component: {{ menu|title }}Component,
        children: [
            // { path: '', redirectTo: '{{ submenu }}', pathMatch: 'prefix' },
            {% for submenu in submenus %}
            { path: '{{ submenu }}', loadChildren: './{{ submenu }}/{{ submenu }}.module#{{ submenu|title }}Module'},{% endfor %}
        ]
    }
];

@NgModule({
    imports: [RouterModule.forChild(routes)],
    exports: [RouterModule]
})
export class {{ menu|title }}RoutingModule {}
