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
//import { Cookie } from 'ng2-cookies/ng2-cookies';
var auth_service_js_1 = require("./auth.service.js");
var Login = (function () {
    function Login() {
    }
    return Login;
}());
var LoginComponent = (function () {
    function LoginComponent(authService, router) {
        this.authService = authService;
        this.router = router;
        this.login_response = false;
        this.credentials = new Login();
        this.has_error = false;
    }
    LoginComponent.prototype.ngOnInit = function () {
        console.log('XXXXXX');
    };
    LoginComponent.prototype.login = function (credentials) {
        var _this = this;
        console.log('in login');
        this.login_response = true;
        this.authService.login(credentials)
            .subscribe(function (data) { return _this.handleSuccess(data); }, function (err) { return _this.logError(err); });
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
    __metadata("design:paramtypes", [auth_service_js_1.AuthService, router_1.Router])
], LoginComponent);
exports.LoginComponent = LoginComponent;
//# sourceMappingURL=login.component.js.map