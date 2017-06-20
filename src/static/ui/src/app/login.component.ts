import { Component , OnInit } from '@angular/core';
import { Router } from '@angular/router';
//import { Cookie } from 'ng2-cookies/ng2-cookies';
import { AuthService } from './auth.service.js';

class Login {
    username:string;
    password:string;
}

@Component({
    moduleId: module.id,
    selector: 'log-in',
    templateUrl: './login.component.html'
})
export class LoginComponent implements OnInit {
    error:string;
    has_error:boolean;
    login_response:boolean = false;
    private credentials:Login;


    constructor(private authService: AuthService, private router: Router) {
        this.credentials = new Login();
        this.has_error = false;
    }

    ngOnInit() {
        console.log('XXXXXX');
    }

    login(credentials:Login): void {
        console.log('in login')
        this.login_response = true;
        this.authService.login(credentials)
            .subscribe(
                data => this.handleSuccess(data),
                err => this.logError(err)
            );
    };

    handleSuccess(response:any) {
        if(response) {
            this.router.navigate(['contact-list']);
        }
    }

    logError(error:any) {
        this.error = error;
        this.has_error = true;
        this.login_response= false;
    }

}
