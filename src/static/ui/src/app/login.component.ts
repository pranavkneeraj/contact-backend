import { Component , OnInit } from '@angular/core';
import { Router } from '@angular/router';
//import { Cookie } from 'ng2-cookies/ng2-cookies';
import { AuthRes } from './auth.service.js';

class Login {
    username:string;
    password:string;
}

@Component({
    moduleId: module.id,
    selector: 'log-in',
    templateUrl: './login.component.html'
})
export class LoginComponent  {
    error:string;
    has_error:boolean;
    login_response:boolean = false;
    private credentials:Login;

    constructor(private authRes:AuthRes, private router: Router) {
        this.credentials = new Login();
        this.has_error = false;
    }

    login(credentials:Login): void {
        credentials['action'] = 'login';
        let login = this.authRes.save(credentials);
        login.$observable
            .subscribe((user:any) => {
                this.login_response = true;

                console.log("asdasd",user.token);
            }, (err:any) => {
                this.login_response = true;
                console.log(err);
            })
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
