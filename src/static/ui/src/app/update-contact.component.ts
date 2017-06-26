import { MdDialogRef } from '@angular/material';
import { Component, Output, EventEmitter } from '@angular/core';
import { MdDialogTitle, MdIconRegistry, MdDialogRef } from '@angular/material';
import {DomSanitizer} from '@angular/platform-browser';

@Component({
    selector: 'update-contact',
    templateUrl: './ng/src/app/update-contact.component.html',
})

export class UpdateContactComponent {

    phoneTypes = [
        {value: 'work', viewValue: 'Work'},
        {value: 'home', viewValue: 'Home'},
        {value: 'personal', viewValue: 'Personal'},
        {value: 'custom', viewValue: 'Custom'},
    ];

     emailTypes = [
        {value: 'work', viewValue: 'Work'},
        {value: 'home', viewValue: 'Home'},
        {value: 'personal', viewValue: 'Personal'},
        {value: 'custom', viewValue: 'Custom'},
     ];

    phoneDetails: Array<string> = ['']
    emailDetails: Array<string> = ['']

    @Output() onClose = new EventEmitter<boolean>();

    constructor(public dialogRef: MdDialogRef<UpdateContactComponent>, iconRegistry: MdIconRegistry, sanitizer: DomSanitizer) {
        iconRegistry.addSvgIcon(
            'thumbs-up',
            sanitizer.bypassSecurityTrustResourceUrl('assets/img/examples/thumbup-icon.svg'));
    }

    addPhoneDetail() {
        console.log("sadasdasdasdsad")
        this.phoneDetails.push('');
    }

    addEmailDetail() {
        this.emailDetails.push('');
    }

    close(isOpen: boolean) {
        this.onClose.emit(isOpen)
    }
}
