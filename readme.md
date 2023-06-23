##INFO###

Mydiabprod is a staged beta version of the support interface for diabetics.
Initial works were conducted in 2017 year.
Currently development is freezed due to the iUncas personal circumstances.
Service is written in Python and is modelled within Django framework. 
Service can be operated with Django Server as well as an independent Apache server relase.
Some components (jquery) are deprecated and must be updated.
Service includes module for loading results from glucometers in various formats, file uploader, event scheduler, google chart result analysis, simple table formatting, admin panel as well as the beta calendar connected to event scheduler.
Service includes personal blog written fully by dev iUncas - intending to be a part of the interface for comments and observations in the future.
Particular gui views are protected by the roles authorization - external provided by Django admin as well as the developed one.
Service utilizes currently MySQL engine and is adaptable in other engines - tested earlier with MSSQL DB.
Service tested in Ubuntu 16, 18, 20 Servers
Structure /mydiabprod/views.py
###VERSIONING###
February 2020, Version STAG_3

