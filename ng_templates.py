################################### MAIN MENU #################################

COMPONENT_TEMPLATE = '''
import { Component, OnInit } from '@angular/core';

@Component({
    selector: 'app-$name',
    template: '<router-outlet></router-outlet>'
})
export class ${cname}Component implements OnInit {
    constructor() {}

    ngOnInit() {}
}

'''

MODULE_TEMPLATE = '''
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { DataTablesModule } from 'angular-datatables';

import { ${cname}RoutingModule } from './${name}-routing.module';
import { ${cname}Component } from './${name}.component';
@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    ${cname}RoutingModule,
    DataTablesModule
  ],
  declarations: [
    ${cname}Component
    ]
})
export class ${cname}Module { }

'''

ROUTING_TEMPLATE='''
import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { ${cname}Component } from './${name}.component';

const routes: Routes = [
    {
        path: '',
        component: ${cname}Component,
        children: [
            // { path: '', redirectTo: 'student', pathMatch: 'prefix' },
            // { path: 'student', loadChildren: './student/student.module#StudentModule'}
        ]
    }
];

@NgModule({
    imports: [RouterModule.forChild(routes)],
    exports: [RouterModule]
})
export class ${cname}RoutingModule {}

'''
################################## SUB MENUS ####################################


# submenu-routing.module.ts
SUB_ROUTING_TEMPLATE = '''
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Routes, RouterModule } from '@angular/router';

import { ${cname}Component } from './components/${name}.component';
import { ${cname}CuComponent } from './components/${name}-cu.component';
import { ${cname}ViewComponent } from './components/${name}-view.component';

const routes: Routes = [
  { path: '', component: ${cname}Component },
  { path: 'add', component: ${cname}CuComponent },
  { path: 'view/:id', component: ${cname}ViewComponent },
  { path: 'edit/:id', component: ${cname}CuComponent },
];

@NgModule({
  imports: [
    RouterModule.forChild(routes),
    CommonModule
  ],
  exports: [ RouterModule ],
  declarations: []
})
export class ${cname}RoutingModule { }

'''

# submenu.module.ts
SUB_MODULE_TEMPLATE='''
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';

import { DataTablesModule } from 'angular-datatables';

import { ${cname}RoutingModule } from './${name}-routing.module';

import { ${cname}Component } from './components/${name}.component';
import { ${cname}ViewComponent } from './components/${name}-view.component';
import { ${cname}CuComponent } from './components/${name}-cu.component';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    ReactiveFormsModule,
    ${cname}RoutingModule,
    DataTablesModule
  ],
  declarations: [
    ${cname}Component,
    ${cname}ViewComponent,
    ${cname}CuComponent,
    ]
})
export class ${cname}Module { }
'''


# submenu.service.ts
SUB_SERVICE_TEMPLATE = '''
import { Injectable } from '@angular/core';
import { HttpClient} from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class ${cname}Service {

  constructor(private  httpClient:  HttpClient) {}

  get${cname}() {
    return this.httpClient.get('/students/studentcategory/');
  }
  get${cname}(id) {
    return this.httpClient.get(`/students/studentcategory/${id}/`);
  }
  post${cname}(studentcat) {
    return this.httpClient.post('/students/studentcategory/', studentcat);
  }
  update${cname}(id, studentcat) {
    return this.httpClient.patch(`/students/studentcategory/${id}/`, studentcat);
  }
}
'''

SUB_COMPONENT_TEMPLATE = '''
import { Component, OnDestroy, OnInit } from '@angular/core';
import { Subject } from 'rxjs';
import { StudentCategoryService } from '../student-category.service';

@Component({
  selector: 'app-student-category',
  templateUrl: '../pages/student-category.component.html'
})

export class StudentCategoryComponent implements OnInit {

  ngOnInit() {
  }

}
'''

SUB_HTML_PAGE = '''
<div class="row">
  <div class="col-md-12 col-sm-12 col-xs-12">
    <div class="x_panel">
      <div class="x_title">
        <h2>Student Category</h2>

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