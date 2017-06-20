import { Component, OnInit } from '@angular/core';
import { MdDialog,MdDialogRef } from '@angular/material';
import { ContactDetailsComponent } from './contact-details.component.js';
import { UpdateContactComponent } from './update-contact.component.js';
import { DomSanitizer } from '@angular/platform-browser';


@Component({
    moduleId: module.id,
    selector: 'contact-list',
    templateUrl: './contact-list.component.html',

})

export class ContactListComponent implements OnInit {

    public isOpen: boolean = false;

    constructor(public dialog: MdDialog) {

    }

    ngOnInit() {

    }

    public openDialog() {
        let dialogRef =  this.dialog.open(UpdateContactComponent);

        dialogRef.afterClosed().subscribe(result => {
        });
    }

    public openForm() {
        this.isOpen = true;
    }

    onClose(isOpen: boolean) {
        this.isOpen = isOpen;
    }

}
