{% set cap = submenu | title %}

import { Component, OnDestroy, OnInit } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { {{ cap }}Service } from '../{{ submenu }}.service';

@Component({
  selector: 'app-{{ submenu }}-cu',
  templateUrl: '../pages/{{ submenu }}-cu.component.html'
})

export class {{ cap }}CuComponent implements OnInit {
  {{ submenu }}Id: string;
  action_type = 'Add';
  loading = false;
  loading_frm = true; // used to hide edit form while fetching
  {{ extra }}: any = {};
  errors: string;

  constructor(
    private {{ submenu }}Service: {{ cap }}Service,
    private route: ActivatedRoute,
    private router: Router) { }

    ngOnInit() {
      // console.log(this.route.snapshot.paramMap.get('id'));
      this.{{ submenu }}Id = this.route.snapshot.paramMap.get('id');
      if (this.{{ submenu }}Id) {
        // console.log('edit');
        this.action_type = 'Update';
        this.loading_frm = false;
        this.{{ submenu }}Service.get{{ extra| title  }}(this.{{ submenu }}Id)
          .subscribe( data => {
            this.loading_frm = true; // show edit form
            // console.log(data);
            this.{{ extra }} = data;
        });
      }
    }
  onSubmit(): void {
    this.loading = true;
    let myhttpService;
    // alert(this.action_type);
    if (this.action_type === 'Add') {
      myhttpService = this.{{ submenu }}Service.post{{extra| title }}(this.{{ extra }});
    } else if (this.action_type === 'Update') {
      myhttpService = this.{{ submenu }}Service.update{{extra| title }}(this.{{ submenu }}Id, this.{{ extra }});
    }

    myhttpService.subscribe((response) => {
      this.router.navigate(['/{{menu}}/{{ submenu }}/']);
    }, // success
      error => {
        // this.alertService.error(error);
        this.errors = error;
        this.loading = false;
        // console.log(error);
      }
    );    
  }

}
