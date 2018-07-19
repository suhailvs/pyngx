import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { {{ menu|title }}Component } from './{{ menu }}.component';

const routes: Routes = [
    {
        path: '',
        component: {{ menu|title }}Component,
        children: [
            { path: '', redirectTo: '{{ submenu }}', pathMatch: 'prefix' },
            { path: '{{ submenu }}', loadChildren: './{{ submenu }}/{{ submenu }}.module#{{ submenu|title }}Module'}
        ]
    }
];

@NgModule({
    imports: [RouterModule.forChild(routes)],
    exports: [RouterModule]
})
export class {{ menu|title }}RoutingModule {}
