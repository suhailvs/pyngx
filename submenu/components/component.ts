import { Component, OnDestroy, OnInit } from '@angular/core';
import { Subject } from 'rxjs';
import { {{ submenu|title }}Service } from '../{{ submenu }}.service';

@Component({
  selector: 'app-{{ submenu }}',
  templateUrl: '../pages/{{ submenu }}.component.html'
})

export class {{ submenu|title }}Component implements OnDestroy, OnInit {

  dtOptions: DataTables.Settings = {};
  dtTrigger: Subject<any> = new Subject();
  private {{extra}}s:  Array<object> = [];
  loading = false;

  constructor(private {{submenu}}Service:  {{ submenu|title }}Service) { }

  ngOnInit() {
  	this.dtOptions = {
      pagingType: 'full_numbers',
      pageLength: 10
    };

    this.get{{ extra|title }}s();
  }

  public get{{ extra|title }}s() {
    this.loading = true;
    this.{{submenu}}Service.get{{ extra|title }}s().subscribe((data:  Array<object>) => {
      this.{{extra}}s  =  data;
      // Calling the DT trigger to manually render the table
      // console.log(data);
      this.dtTrigger.next();
      // console.log(data);
      this.loading = false;
    });
  }

  ngOnDestroy(): void {
      // Do not forget to unsubscribe the event
      this.dtTrigger.unsubscribe();
  }

}
