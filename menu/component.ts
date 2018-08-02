import { Component, OnInit } from '@angular/core';

@Component({
    selector: 'app-{{ menu }}',
    template: '<router-outlet></router-outlet>'
})
export class {{ menu|title }}Component implements OnInit {
    constructor() {}

    ngOnInit() {}
}
