{% set cap = submenu | title %}

import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { {{ cap }}Service } from '../{{ submenu }}.service';


@Component({
  selector: 'app-{{ submenu }}-view',
  templateUrl: '../pages/{{ submenu }}-view.component.html'
})

export class {{ cap }}ViewComponent implements OnInit {

  loading = false;
  {{ extra }}: any;

  constructor(
    private route: ActivatedRoute,
    private {{ submenu }}Service: {{ cap }}Service
  ) { }

  public get{{ extra|title }}() {
    this.loading = true;
    const id = this.route.snapshot.paramMap.get('id');
    this.{{submenu}}Service.get{{extra| title }}(id).subscribe((data: Array<object>) => {
      this.{{ extra }} = data;
      // console.log(this.student);
      this.loading = false;
    });
  }
  ngOnInit() {
    // https://blog.thoughtram.io/angular/2016/10/10/resolving-route-data-in-angular-2.html
    this.get{{extra|title}}();
  }
}

