# Description
Basics directory contains basic applications and dealing with basic elements in QT designer such as buttons, radio buttons, labels, line edit, date, list widget..etc

A GUI screenshot is included in each application folder to demonstrate the application's functionality and features.

**note**: Qt Designer is not used in the first 3 applications and no files for UI, implemented with pure Python Code using PyQt5.

# Dependencies

- PyQt5: command ```pip install PyQt5```
- QT Designer

**Note**: Qt Designer UI file is converted to Python file using command:

``` pyuic5 fileName.ui -o fileName.py```

# Apps content

## App1

Simple app to take 2 inputs in 2 text fields, when save is pressed, the inputs are displayed on console

**New**:
- Set app title and icon
- Buttons
- Labels and line edits (text fields)

## App2
Same as app1, but inputs are displayed on the application UI on a label

## App3
simple calculator to perform addition, subtraction, multiplication and division. result is displayed on the UI.

**note**: accepts integers only, float numbers or text inputs will lead to program termination.

## App4
Calculator app similar to app3. UI implemented using QT Designer.

## App6
simple app to select hobbies using multiple **checkboxes**. pressing 'Get' will display selected hobbies on UI label.

**New**:
- Groupbox
- Checkboxes

## App7
Simple app to select your country and job from **radio buttons**. pressing 'Get' will display selected country and job on UI label.

**New**:
- Radio buttons inside groupbox

## App8
Simple app to use dropdown menu (Combobox) and select an item. exploring how to clear the combobox by pressing clear, get current selected item and display it by pressing get, load new items to the dropdown menu by pressing load (items to be loaded are written already in code).

**New**:
- Combobox

## App9
Simple app to display message box when Exit is pressed to confirm exit.

**New**:
- Message box
- Warning message box and Question message box
- Adding details button to the message box, adding another button 'ignore' button for example

## App10
Simple app to display start date and end date, allowing user to select dates from calender UI. using PyQt function to calculate the days between start and end date by pressing 'get start to end days', or current date by pressing 'get start to current days'.

**New**:
- Date Edit

## App11
App to interact with list widget with the following options: add item, remove item, edit existing item, move item up or down, sort the list.

**New**:
- List widget and various methods to modify the list.
