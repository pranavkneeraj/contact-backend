import { Injectable } from '@angular/core';
import { Router }  from '@angular/router';
import { Observable } from 'rxjs/Observable';
import { CookieService } from 'ngx-cookie';
import { Http, Response} from '@angular/http';
import { ContentHeaderService } from './content.header.service.js';
import { SharedService } from './shared.service.js';

@Injectable()
export class AuthService {

    public invalidCredentials:boolean = false;

    constructor(private _http: Http,
                private _router: Router,
                private _cookieService:CookieService,
                private _contentHeaderService:ContentHeaderService,
                private _sharedService: SharedService
               ) {
    }


    login(credentials:any): Observable<any> {
        console.log('in service');
        let username:string=credentials['username'];
        let password:string=credentials['password'];
        let body = JSON.stringify({ username, password });
        let options = this._contentHeaderService.getOptions(null);
        console.log(this._http)
        return this._http.post(this._sharedService.api_url+'auth/login', body, options)
            .map((response:Response) => this.handleLoginResponse(response))
            .catch(this.handleLoginError);
    }

    private handleLoginResponse(res:Response) {
        console.log(res)
        let body = res.json();
        if(body.token===undefined || body.token===null) {
            this._router.navigate(['/login']);
            return false;
        } else {
            this._cookieService.put('token', body.token);
            this._router.navigate(['']);
            this.invalidCredentials = false; // set here coz its value remains true after perform logout and
            //needs to be false after the login
            return true;
        }
    }

    private handleLoginError(err: Response) {
        let body = err.json();
        if (body.non_field_errors) {
            return Observable.throw(body.non_field_errors[0]);
        }else {
            return Observable.throw('Both fields are mandatory');
        }
    }

}
