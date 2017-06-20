"use strict";
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};
Object.defineProperty(exports, "__esModule", { value: true });
var core_1 = require("@angular/core");
var router_1 = require("@angular/router");
var Observable_1 = require("rxjs/Observable");
var ngx_cookie_1 = require("ngx-cookie");
var http_1 = require("@angular/http");
var content_header_service_js_1 = require("./content.header.service.js");
var shared_service_js_1 = require("./shared.service.js");
var AuthService = (function () {
    function AuthService(_http, _router, _cookieService, _contentHeaderService, _sharedService) {
        this._http = _http;
        this._router = _router;
        this._cookieService = _cookieService;
        this._contentHeaderService = _contentHeaderService;
        this._sharedService = _sharedService;
        this.invalidCredentials = false;
    }
    AuthService.prototype.login = function (credentials) {
        var _this = this;
        console.log('in service');
        var username = credentials['username'];
        var password = credentials['password'];
        var body = JSON.stringify({ username: username, password: password });
        var options = this._contentHeaderService.getOptions(null);
        console.log(this._http);
        return this._http.post(this._sharedService.api_url + 'auth/login', body, options)
            .map(function (response) { return _this.handleLoginResponse(response); })
            .catch(this.handleLoginError);
    };
    AuthService.prototype.handleLoginResponse = function (res) {
        console.log(res);
        var body = res.json();
        if (body.token === undefined || body.token === null) {
            this._router.navigate(['/login']);
            return false;
        }
        else {
            this._cookieService.put('token', body.token);
            this._router.navigate(['']);
            this.invalidCredentials = false; // set here coz its value remains true after perform logout and
            //needs to be false after the login
            return true;
        }
    };
    AuthService.prototype.handleLoginError = function (err) {
        var body = err.json();
        if (body.non_field_errors) {
            return Observable_1.Observable.throw(body.non_field_errors[0]);
        }
        else {
            return Observable_1.Observable.throw('Both fields are mandatory');
        }
    };
    return AuthService;
}());
AuthService = __decorate([
    core_1.Injectable(),
    __metadata("design:paramtypes", [http_1.Http,
        router_1.Router,
        ngx_cookie_1.CookieService,
        content_header_service_js_1.ContentHeaderService,
        shared_service_js_1.SharedService])
], AuthService);
exports.AuthService = AuthService;
//# sourceMappingURL=auth.service.js.map