import {Component} from '@angular/core';
import {TranslateService} from '@ngx-translate/core';

@Component({
  selector: 'app-{{ submenu }}',
  template: `
      <app-toolbar-datatable [model_name]="'{{menu}}__{{ submenu|title }}'" [fields]="fields"></app-toolbar-datatable>`
})

export class {{ submenu|title }}Component {
  fields = [this.translate.instant('id'), this.translate.instant('Status')];
  
  constructor(
    public translate: TranslateService) 
  { }
}

