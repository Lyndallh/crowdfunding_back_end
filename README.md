# crowdfunding_back_end
Shecodes Project Description: Kickstarter, Go Fund Me, Kiva, Change.org, Patreon... All of these different websiteshave something in common: they provide a platform for people to fund projects that they believe in, but they all have a slightly different approach. You are going to create your own crowdfunding website, and put your own spin on it!

# Equipme

EquipMe is a crowdfundinng platform focused on connecting generous donors willing to provide financial support with individuals in need of essential equipment. This streamlined platform is designed to empower users facing financial constraints to articulate their specific equipment requirements, spanning medical devices, educational tools, and more. With a user-friendly interface, EquipMe simplifies the process of securing financial pledges, ensuring that those seeking assistance can receive the financial support they need to acquire the necessary equipment. Join us on EquipMe as we create a community committed to making impactful financial pledges that directly contribute to fulfilling equipment requests and improving lives.

Potential donors: Private enterprise, philanthropists and the general public

## MVP Features

### User Accounts

- [X] Username
- [X] Email Address
- [X] Password

### Project MVP

- [X] Create a project
  - [X] Title
  - [X] Owner (a user)
  - [X] Description
  - [X] Image
  - [X] Target Amount to fundraise
  - [X] Whether it is currently open to accepting new supporters or not
  - [X] When was the project created
- [X] Ability to pledge to a project
  - [X] An amount
  - [X] The project the pledge is for
  - [X] The supporter /user (i.e. who created the pledge)
  - [X] Whether the pledge is anonymous
  - [X] A comment to go with the pledge

- [x] Implement suitable update/delete functionality, e.g. should a project owner be allowed to update a project description?
- [x] Implement suitable permissions
- [x] Return the relevant status codes for both successful and unsuccessful requests to the API.

- [ ] Handle failed requests gracefully (e.g. you should have a custom 404 page rather than the default error page).**future feature in REACT project*
- [x] Use Token Authentication.
- [ ] Implement responsive design. **future feature in REACT project*

## Additional features
- [x] Autopopulate date created (timestamp) for projects, this does not update on when updating a project
- [x] Implement a date modified feild that autopopulates (timestamp) when updating a project
- [x] Implement a date created feild for pledges
- [x] Autopopulate date created (timestamp) for pledges, this does not update on when updating a project

## Part A Submission

Deployed API project: https://crowdfunding-back-end-equipme.fly.dev

### Insomnia Screenshots
#### GET Success
![A screenshot of Insomnia, demonstrating a successful GET method for any endpoint.](images/GET_success.png)
#### POST Success
![A screenshot of Insomnia, demonstrating a successful POST method for any endpoint.](images/POST_success.png)
#### TOKEN Success
![A screenshot of Insomnia, demonstrating a token being returned.](images/TOKEN_success.png)

#### ERD and API Spec
[API Specification - Submission.pdf](API_Spec_Submission.pdf)
![Alt text](images/ERD.png)


### How to:

1. Create User
```
curl --request POST \
  --url https://crowdfunding-back-end-equipme.fly.dev/users/ \
  --header 'Content-Type: application/json' \
  --data '    
    {
		"username": "<username>",
		"first_name": "<first name>",
		"last_name": "<last name>",
		"email": "<email address>",	
		"password": "<password>"
    }'
```

1. Sign in User
```
curl --request POST \
  --url https://crowdfunding-back-end-equipme.fly.dev/api-token-auth/ \
  --header 'Content-Type: application/json' \
  --data '   
    {
    "username": "<username>",
    "password": "<password>"
    }'
```

3. Create Project
```
curl --request POST \
  --url https://crowdfunding-back-end-equipme.fly.dev/projects/ \
  --header 'Authorization: TOKEN fc949fd1ff6b4ec8dec02d12ae8054117df1aa74' \
  --header 'Content-Type: application/json' \
  --header 'User-Agent: insomnia/8.5.1' \
  --data '
    {
	"title": "<title>",
	"description": "<description>",
	"goal": "<goal amount integer>",
	"image": "<image url>",
	"is_open": "<boolean>",
	"date_end": "<date for the project to close (isoformat)>"
    }'
```
