import { Component, OnDestroy, OnInit } from '@angular/core';
import { Subject } from 'rxjs';
import { {{ submenu|title }}Service } from '../{{ submenu }}.service';

@Component({
  selector: 'app-{{ submenu }}TODO',
  templateUrl: '../pages/{{ submenu }}TODO.component.html'
})

export class {{ submenu|title }}TODOComponent implements OnInit {

  ngOnInit() {
  }

}