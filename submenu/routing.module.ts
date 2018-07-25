import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Routes, RouterModule } from '@angular/router';

import { {{ submenu|title }}Component } from './components/{{ submenu }}.component';
import { {{ submenu|title }}CuComponent } from './components/{{ submenu }}-cu.component';
import { {{ submenu|title }}ViewComponent } from './components/{{ submenu }}-view.component';

const routes: Routes = [
  { path: '', component: {{ submenu|title }}Component },
  { path: 'add', component: {{ submenu|title }}CuComponent },
  { path: 'view/:id', component: {{ submenu|title }}ViewComponent },
  { path: 'edit/:id', component: {{ submenu|title }}CuComponent },
];

@NgModule({
  imports: [
    RouterModule.forChild(routes),
    CommonModule
  ],
  exports: [ RouterModule ],
  declarations: []
})
export class {{ submenu|title }}RoutingModule { }
