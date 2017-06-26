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
var shared_service_js_1 = require("./shared.service.js");
var ngx_cookie_1 = require("ngx-cookie");
var auth_service_js_1 = require("./auth.service.js");
console.log(auth_service_js_1.AuthRes);
var AppComponent = (function () {
    function AppComponent(authRes, router, elm, _sharedService, _cookieService) {
        this.authRes = authRes;
        this.router = router;
        this._sharedService = _sharedService;
        this._cookieService = _cookieService;
        _sharedService.api_url = elm.nativeElement.getAttribute('api_url');
    }
    AppComponent.prototype.ngOnInit = function () {
        var _this = this;
        var me = this.authRes.query({ 'action': 'me' });
        me.$observable.subscribe(function (user) {
            _this.router.navigate(['/contact-list']);
        }, function (err) {
            _this.router.navigate(['/login']);
        });
        //this.userRes.post({'action':'login'}, (user:any) => {})
        // if(!this._cookieService.get('token')) {
        //     console.log('in redirect')
        //     this.router.navigate(['/login']);
        // }
        // else
        // {
        //     console.log('redirect to contact list')
        // }
    };
    return AppComponent;
}());
AppComponent = __decorate([
    core_1.Component({
        selector: 'my-app',
        template: "\n    <router-outlet></router-outlet>\n  ",
        styleUrls: ['./ng/src/app/app.component.css']
    }),
    __metadata("design:paramtypes", [auth_service_js_1.AuthRes, router_1.Router, core_1.ElementRef, shared_service_js_1.SharedService, ngx_cookie_1.CookieService])
], AppComponent);
exports.AppComponent = AppComponent;
//# sourceMappingURL=app.component.js.map