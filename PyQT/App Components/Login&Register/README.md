## Description
Login and register pages app component, allowing user to sign in and verifying login credentials, or sign up, and adding new account credentials to database.

Added:
- stackedwidget to include application pages
- Stylesheets coloring for background
- designing underlined button with transparent background ``` <u>Sign In</u>``` and coloring in blue when hovered.

## Test cases implemented for app:

### Test Case 1
Scenario: User enters valid email and password (credentials: hassan@email.com & password) then click login app.

Output:  ```login successful``` on console.

### Test Case 2
Scenario: User enters invalid credentials:
- enters invalid email (ex: asd@email.com)
- enters invalid password
- invalid email and invalid password

and clicks **Sign In**.

Output: ```invalid username or password``` on console.

### Test Case 3
Scenario: User clicks **register**, then clicks ***sign in*** again.

Output: switch to Register Page, then Login Page.

### Test Case 4
Scenario: User enters Email, and two matching passwords and clicks **Sign Up**.

Output: ```Registered Successfully``` on console, then redirect to Login Page.

### Test Case 5
Scenario: User enters valid email but passwords don't match.

Output: ```Passwords don't match``` on console.


## Uncovered Scenarios

- User leaves text field (Line Edit) Empty and click **Sign In** or **Sign Up** in both login and register pages.

>Notations:
- No check for email format: if user enters email address like 'Mohamed' or 'John' will be accepted without checking for @ or domain.
- No check for password length, characters, upper case