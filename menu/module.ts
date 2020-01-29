import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { {{ menu|title }}RoutingModule } from './{{ menu }}-routing.module';
import { {{ menu|title }}Component } from './{{ menu }}.component';
@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    {{ menu|title }}RoutingModule
  ],
  declarations: [
    {{ menu|title }}Component
    ]
})
export class {{ menu|title }}Module { }
