The _ShowOff_ app
=================

The _ShowOff_ app allows you to share your screen time statistics with a group of friends.

Why should you do this?
-----------------------

A mobile screen is often a harmful enemy. It damages your hours of sleep, your health, 
your attention to your closes ones and distracts your mind from the things you want
to do.

There are many screen time tracker apps. Yet, they all have one big vulnerability:
They leave you alone in front of the enemy. What if it is stronger?

Installing _ShowOff_ is an act of humbleness. It might be too optimistic to hope we can beat
the addictive power of our screen using this very screen itself only. Sadly, if no one watching
**us**, we'll keep watching **it**. We have to get better opening conditions.

_ShowOff_ allows you to use the power of a group to reduce your screen time, and invest your 
resources in what care about.

Example
-------
This is how the _ShowOff_ app's statistics viewer looks like:

![Screenshots from ShowOff](readme_img/animated_screen_shots.png)

Structure
---------
Here is a diagram of the app's structure:

![ShowOff's struture](readme_img/app_structure.jpg)

The server-side is Django-based. 
The main principle of the design is keeping the client-side as "thin" as possible.
The main advantages of delegating most of the responsibilities to the server-side are:
* Simple structure: Fewer classes; No need for client-side Database; less friction between different languages.
* App update is not required when new functionality is applied, or when the UI is changed.
* Accessibility of a variety of powerful technologies

Tasks
-----
The following parts of the project are not yet completed:

Client-side: 

* All

Server-side:
* User registration
* Group registration
* Integration of the User and Group Models within the built-in Django's authentication and authorization
* Usage data receiver 


Features
--------
* Every user can register to ONE group only
* A group has up to 7 members.
* Presentation of the group's screen time statistics for yesterday, the last 7 days, and the last 30 days.

The limits on group size and groups number enhance the tangibility of one's rating in the group. They prop up the personal connections inside the group as well.

Author
------
[Itamar Stahl](https://github.com/itamar-stahl)

Changelog
---------

* 31/08/2021 - Update Readme.
* 31/08/2021 - UI: Minor changes. Update Readme.
* 31/08/2021 - First publish. Server-side only. Presents fake data.