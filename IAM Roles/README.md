# AMAZON IAM ROLES


An IAM role is an AWS identity with permission policies that determine what the identity can and cannot do in AWS. 
IAM roles allow you to access your data from Databricks clusters without having to embed your AWS keys in notebooks.
In order to access AWS resources securely, you can launch Databricks clusters with IAM roles


## What is IAM(Identity And Access Management)


Identity and Access Management (IAM) manages Amazon Web Services (AWS) users and their access to AWS accounts and services. It controls the level of access a user can have over an AWS account & set users, grant permission and allows a user to use different features of AWS account. Identity and access management is mostly used to manage users, groups, roles and Access polices.


The account we created to sign in Amazon web services is knows as root account and it holds all the administrative rights and has access to all parts of the account. The new user created in AWS account, by default they have no access to any services in the account & it is done with the help of IAM that the root account holder can implement access polices and grant permission to the user to access certain services.


## Features of IAM:

1. **Shared Access to your Account:** A team of people who are working for a project together can easily share resources with the help of the shared access feature.


2. **Free of cost:** IAM feature of Aws account is free to use & charges are added only when you access other Amazon web services using IAM user.


3. **Have Centralized control over your Aws account:** Any new creation of user, groups or any form of cancellation that takes places in Aws account is controlled by you and have the control over what & how data can be accessed by the user.
Grant permission to the user: As root account holds of the administrative rights, user will be granted permission to Access certain services by IAM.


4. **Multifactor Authentication:** Additional layer of security implemented on your account by third party, a six digit number which you have to put along with your password when you log into your accounts.
