import { MdDialogRef } from '@angular/material';
import { Component } from '@angular/core';
import { MdDialogTitle } from '@angular/material';


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

    constructor(public dialogRef: MdDialogRef<UpdateContactComponent>) {

    }

    addPhoneDetail() {
        this.phoneDetails.push('');
    }

    addEmailDetail() {
        this.emailDetails.push('');
    }
}
