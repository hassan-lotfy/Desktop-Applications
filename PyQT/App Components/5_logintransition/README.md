# Description

Login screen taking username and password, logins to main dashboard, sidebar menu to switch between 3 main pages: Home, Products, and Users Page.

### New Features: 
- Modern UI for Login screen.
- Added icon inside line edit (user icon for username line edit, and lock icon for password line edit).
- Made Username line edit selected by default upon opening the login screen.
- Pressing tab in login screen will jump from username to password field, then to login button, then to username again.
- Pressing Enter inside username or password fields will act as a click on login button.
- Maximizing the window on transition from small login screen to full dashboard screen.


# Notes

- Use setFocus method (to username line edit) after the window is open not before (after window.show).
- For sidebar UI, using a vertical spacer will not function properly (size stretching upon using layout horizontally will not give the desired UI), use an empty Qframe as a spacer.
- To add an Icon to the label, use addAction method, the Icon **MUST** be '.ico' extension.