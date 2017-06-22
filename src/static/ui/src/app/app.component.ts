import { Component , OnInit, ElementRef } from '@angular/core';
import { Router } from '@angular/router';
import { AppRoutingModule } from'./app-routing.module.js';
import { SharedService } from './shared.service.js';
import { CookieService } from 'ngx-cookie';
import { AuthRes } from './auth.service.js'
import { AuthService } from './auth.service.js'
@Component({
  selector: 'my-app',
  template: `
    <span *ngIf="_sharedService.user"> <h1>{{_sharedService.user.username}}</h1> </span>

    <router-outlet></router-outlet>
    <span *ngIf="_sharedService.user"> <h1>{{_sharedService.user.shard  }}</h1> </span>
  `,
  styleUrls: ['./ng/src/app/app.component.css']
})
export class AppComponent implements OnInit {
    constructor(private authRes: AuthRes, private router: Router, elm: ElementRef, private _sharedService:SharedService, private _cookieService:CookieService) {
        _sharedService.api_url = elm.nativeElement.getAttribute('api_url');
    }

    ngOnInit() {
        let me=this.authRes.query({'action':'me'});
        me.$observable.subscribe((user: any) => {
            this.router.navigate(['/contact-list']);
        }, (err: any) => {
             this.router.navigate(['/login']);
        })
        //this.userRes.post({'action':'login'}, (user:any) => {})


        // if(!this._cookieService.get('token')) {
        //     console.log('in redirect')
        //     this.router.navigate(['/login']);
        // }
        // else
        // {
        //     console.log('redirect to contact list')

        // }

    }
}
