import { Injectable } from '@angular/core';
import { Router }  from '@angular/router';
import { Observable } from 'rxjs/Observable';
import { CookieService } from 'ngx-cookie';
import { Http, Response} from '@angular/http';
import { ContentHeaderService } from './content.header.service.js';
import { SharedService } from './shared.service.js';
import { ResourceCRUD, ResourceParams } from 'ngx-resource';

interface User {
    id?: number;
    first_name?: string;
    last_name?: string;
    username?: string;
    email?: string;
    //shard?: string;
    is_active?: boolean;
    is_superuser?: boolean;
}

interface IQuery {
    action?:string;
}
@Injectable()
@ResourceParams({
    url: 'api/auth/{action}',
    removeTrailingSlash:false
})
export class AuthRes extends ResourceCRUD<IQuery, any, any> {

}


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
        let username:string=credentials['username'];
        let password:string=credentials['password'];
        let body = JSON.stringify({ username, password });
        let options = this._contentHeaderService.getOptions(null);
        console.log(this._http);
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
            return true;
        }
    }

    private handleLoginError(err: Response) {
        console.log(err)
        let body = err.json();
        if (body.non_field_errors) {
            return Observable.throw(body.non_field_errors[0]);
        }else {
            return Observable.throw('Both fields are mandatory');
        }
    }
    private setUserData(res:Response) {
            this._sharedService.user=res.json() ;
            return res.json();
    }

    me():Observable<any> {
        let token = this._cookieService.get('token');
        //this._http._defaultOptions.headers.append('Authorization', 'token');
        return this._http.get(this._sharedService.api_url+'auth/me')
            .map((response:Response) => this.setUserData(response))
            .catch(this.handleLoginError);
    }

}
