Tay Pham 02/20/2022
Below are the results from running menu.py for all of the functions listed in the assignment.
Assignment 03 is peewee while assignment 05 is mongodb.
The menu and main.py files were modified to make path work and i added logging to record the execution times using time.time().

Assignment 03's Performance:
2022-02-20 15:35:37,391 menu.py:28  INFO Assignment 03 load user csv total time: 374.8031 Milliseconds.
2022-02-20 15:36:20,693 menu.py:42  INFO Assignment 03 load status csv total time: 38077.7631 Milliseconds.
2022-02-20 15:36:34,329 menu.py:62  INFO Assignment 03 add user total time: 4.0040 Milliseconds.
2022-02-20 15:36:41,561 menu.py:78  INFO Assignment 03 update user total time: 3.9408 Milliseconds.
2022-02-20 15:36:44,150 menu.py:95  INFO Assignment 03 search user total time: 0.8609 Milliseconds.
2022-02-20 15:36:47,745 menu.py:108 INFO Assignment 03 delete user total time: 4.1528 Milliseconds.
2022-02-20 15:37:03,481 menu.py:124 INFO Assignment 03 add status total time: 5.0530 Milliseconds.
2022-02-20 15:37:11,047 menu.py:139 INFO Assignment 03 update status total time: 3.9921 Milliseconds.
2022-02-20 15:37:16,692 menu.py:155 INFO Assignment 03 search status total time: 0.5529 Milliseconds.
2022-02-20 15:37:20,231 menu.py:168 INFO Assignment 03 delete status total time: 4.1449 Milliseconds.

Assignment 05's Performance:
2022-02-20 15:50:01,781 menu.py:20  INFO Assignment 05 load user csv total time: 3714.6039 Milliseconds.
2022-02-20 15:51:41,836 menu.py:30  INFO Assignment 05 load status csv total time: 92852.9842 Milliseconds.
2022-02-20 15:52:10,517 menu.py:50  INFO Assignment 05 add user total time: 1.0531 Milliseconds.
2022-02-20 15:52:26,061 menu.py:66  INFO Assignment 05 update user total time: 2.3699 Milliseconds.
2022-02-20 15:52:33,637 menu.py:83  INFO Assignment 05 search user total time: 1.2801 Milliseconds.
2022-02-20 15:52:41,983 menu.py:96  INFO Assignment 05 delete user total time: 3.7911 Milliseconds.
2022-02-20 15:52:50,540 menu.py:111 INFO Assignment 05 add status total time: 1.9279 Milliseconds.
2022-02-20 15:52:59,783 menu.py:126 INFO Assignment 05 update status total time: 5.1267 Milliseconds.
2022-02-20 15:53:05,131 menu.py:142 INFO Assignment 05 search status total time: 1.2140 Milliseconds.
2022-02-20 15:53:08,643 menu.py:155 INFO Assignment 03 delete status total time: 1.9209 Milliseconds.

Mongodb does have a significant performance hit over peewee. However it seems the actions are all very time consistent while peewee can very from items to item. Adding and deleting can take up to 4 times longer than mongodb while others can take up to half the time. The answer to which is better would have to depend on the application. For applications that load files just once and runs many operations, I would choose mongo since overtime the performance would eventually overcome peewee. However if it requires a lot of csv data loading then currently, peewee is the better choice. However I suspect there are things that can be done to improve mongo. Also mongo seems to have the added benefit of cleaner code and possibly server interactions and tools.