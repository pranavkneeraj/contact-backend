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
var material_1 = require("@angular/material");
var platform_browser_1 = require("@angular/platform-browser");
var ContactDetailsComponent = (function () {
    function ContactDetailsComponent(iconRegistry, sanitizer) {
        //    public isOpen:boolean;
        this.phoneTypes = [
            { value: 'work', viewValue: 'Work' },
            { value: 'home', viewValue: 'Home' },
            { value: 'personal', viewValue: 'Personal' },
            { value: 'custom', viewValue: 'Custom' },
        ];
        this.emailTypes = [
            { value: 'work', viewValue: 'Work' },
            { value: 'home', viewValue: 'Home' },
            { value: 'personal', viewValue: 'Personal' },
            { value: 'custom', viewValue: 'Custom' },
        ];
        this.phoneDetails = [''];
        this.emailDetails = [''];
        this.onClose = new core_1.EventEmitter();
        iconRegistry.addSvgIcon('thumbs-up', sanitizer.bypassSecurityTrustResourceUrl('assets/img/examples/thumbup-icon.svg'));
    }
    ContactDetailsComponent.prototype.addPhoneDetail = function () {
        console.log('adding phone');
        this.phoneDetails.push('');
    };
    ContactDetailsComponent.prototype.addEmailDetail = function () {
        this.emailDetails.push('');
    };
    ContactDetailsComponent.prototype.close = function (isOpen) {
        this.onClose.emit(isOpen);
    };
    return ContactDetailsComponent;
}());
__decorate([
    core_1.Output(),
    __metadata("design:type", Object)
], ContactDetailsComponent.prototype, "onClose", void 0);
ContactDetailsComponent = __decorate([
    core_1.Component({
        moduleId: module.id,
        selector: 'contact-details',
        templateUrl: './contact-details.component.html'
    }),
    __metadata("design:paramtypes", [material_1.MdIconRegistry, platform_browser_1.DomSanitizer])
], ContactDetailsComponent);
exports.ContactDetailsComponent = ContactDetailsComponent;
//# sourceMappingURL=contact-details.component.js.map