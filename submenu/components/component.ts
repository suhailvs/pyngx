import {Component} from '@angular/core';
import {TranslateService} from '@ngx-translate/core';

@Component({
  selector: 'app-{{ submenu }}',
  template: `
      <app-toolbar-datatable [model_name]="'dashboard__Users'" [user_type]="'BC'" [fields]="fields"></app-toolbar-datatable>`
})

export class {{ submenu|title }}Component {
  fields = [this.translate.instant('id'), this.translate.instant('First Name'), this.translate.instant('Username'), this.translate.instant('Email'), this.translate.instant('Status')];
  
  constructor(
    public translate: TranslateService) 
  { }
}

  