import { Component, OnDestroy, OnInit } from '@angular/core';
import { Subject } from 'rxjs';
import { {{ submenu|title }}Service } from '../{{ submenu }}.service';

@Component({
  selector: 'app-{{ submenu }}{% if extra %}-{{extra}}{% endif %}',
  templateUrl: '../pages/{{ submenu }}{% if extra %}-{{extra}}{% endif %}.component.html'
})

export class {{ submenu|title }}{{extra|title}}Component implements OnInit {

  ngOnInit() {
  }

}
