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
var core_1 = require("@angular/core");
var router_1 = require("@angular/router");
//import { Cookie } from 'ng2-cookies/ng2-cookies';
var auth_service_js_1 = require("./auth.service.js");
var Login = (function () {
    function Login() {
    }
    return Login;
}());
var LoginComponent = (function () {
    function LoginComponent(authRes, router) {
        this.authRes = authRes;
        this.router = router;
        this.login_response = false;
        this.credentials = new Login();
        this.has_error = false;
    }
    LoginComponent.prototype.login = function (credentials) {
        var _this = this;
        credentials['action'] = 'login';
        var login = this.authRes.save(credentials);
        login.$observable
            .subscribe(function (user) {
            _this.login_response = true;
            console.log("asdasd", user.token);
        }, function (err) {
            _this.login_response = true;
            console.log(err);
        });
    };
    ;
    LoginComponent.prototype.handleSuccess = function (response) {
        if (response) {
            this.router.navigate(['contact-list']);
        }
    };
    LoginComponent.prototype.logError = function (error) {
        this.error = error;
        this.has_error = true;
        this.login_response = false;
    };
    return LoginComponent;
}());
LoginComponent = __decorate([
    core_1.Component({
        moduleId: module.id,
        selector: 'log-in',
        templateUrl: './login.component.html'
    }),
    __metadata("design:paramtypes", [auth_service_js_1.AuthRes, router_1.Router])
], LoginComponent);
exports.LoginComponent = LoginComponent;
//# sourceMappingURL=login.component.js.map