It is a Job Scheduling Application using Django Framework.

Project  Overview:
----------------
You need to create a Web application having 3 pages called - Contractor, Companies, Installation Jobs. On the contractor
page you should be able to create, edit and delete contractors. On the companies page, you should be able to create, edit and
delete a company’s details. On the installation jobs page, you should be able to create a job with an installation job id and
installation job title and you should be able to assign a company to that installation job using a drop down that shows all
companies and assign a contractor using a second drop down which has the list of all the contractors and schedule for a
date and time. The application needs to communicate with a database and store information in the respective databases for
respective entities like Contractor, Companies, Installation Jobs. Finally, after creating the application and database you need
to host the application using Heroku.
Stage 1:
--------
1. Create a CRUD (Create, Read, Update, Delete) application for 2 pages - Contractor, Companies
2. On Contractor page create 4 text boxes to enter the id for contractor, name of the contractor, city of the contractor, zip
code and a submit button next to it
3. On Company page create 4 text boxes to enter the id for company, name of the company, city of the company, zip code
and a submit button next to it
4. The submit button should add the respective information into the database
5. Create a simple user interface on each page to view the information that was added. You can use a simple table if
needed or just plain paragraph tags also will do as long as there is a way to view the information on the page.
6. Create edit button and delete button next to each saved entry on both the pages to be able to edit and delete the added
entry
Stage 2:
-------
1. Create the Installation Jobs page
2. The page should include the following - Create a textbox to enter installation job id, a textbox to enter installation job
title,a textbox to enter installation job price, a dropdown to select the company from the list of companies that you have
added in the company page, a drop down too select a contractor that were added on the contractor page, an input field
to add a date for the job, an input field to add time for the job in the 24hr format (e.g 8am would be input as 08:00, 4pm
would be input as 16:00), submit button to add a new job
3. After adding an installation job and saving it, it should show in a list form with all the details. In that list you should have
edit and delete buttons to modify existing data and delete data