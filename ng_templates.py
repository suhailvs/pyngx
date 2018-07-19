################################### MAIN MENU #################################

COMPONENT_TEMPLATE = '''
import { Component, OnInit } from '@angular/core';

@Component({
    selector: 'app-${menu}',
    template: '<router-outlet></router-outlet>'
})
export class ${cmenu}Component implements OnInit {
    constructor() {}

    ngOnInit() {}
}

'''

MODULE_TEMPLATE = '''
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { DataTablesModule } from 'angular-datatables';

import { ${cmenu}RoutingModule } from './${menu}-routing.module';
import { ${cmenu}Component } from './${menu}.component';
@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    ${cmenu}RoutingModule,
    DataTablesModule
  ],
  declarations: [
    ${cmenu}Component
    ]
})
export class ${cmenu}Module { }

'''

ROUTING_TEMPLATE='''
import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { ${cmenu}Component } from './${menu}.component';

const routes: Routes = [
    {
        path: '',
        component: ${cmenu}Component,
        children: [
            { path: '', redirectTo: '${submenu}', pathMatch: 'prefix' },
            { path: '${submenu}', loadChildren: './${submenu}/${submenu}.module#${subcmenu}Module'}
        ]
    }
];

@NgModule({
    imports: [RouterModule.forChild(routes)],
    exports: [RouterModule]
})
export class ${cmenu}RoutingModule {}

'''
################################## SUB MENUS ####################################


# submenu-routing.module.ts
SUB_ROUTING_TEMPLATE = '''
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Routes, RouterModule } from '@angular/router';

import { ${subcmenu}Component } from './components/${submenu}.component';
import { ${subcmenu}CuComponent } from './components/${submenu}-cu.component';
import { ${subcmenu}ViewComponent } from './components/${submenu}-view.component';

const routes: Routes = [
  { path: '', component: ${subcmenu}Component },
  { path: 'add', component: ${subcmenu}CuComponent },
  { path: 'view/:id', component: ${subcmenu}ViewComponent },
  { path: 'edit/:id', component: ${subcmenu}CuComponent },
];

@NgModule({
  imports: [
    RouterModule.forChild(routes),
    CommonModule
  ],
  exports: [ RouterModule ],
  declarations: []
})
export class ${subcmenu}RoutingModule { }

'''

# submenu.module.ts
SUB_MODULE_TEMPLATE='''
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';

import { DataTablesModule } from 'angular-datatables';

import { ${subcmenu}RoutingModule } from './${submenu}-routing.module';

import { ${subcmenu}Component } from './components/${submenu}.component';
import { ${subcmenu}ViewComponent } from './components/${submenu}-view.component';
import { ${subcmenu}CuComponent } from './components/${submenu}-cu.component';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    ReactiveFormsModule,
    ${subcmenu}RoutingModule,
    DataTablesModule
  ],
  declarations: [
    ${subcmenu}Component,
    ${subcmenu}ViewComponent,
    ${subcmenu}CuComponent,
    ]
})
export class ${subcmenu}Module { }
'''


# submenu.service.ts
SUB_SERVICE_TEMPLATE = '''
import { Injectable } from '@angular/core';
import { HttpClient} from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class ${subcmenu}Service {

  constructor(private  httpClient:  HttpClient) {}

  get${subcmenu}s() {
    return this.httpClient.get('/${menu}/${submenu}/');
  }
  get${subcmenu}(id) {
    return this.httpClient.get(`/${menu}/${submenu}/${id}/`);
  }
  post${subcmenu}(${submenu}) {
    return this.httpClient.post('/${menu}/${submenu}/', ${submenu});
  }
  update${subcmenu}(id, ${submenu}) {
    return this.httpClient.patch(`/${menu}/${submenu}/${id}/`, ${submenu});
  }
}
'''

SUB_COMPONENT_TEMPLATE = '''
import { Component, OnDestroy, OnInit } from '@angular/core';
import { Subject } from 'rxjs';
import { ${subcmenu}Service } from '../${submenu}.service';

@Component({
  selector: 'app-${submenu}TODO',
  templateUrl: '../pages/${submenu}TODO.component.html'
})

export class ${subcmenu}TODOComponent implements OnInit {

  ngOnInit() {
  }

}
'''

SUB_HTML_PAGE = '''
<div class="row">
  <div class="col-md-12 col-sm-12 col-xs-12">
    <div class="x_panel">
      <div class="x_title">
        <h2>${subcmenu}</h2>

        <div class="clearfix"></div>
      </div>
      <div class="x_content">
          <img *ngIf="loading" src="https://upload.wikimedia.org/wikipedia/commons/b/b1/Loading_icon.gif" width="50">
fgdsgfdsfgfdsg dsfg df
                    <br>
      </div>
    </div>
  </div>
</div>

<!-- /page content -->
'''