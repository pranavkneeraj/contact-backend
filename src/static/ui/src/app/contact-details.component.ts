import { Component, EventEmitter, Input, Output } from '@angular/core';
import { MdDialog,MdDialogRef, MdIconRegistry } from '@angular/material';
import {DomSanitizer} from '@angular/platform-browser';

@Component({
    moduleId: module.id,
    selector: 'contact-details',
    templateUrl: './contact-details.component.html'
})

export class ContactDetailsComponent {

//    public isOpen:boolean;

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

    constructor(iconRegistry: MdIconRegistry, sanitizer: DomSanitizer) {
        iconRegistry.addSvgIcon(
            'thumbs-up',
            sanitizer.bypassSecurityTrustResourceUrl('assets/img/examples/thumbup-icon.svg'));

    }

    addPhoneDetail() {
        this.phoneDetails.push('');
    }

    addEmailDetail() {
        this.emailDetails.push('');
    }

    close(isOpen: boolean) {
        this.onClose.emit(isOpen)
    }
}
