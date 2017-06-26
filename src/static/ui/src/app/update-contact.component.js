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
var material_1 = require("@angular/material");
var core_1 = require("@angular/core");
var material_2 = require("@angular/material");
var platform_browser_1 = require("@angular/platform-browser");
var UpdateContactComponent = (function () {
    function UpdateContactComponent(dialogRef, iconRegistry, sanitizer) {
        this.dialogRef = dialogRef;
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
    UpdateContactComponent.prototype.addPhoneDetail = function () {
        console.log("sadasdasdasdsad");
        this.phoneDetails.push('');
    };
    UpdateContactComponent.prototype.addEmailDetail = function () {
        this.emailDetails.push('');
    };
    UpdateContactComponent.prototype.close = function (isOpen) {
        this.onClose.emit(isOpen);
    };
    return UpdateContactComponent;
}());
__decorate([
    core_1.Output(),
    __metadata("design:type", Object)
], UpdateContactComponent.prototype, "onClose", void 0);
UpdateContactComponent = __decorate([
    core_1.Component({
        selector: 'update-contact',
        templateUrl: './ng/src/app/update-contact.component.html',
    }),
    __metadata("design:paramtypes", [material_1.MdDialogRef, material_2.MdIconRegistry, platform_browser_1.DomSanitizer])
], UpdateContactComponent);
exports.UpdateContactComponent = UpdateContactComponent;
//# sourceMappingURL=update-contact.component.js.map