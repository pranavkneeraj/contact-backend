import { NgModule }      from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule }   from '@angular/forms';
import { HttpModule }    from '@angular/http';

import { AppRoutingModule } from './app-routing.module.js';

// Imports for loading & configuring the in-memory web api
import { InMemoryWebApiModule } from 'angular-in-memory-web-api';
import { InMemoryDataService }  from './in-memory-data.service.js';

import { AppComponent }         from './app.component.js';
import { LoginComponent } from './login.component.js';
import { UpdateContactComponent } from './update-contact.component.js';
import { ContactListComponent }  from './contact-list.component.js';
import { ContactDetailsComponent } from './contact-details.component.js';
import { SharedService } from './shared.service.js';
import { AuthRes } from './auth.service.js';
import { ContentHeaderService } from './content.header.service.js';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MaterialModule } from '@angular/material';
import {MdIconModule} from '@angular/material';
import { ResourceModule } from 'ngx-resource';

import { CookieModule } from 'ngx-cookie';

@NgModule({
    imports: [
        BrowserModule,
        FormsModule,
        HttpModule,
        BrowserAnimationsModule,
        CookieModule.forRoot(),
        ResourceModule.forRoot(),
        AppRoutingModule,
        MaterialModule,
        MdIconModule
    ],
    declarations: [
        AppComponent,
        LoginComponent,
        UpdateContactComponent,
        ContactListComponent,
        ContactDetailsComponent,
    ],

    entryComponents: [
        UpdateContactComponent,
    ],
    providers: [ SharedService, AuthRes, ContentHeaderService],
    bootstrap: [ AppComponent ]
})
export class AppModule { }
