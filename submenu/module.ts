import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';

import { MatInputModule } from '@angular/material/input';
import { MatSelectModule } from '@angular/material/select';

import {SharedModule} from '../../../shared/shared.module';
import {TranslateModule} from '@ngx-translate/core';

import { {{ submenu|title }}RoutingModule } from './{{ submenu }}-routing.module';

import { {{ submenu|title }}Component } from './components/{{ submenu }}.component';
import { {{ submenu|title }}CuComponent } from './components/{{ submenu }}-cu.component';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    ReactiveFormsModule,
    MatInputModule,
    MatSelectModule,
    TranslateModule,
    SharedModule,

    {{ submenu|title }}RoutingModule,
  ],
  declarations: [
    {{ submenu|title }}Component,
    {{ submenu|title }}CuComponent,
    ]
})
export class {{ submenu|title }}Module { }
