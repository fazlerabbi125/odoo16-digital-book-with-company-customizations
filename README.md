
# Employee Digital Book

## About The Module

Once this custom module is installed, select `Employee Digital Books` from the main menu. It will be redirected to the tree view of the module. From the configuration menu, it is possible to create different `document types` for upload such as Word, Excel, PDF etc and this will be used to validate the file uploaded for the digital book. It is also possible to create different `categories` of the documents such as  resumes, appointment letters, employment contracts, NDA, resumes, certificates, NID, release letters, experience certificates,reference checking forms, increment, promotion Letters, Memo etc.

This module has dependency with the `hr.employee` module. As each document needs to be stored against an employee.

From the `Employee Digital Books` menu, it is possible to store documents with different categories, document types and employees. CRUD operations can be performed if user has the appropriate permission.

## Access Control

There are 3 types of users in this module.

- <b>Administrator</b>: Has full access to the ERP. They can create users and give them proper access level.

- <b>User</b>:  Cannot see this module in the main menu and it will show access error if try to visit the pages of this module via URL. 

- <b>Officer</b>: Has full access to this module.

Access level can be set by selecting the appropriate option from the Employee dropdown in the HR section of the User form in the Settings module. For example, to set the access to `User`, you have to leave the Employee dropdown empty.

## Document Export and Printing

- Digital book records can be exported from the tree view and attachments can downloaded from the form view.


## Searching and Grouping
- Digital books can be searched using different criteria such as `employee name`, `document title`,`file name` ,`document type`, and `category` .
- Digital books can be grouped by `document type` and `category`. 
