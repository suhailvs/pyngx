{% set cap = submenu | title %}
import { Component, OnDestroy, OnInit } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import {FormArray, FormBuilder, Validators} from '@angular/forms';
import {TranslateService} from '@ngx-translate/core';
import {ToastrService} from 'ngx-toastr';
import * as moment from 'moment';
import { MustMatch } from '../../../dashboard/users/components/equal-validator';
import { {{ cap }}Service } from '../{{ submenu }}.service';

@Component({
  selector: 'app-{{ submenu }}-cu',
  templateUrl: '../pages/{{ submenu }}-cu.component.html'
})

export class {{ cap }}CuComponent implements OnInit {

  {{ submenu }}Form = this.fb.group({
    id: [''],
    username: ['', [Validators.required, Validators.pattern('(?=[a-zA-Z0-9._]{6,20}$)(?!.*[_.]{2})[^_.].*[^_.]')]],
    first_name: ['', Validators.required],
    middle_name: [''],
    last_name: ['', Validators.required],
    email: ['', Validators.required],
    password: [''],
    confirm_password: [''],
    // user_type: ['TC'],
    title: [''],
    gender: ['M', Validators.required],
    dob: [''],
    photo: [''],
    status: [1, Validators.required]
  },{
      validator: MustMatch('password', 'confirm_password')
  });


  profilepic = '';
  submitted = false;
  actionType = 'Save';
  // progress =0;
  errors: string;
  
  constructor(
    private {{ submenu }}Service: {{ cap }}Service,
    public translate: TranslateService,
    private route: ActivatedRoute,
    private toastr: ToastrService,
    private fb: FormBuilder,
    private router: Router) { }

    
  get f() {
    return this.{{ submenu }}Form.controls;
  }  



  ngOnInit() {
    const user_id = this.route.snapshot.paramMap.get('id');
    if (user_id) {
      this.actionType = 'Update';
      this.{{ submenu }}Service.get{{ extra| title  }}(user_id)
        .subscribe( data => {
          this.{{ submenu }}Form.patchValue({
            id: data['user']['id'],
            username: data['user']['username'],
            first_name: data['user']['first_name'],
            middle_name: data['user']['middle_name'],
            last_name: data['user']['last_name'],
            email: data['user']['email'],
            status: data['user']['status'],
          })
          if (Object.keys(data['userprofile']).length != 0) {
            this.{{ submenu }}Form.patchValue({
              title: data['userprofile']['title'] ? data['userprofile']['title']:'',
              gender: data['userprofile']['gender'],
              dob: data['userprofile']['dob'] ? data['userprofile']['dob']:'',
              photo: ''
            })
            
            this.profilepic = data['userprofile']['photo'];
          }
      });

    }
  }

  toFormData<T>( formValue: T ) {
    const formData = new FormData();

    for ( const key of Object.keys(formValue) ) {
      const value = formValue[key];
      formData.append(key, value);
    }

    return formData;
  }

  onSubmit() {
    this.submitted = true;
    if (this.{{ submenu }}Form.invalid) {
      return;
    }
    
    let dob = this.{{ submenu }}Form.value['dob'];
    if (dob) {dob=moment(dob, 'YYYY-MM-DD').format('YYYY-MM-DD')} else {dob = ''}
    this.{{ submenu }}Form.patchValue({
        dob: dob
    });
    let myhttpService;
     
    if (this.actionType === 'Save') {
      delete this.{{ extra }}Form.value.id;
      myhttpService = this.{{ submenu }}Service.post{{extra| title }}(this.toFormData(this.{{ extra }}Form.value));
    } else if (this.actionType === 'Update') {
      myhttpService = this.{{ submenu }}Service.update{{extra| title }}(this.toFormData(this.{{ extra }}Form.value));
    }
    
    myhttpService.subscribe((response) => {
      this.router.navigate(['/{{menu}}/{{ submenu }}/']);
    }, // success
      error => {
        this.errors = error;
        Object.keys(error.error).forEach((key,index)=>this.toastr.error(error.error[key][0],key));
      }
    );

  }


}
