import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';

import { DataTablesModule } from 'angular-datatables';

import { {{ submenu|title }}RoutingModule } from './{{ submenu }}-routing.module';

import { {{ submenu|title }}Component } from './components/{{ submenu }}.component';
import { {{ submenu|title }}ViewComponent } from './components/{{ submenu }}-view.component';
import { {{ submenu|title }}CuComponent } from './components/{{ submenu }}-cu.component';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    ReactiveFormsModule,
    {{ submenu|title }}RoutingModule,
    DataTablesModule
  ],
  declarations: [
    {{ submenu|title }}Component,
    {{ submenu|title }}ViewComponent,
    {{ submenu|title }}CuComponent,
    ]
})
export class {{ submenu|title }}Module { }