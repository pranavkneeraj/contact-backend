import { Component , OnInit, ElementRef } from '@angular/core';
import { Router } from '@angular/router';
import { AppRoutingModule } from'./app-routing.module.js';
import { SharedService } from './shared.service.js';
import { CookieService } from 'ngx-cookie';

@Component({
  selector: 'my-app',
  template: `
    <router-outlet></router-outlet>
  `,
  styleUrls: ['./ng/src/app/app.component.css']
})

export class AppComponent implements OnInit {

    constructor(private router: Router, elm: ElementRef, private _sharedService:SharedService, private _cookieService:CookieService) {
        _sharedService.api_url = elm.nativeElement.getAttribute('api_url');
    }

    ngOnInit() {
        if(!this._cookieService.get('token')) {
            console.log('in redirect')
            this.router.navigate(['/login']);
        }
        else
        {
            console.log('redirect to contact list')
            this.router.navigate(['/contact-list']);
        }

    }
}
