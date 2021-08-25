Easy clipboard manager
=============================
A program to sniff text clipboard
Ctrl + Space to stop program in background (u can change it)
***
How is it working?
==============
1) Make a new file in folder, where is file placed with filename %year-month-day%, where program will write a history of clipboard.
2) If file created - opened it.
3) Start sniff text clipboard. Format: %hours:minutes:seconds% > %some_text_in_clipboard%
4) Write text in file + console
5) If program sniff non-text - write empty line
6) If python process gonna close - write it.
7) Operations create/open/close - will have prefix  "!!!"
***
Installation
==============

Just run it in .py and u will see all in console + log file.
Just run it in .pyw and u will see all only in log file
***
Task
------------

Try to sniff clipboard in file
