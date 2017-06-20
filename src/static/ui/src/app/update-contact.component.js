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
var material_1 = require("@angular/material");
var core_1 = require("@angular/core");
var UpdateContactComponent = (function () {
    function UpdateContactComponent(dialogRef) {
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
    }
    UpdateContactComponent.prototype.addPhoneDetail = function () {
        this.phoneDetails.push('');
    };
    UpdateContactComponent.prototype.addEmailDetail = function () {
        this.emailDetails.push('');
    };
    return UpdateContactComponent;
}());
UpdateContactComponent = __decorate([
    core_1.Component({
        selector: 'update-contact',
        templateUrl: './ng/src/app/update-contact.component.html',
    }),
    __metadata("design:paramtypes", [material_1.MdDialogRef])
], UpdateContactComponent);
exports.UpdateContactComponent = UpdateContactComponent;
//# sourceMappingURL=update-contact.component.js.map