# nuonline-points-clicker
Autoclicker to distribute skill points to game MuOnline created with PyAutoGUI

## How it works?

![skill buttons image from game screen](https://ibb.co/s53K33H)

-> Uses the skill points add buttons image from the character screen<br>
-> If you are running a different game version, change the buttons.png image.<br>
-> It will click in a specific mouse X and Y position to add the points automatically<br>

**NOTE**: created for testing of PyAutoGUI. Use wisely.

## What this code wont do!

-> Its not for auto hunting!<br>
-> Not tested with a lot of MuOnline game versions (the screen GUI must match to work)<br>

## Install instructions

    1. Install python(> 3.8.x)
    2. pip install virtualenv
    3. Execute: virtualenv venv (or any other env name you wish)
    4. Activate the virtual env: cd venv/scripts & activate
    5. Execute: "pip install -r requirements.txt" to install the package (only one so far)

## Config instructions

    * Change the amount of clicks on line 18 (run.py)
    * Change the coordinate offset on line 17
    * NOTE: its hardcode but i`m going to organizer in a close future!! :)

## Be happy! Don`t waste your time clicking thousands of times! :)
    EXECUTE: exec.bat ou python run.py

[Blog - rodrigoreisf.com.br](http://rodrigoreisf.com.br)
