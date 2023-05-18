Report for Assignment 07.
Tay Pham

Since each loop is a different multiprocessing event. The chunk sizes determine how many of them will run before joining. I'm only guessing here but since I only have 4 cores, I have notice that dividing the total number of items in the csv by around 3-5 and using that as the relative chunk sizes gives the best effect. Perhaps thats because I would only have about 3 available cores out of 4 and somehow the finish times line up to give an optimum performance? Overall there is minimal performance improvements seen over just using insert many just once. Which may be using multiprocessing already?

Also something to note is that I would need to close all other applications and disconnect my monitors to get the best performance else I get programs/monitor cut out. Especially at the lower chunk sizes.

Note: i just put the chunksize (size) adjustment in the main.py function inputs as a default if you want to adjust them.

Without Multiprocessing:
2022-02-20 15:50:01,781 menu.py:20  INFO Assignment 05 load user csv total time: 3714.6039 Milliseconds.
2022-02-20 15:51:41,836 menu.py:30  INFO Assignment 05 load status csv total time: 92852.9842 Milliseconds.

Multiprocessing: user chunk size 10, status update chunk size 1000
2022-03-05 10:37:28,248 menu.py:19  INFO load user csv total time: 24102.8631 Milliseconds.
2022-03-05 10:39:19,934 menu.py:29  INFO load status csv total time: 96493.1409 Milliseconds.

Multiprocessing: user chunk size 100, status update chunk size 10000
2022-03-05 10:40:26,217 menu.py:19  INFO load user csv total time: 6697.6039 Milliseconds.
2022-03-05 10:41:52,725 menu.py:29  INFO load status csv total time: 85071.8622 Milliseconds.

Multiprocessing: user chunk size 300, status update chunk size 30000
2022-03-05 10:42:59,045 menu.py:19  INFO load user csv total time: 3352.1211 Milliseconds.
2022-03-05 10:44:23,022 menu.py:29  INFO load status csv total time: 82208.7810 Milliseconds.

Multiprocessing: user chunk size 400, status update chunk size 40000
2022-03-05 10:46:54,183 menu.py:19  INFO load user csv total time: 3516.6569 Milliseconds.
2022-03-05 10:48:14,217 menu.py:29  INFO load status csv total time: 78983.2251 Milliseconds.

Multiprocessing: user chunk size 500, status update chunk size 50000
2022-03-05 10:49:33,832 menu.py:19  INFO load user csv total time: 2863.4989 Milliseconds.
2022-03-05 10:51:01,919 menu.py:29  INFO load status csv total time: 87135.5259 Milliseconds.

Multiprocessing: user chunk size 600, status update chunk size 60000
2022-03-05 10:53:28,219 menu.py:19  INFO load user csv total time: 2613.5101 Milliseconds.
2022-03-05 10:54:51,958 menu.py:29  INFO load status csv total time: 82162.3490 Milliseconds.

Multiprocessing: user chunk size 1000, status update chunk size 100000
2022-03-05 10:55:49,816 menu.py:19  INFO load user csv total time: 2988.1830 Milliseconds.
2022-03-05 10:57:12,993 menu.py:29  INFO load status csv total time: 81397.5489 Milliseconds.