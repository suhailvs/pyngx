{% set cap = submenu | title %}
import { Component, OnDestroy, OnInit } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import {FormArray, FormBuilder, Validators} from '@angular/forms';
import {TranslateService} from '@ngx-translate/core';

import { {{ cap }}Service } from '../{{ submenu }}.service';

@Component({
  selector: 'app-{{ submenu }}-cu',
  templateUrl: '../pages/{{ submenu }}-cu.component.html'
})


export class {{ cap }}CuComponent implements OnInit {

  {{ submenu }}Form = this.fb.group({
    id: [''],
    status: [1, Validators.required]
  });

  {{ submenu }}Id: string;
  submitted = false;
  actionType = 'Add';

  errors: string;

  constructor(
    private {{ submenu }}Service: {{ cap }}Service,
    public translate: TranslateService,
    private route: ActivatedRoute,
    private fb: FormBuilder,
    private router: Router) { }

    
  get f() {
    return this.{{ submenu }}Form.controls;
  }  

  ngOnInit() {
    // console.log(this.route.snapshot.paramMap.get('id'));
    this.{{ submenu }}Id = this.route.snapshot.paramMap.get('id');
    if (this.{{ submenu }}Id) {
      // console.log('edit');
      this.actionType = 'Update';
      this.{{ submenu }}Service.get{{ extra| title  }}(this.{{ submenu }}Id)
        .subscribe( data => {
          this.{{ submenu }}Form.patchValue({
            id: data['id'],
            status: data['status']
          })
      });
    }
  }

  onSubmit() {
    this.submitted = true;
    if (this.{{ submenu }}Form.invalid) {
      return;
    }
    let myhttpService;
    // alert(this.actionType);
    if (this.actionType === 'Add') {
      myhttpService = this.{{ submenu }}Service.post{{extra| title }}(this.{{ extra }}Form.value);
    } else if (this.actionType === 'Update') {
      myhttpService = this.{{ submenu }}Service.update{{extra| title }}(this.{{ submenu }}Id, this.{{ extra }}Form.value);
    }

    myhttpService.subscribe((response) => {
      this.router.navigate(['/{{menu}}/{{ submenu }}/']);
    }, // success
      error => {
        this.errors = error;
      }
    );
  }
}
