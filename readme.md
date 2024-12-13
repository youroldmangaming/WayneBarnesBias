Last login: Sun Dec  8 17:55:23 on ttys011
mikewilson@Mikes-MacBook ~ % ssh rpi@192.168.188.151
rpi@192.168.188.151's password: 
Linux rpi51 6.6.51+rpt-rpi-2712 #1 SMP PREEMPT Debian 1:6.6.51-1+rpt3 (2024-10-08) aarch64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Fri Dec 13 20:22:47 2024 from 192.168.188.22
rpi@rpi51:~ $ cd WayneBarnesBias/
rpi@rpi51:~/WayneBarnesBias $ nano analysis2.py 
rpi@rpi51:~/WayneBarnesBias $ python3 analysis2.py 
Traceback (most recent call last):
  File "/home/rpi/WayneBarnesBias/analysis2.py", line 1, in <module>
    import pandas as pd
ModuleNotFoundError: No module named 'pandas'
rpi@rpi51:~/WayneBarnesBias $ source venv/bin/activate
(venv) rpi@rpi51:~/WayneBarnesBias $ python3 analysis2.py 
Barnes Matches:
                        date      opponent result  nz_points  opponent_points       referee
0   Sat 28th Oct 2023 9:00pm  South Africa   loss         11               12  Wayne Barnes
1   Sat 14th Oct 2023 9:00pm       Ireland    win         28               24  Wayne Barnes
2    Thu 5th Oct 2023 9:00pm       Uruguay    win         73                0  Wayne Barnes
3   Sat 29th Jul 2023 7:45pm     Australia    win         38                7  Wayne Barnes
4    Sat 5th Nov 2022 3:15pm         Wales    win         55               23  Wayne Barnes
5   Sat 16th Jul 2022 7:05pm       Ireland   loss         22               32  Wayne Barnes
6   Sat 20th Nov 2021 9:00pm        France   loss         25               40  Wayne Barnes
7    Fri 1st Nov 2019 6:00pm         Wales    win         40               17  Wayne Barnes
8   Sat 17th Nov 2018 7:00pm       Ireland   loss          9               16  Wayne Barnes
9   Sat 25th Aug 2018 7:35pm     Australia    win         40               12  Wayne Barnes
10  Sat 25th Nov 2017 5:15pm         Wales    win         33               18  Wayne Barnes
11  Sat 21st Oct 2017 8:00pm     Australia   loss         18               23  Wayne Barnes
12  Sat 19th Aug 2017 8:00pm     Australia    win         54               34  Wayne Barnes
13  Sat 26th Nov 2016 9:00pm        France    win         24               19  Wayne Barnes
14  Sat 11th Jun 2016 7:35pm         Wales    win         39               21  Wayne Barnes
15  Sun 20th Sep 2015 4:45pm     Argentina    win         26               16  Wayne Barnes
16   Sat 8th Aug 2015 8:05pm     Australia   loss         19               27  Wayne Barnes
17  Sat 22nd Nov 2014 5:30pm         Wales    win         34               16  Wayne Barnes
18   Sat 4th Oct 2014 5:05pm  South Africa   loss         25               27  Wayne Barnes
19   Sat 8th Jun 2013 7:35pm        France    win         23               13  Wayne Barnes
20  Sat 27th Aug 2011 8:05pm     Australia   loss         20               25  Wayne Barnes
21  Sat 12th Jun 2010 7:35pm       Ireland    win         66               28  Wayne Barnes
22   Sat 8th Nov 2008 5:15pm      Scotland    win         32                6  Wayne Barnes
23   Sat 6th Oct 2007 9:00pm        France   loss         18               20  Wayne Barnes
24   Sat 8th Sep 2007 1:45pm         Italy    win         76               14  Wayne Barnes

Other Matches:
                          date      opponent result  nz_points  opponent_points
0    Sun 24th Nov 2024  9:10pm         Italy    win         29               11
1    Sun 17th Nov 2024  9:10pm        France   loss         29               30
2     Fri 8th Nov 2024  8:10pm       Ireland    win         23               13
3     Sun 3rd Nov 2024  3:00pm       England    win         24               22
4    Fri 25th Oct 2024  2:50pm         Japan    win         64               19
..                         ...           ...    ...        ...              ...
317  Sat 22nd Jul 2000  7:35pm  South Africa    win         25               12
318  Sat 15th Jul 2000  8:00pm     Australia    win         39               35
319   Sat 1st Jul 2000  7:35pm      Scotland    win         48               14
320  Sat 24th Jun 2000  7:35pm      Scotland    win         69               20
321  Fri 16th Jun 2000  7:35pm         Tonga    win        102                0

[322 rows x 5 columns]

Barnes Dates:
<DatetimeArray>
['2023-10-28 21:00:00', '2023-10-14 21:00:00', '2023-10-05 21:00:00',
 '2023-07-29 19:45:00', '2022-11-05 15:15:00', '2022-07-16 19:05:00',
 '2021-11-20 21:00:00',                 'NaT', '2018-11-17 19:00:00',
 '2018-08-25 19:35:00', '2017-11-25 17:15:00', '2017-08-19 20:00:00',
 '2016-11-26 21:00:00', '2016-06-11 19:35:00', '2015-09-20 16:45:00',
 '2015-08-08 20:05:00', '2014-10-04 17:05:00', '2013-06-08 19:35:00',
 '2011-08-27 20:05:00', '2010-06-12 19:35:00', '2008-11-08 17:15:00',
 '2007-10-06 21:00:00', '2007-09-08 13:45:00']
Length: 23, dtype: datetime64[ns]

Filtered Other Matches (excluding dates from Barnes matches):
                   date      opponent result  nz_points  opponent_points
0   2024-11-24 21:10:00         Italy    win         29               11
1   2024-11-17 21:10:00        France   loss         29               30
2   2024-11-08 20:10:00       Ireland    win         23               13
4   2024-10-25 14:50:00         Japan    win         64               19
5   2024-09-28 19:05:00     Australia    win         33               13
..                  ...           ...    ...        ...              ...
315 2000-08-19 15:00:00  South Africa   loss         40               46
316 2000-08-05 19:35:00     Australia   loss         23               24
318 2000-07-15 20:00:00     Australia    win         39               35
320 2000-06-24 19:35:00      Scotland    win         69               20
321 2000-06-16 19:35:00         Tonga    win        102                0

[239 rows x 5 columns]

Wayne Barnes Refereed Matches:
Wins: 16, Losses: 9, Draws: 0

Other Refereed Matches:
Wins: 198, Losses: 41, Draws: 0
(venv) rpi@rpi51:~/WayneBarnesBias $ nano analysis2.py 
(venv) rpi@rpi51:~/WayneBarnesBias $ python3 analysis2.py 
Barnes Matches:
                        date      opponent result  nz_points  opponent_points       referee
0   Sat 28th Oct 2023 9:00pm  South Africa   loss         11               12  Wayne Barnes
1   Sat 14th Oct 2023 9:00pm       Ireland    win         28               24  Wayne Barnes
2    Thu 5th Oct 2023 9:00pm       Uruguay    win         73                0  Wayne Barnes
3   Sat 29th Jul 2023 7:45pm     Australia    win         38                7  Wayne Barnes
4    Sat 5th Nov 2022 3:15pm         Wales    win         55               23  Wayne Barnes
5   Sat 16th Jul 2022 7:05pm       Ireland   loss         22               32  Wayne Barnes
6   Sat 20th Nov 2021 9:00pm        France   loss         25               40  Wayne Barnes
7    Fri 1st Nov 2019 6:00pm         Wales    win         40               17  Wayne Barnes
8   Sat 17th Nov 2018 7:00pm       Ireland   loss          9               16  Wayne Barnes
9   Sat 25th Aug 2018 7:35pm     Australia    win         40               12  Wayne Barnes
10  Sat 25th Nov 2017 5:15pm         Wales    win         33               18  Wayne Barnes
11  Sat 21st Oct 2017 8:00pm     Australia   loss         18               23  Wayne Barnes
12  Sat 19th Aug 2017 8:00pm     Australia    win         54               34  Wayne Barnes
13  Sat 26th Nov 2016 9:00pm        France    win         24               19  Wayne Barnes
14  Sat 11th Jun 2016 7:35pm         Wales    win         39               21  Wayne Barnes
15  Sun 20th Sep 2015 4:45pm     Argentina    win         26               16  Wayne Barnes
16   Sat 8th Aug 2015 8:05pm     Australia   loss         19               27  Wayne Barnes
17  Sat 22nd Nov 2014 5:30pm         Wales    win         34               16  Wayne Barnes
18   Sat 4th Oct 2014 5:05pm  South Africa   loss         25               27  Wayne Barnes
19   Sat 8th Jun 2013 7:35pm        France    win         23               13  Wayne Barnes
20  Sat 27th Aug 2011 8:05pm     Australia   loss         20               25  Wayne Barnes
21  Sat 12th Jun 2010 7:35pm       Ireland    win         66               28  Wayne Barnes
22   Sat 8th Nov 2008 5:15pm      Scotland    win         32                6  Wayne Barnes
23   Sat 6th Oct 2007 9:00pm        France   loss         18               20  Wayne Barnes
24   Sat 8th Sep 2007 1:45pm         Italy    win         76               14  Wayne Barnes

Other Matches:
                          date      opponent result  nz_points  opponent_points
0    Sun 24th Nov 2024  9:10pm         Italy    win         29               11
1    Sun 17th Nov 2024  9:10pm        France   loss         29               30
2     Fri 8th Nov 2024  8:10pm       Ireland    win         23               13
3     Sun 3rd Nov 2024  3:00pm       England    win         24               22
4    Fri 25th Oct 2024  2:50pm         Japan    win         64               19
..                         ...           ...    ...        ...              ...
317  Sat 22nd Jul 2000  7:35pm  South Africa    win         25               12
318  Sat 15th Jul 2000  8:00pm     Australia    win         39               35
319   Sat 1st Jul 2000  7:35pm      Scotland    win         48               14
320  Sat 24th Jun 2000  7:35pm      Scotland    win         69               20
321  Fri 16th Jun 2000  7:35pm         Tonga    win        102                0

[322 rows x 5 columns]

Barnes Dates:
Traceback (most recent call last):
  File "/home/rpi/WayneBarnesBias/analysis2.py", line 32, in <module>
    print(barnes_dates)
          ^^^^^^^^^^^^
NameError: name 'barnes_dates' is not defined. Did you mean: 'barnes_matches'?
(venv) rpi@rpi51:~/WayneBarnesBias $ nano analysis2.py 
(venv) rpi@rpi51:~/WayneBarnesBias $ python3 analysis2.py 
Traceback (most recent call last):
  File "/home/rpi/WayneBarnesBias/analysis2.py", line 7, in <module>
    barnes_matches = pd.read_csv('barnes_refereed_matches.csv')
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/rpi/WayneBarnesBias/venv/lib/python3.11/site-packages/pandas/io/parsers/readers.py", line 1026, in read_csv
    return _read(filepath_or_buffer, kwds)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/rpi/WayneBarnesBias/venv/lib/python3.11/site-packages/pandas/io/parsers/readers.py", line 620, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/rpi/WayneBarnesBias/venv/lib/python3.11/site-packages/pandas/io/parsers/readers.py", line 1620, in __init__
    self._engine = self._make_engine(f, self.engine)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/rpi/WayneBarnesBias/venv/lib/python3.11/site-packages/pandas/io/parsers/readers.py", line 1880, in _make_engine
    self.handles = get_handle(
                   ^^^^^^^^^^^
  File "/home/rpi/WayneBarnesBias/venv/lib/python3.11/site-packages/pandas/io/common.py", line 873, in get_handle
    handle = open(
             ^^^^^
FileNotFoundError: [Errno 2] No such file or directory: 'barnes_refereed_matches.csv'
(venv) rpi@rpi51:~/WayneBarnesBias $ nano analysis2.py 
(venv) rpi@rpi51:~/WayneBarnesBias $ python3 analysis2.py 
Barnes Matches:
                        date      opponent result  nz_points  opponent_points       referee
0   Sat 28th Oct 2023 9:00pm  South Africa   loss         11               12  Wayne Barnes
1   Sat 14th Oct 2023 9:00pm       Ireland    win         28               24  Wayne Barnes
2    Thu 5th Oct 2023 9:00pm       Uruguay    win         73                0  Wayne Barnes
3   Sat 29th Jul 2023 7:45pm     Australia    win         38                7  Wayne Barnes
4    Sat 5th Nov 2022 3:15pm         Wales    win         55               23  Wayne Barnes
5   Sat 16th Jul 2022 7:05pm       Ireland   loss         22               32  Wayne Barnes
6   Sat 20th Nov 2021 9:00pm        France   loss         25               40  Wayne Barnes
7    Fri 1st Nov 2019 6:00pm         Wales    win         40               17  Wayne Barnes
8   Sat 17th Nov 2018 7:00pm       Ireland   loss          9               16  Wayne Barnes
9   Sat 25th Aug 2018 7:35pm     Australia    win         40               12  Wayne Barnes
10  Sat 25th Nov 2017 5:15pm         Wales    win         33               18  Wayne Barnes
11  Sat 21st Oct 2017 8:00pm     Australia   loss         18               23  Wayne Barnes
12  Sat 19th Aug 2017 8:00pm     Australia    win         54               34  Wayne Barnes
13  Sat 26th Nov 2016 9:00pm        France    win         24               19  Wayne Barnes
14  Sat 11th Jun 2016 7:35pm         Wales    win         39               21  Wayne Barnes
15  Sun 20th Sep 2015 4:45pm     Argentina    win         26               16  Wayne Barnes
16   Sat 8th Aug 2015 8:05pm     Australia   loss         19               27  Wayne Barnes
17  Sat 22nd Nov 2014 5:30pm         Wales    win         34               16  Wayne Barnes
18   Sat 4th Oct 2014 5:05pm  South Africa   loss         25               27  Wayne Barnes
19   Sat 8th Jun 2013 7:35pm        France    win         23               13  Wayne Barnes
20  Sat 27th Aug 2011 8:05pm     Australia   loss         20               25  Wayne Barnes
21  Sat 12th Jun 2010 7:35pm       Ireland    win         66               28  Wayne Barnes
22   Sat 8th Nov 2008 5:15pm      Scotland    win         32                6  Wayne Barnes
23   Sat 6th Oct 2007 9:00pm        France   loss         18               20  Wayne Barnes
24   Sat 8th Sep 2007 1:45pm         Italy    win         76               14  Wayne Barnes

Other Matches:
                          date      opponent result  nz_points  opponent_points
0    Sun 24th Nov 2024  9:10pm         Italy    win         29               11
1    Sun 17th Nov 2024  9:10pm        France   loss         29               30
2     Fri 8th Nov 2024  8:10pm       Ireland    win         23               13
3     Sun 3rd Nov 2024  3:00pm       England    win         24               22
4    Fri 25th Oct 2024  2:50pm         Japan    win         64               19
..                         ...           ...    ...        ...              ...
317  Sat 22nd Jul 2000  7:35pm  South Africa    win         25               12
318  Sat 15th Jul 2000  8:00pm     Australia    win         39               35
319   Sat 1st Jul 2000  7:35pm      Scotland    win         48               14
320  Sat 24th Jun 2000  7:35pm      Scotland    win         69               20
321  Fri 16th Jun 2000  7:35pm         Tonga    win        102                0

[322 rows x 5 columns]

Barnes Dates:
<DatetimeArray>
['2023-10-28 21:00:00', '2023-10-14 21:00:00', '2023-10-05 21:00:00',
 '2023-07-29 19:45:00', '2022-11-05 15:15:00', '2022-07-16 19:05:00',
 '2021-11-20 21:00:00',                 'NaT', '2018-11-17 19:00:00',
 '2018-08-25 19:35:00', '2017-11-25 17:15:00', '2017-08-19 20:00:00',
 '2016-11-26 21:00:00', '2016-06-11 19:35:00', '2015-09-20 16:45:00',
 '2015-08-08 20:05:00', '2014-10-04 17:05:00', '2013-06-08 19:35:00',
 '2011-08-27 20:05:00', '2010-06-12 19:35:00', '2008-11-08 17:15:00',
 '2007-10-06 21:00:00', '2007-09-08 13:45:00']
Length: 23, dtype: datetime64[ns]

Filtered Other Matches (excluding dates from Barnes matches):
                   date      opponent result  nz_points  opponent_points
0   2024-11-24 21:10:00         Italy    win         29               11
1   2024-11-17 21:10:00        France   loss         29               30
2   2024-11-08 20:10:00       Ireland    win         23               13
4   2024-10-25 14:50:00         Japan    win         64               19
5   2024-09-28 19:05:00     Australia    win         33               13
..                  ...           ...    ...        ...              ...
315 2000-08-19 15:00:00  South Africa   loss         40               46
316 2000-08-05 19:35:00     Australia   loss         23               24
318 2000-07-15 20:00:00     Australia    win         39               35
320 2000-06-24 19:35:00      Scotland    win         69               20
321 2000-06-16 19:35:00         Tonga    win        102                0

[239 rows x 5 columns]

Wayne Barnes Refereed Matches:
Wins: 16, Losses: 9, Draws: 0

Other Refereed Matches:
Wins: 198, Losses: 41, Draws: 0
(venv) rpi@rpi51:~/WayneBarnesBias $ python3 analysis2.py 
Barnes Matches:
                        date      opponent result  nz_points  opponent_points       referee
0   Sat 28th Oct 2023 9:00pm  South Africa   loss         11               12  Wayne Barnes
1   Sat 14th Oct 2023 9:00pm       Ireland    win         28               24  Wayne Barnes
2    Thu 5th Oct 2023 9:00pm       Uruguay    win         73                0  Wayne Barnes
3   Sat 29th Jul 2023 7:45pm     Australia    win         38                7  Wayne Barnes
4    Sat 5th Nov 2022 3:15pm         Wales    win         55               23  Wayne Barnes
5   Sat 16th Jul 2022 7:05pm       Ireland   loss         22               32  Wayne Barnes
6   Sat 20th Nov 2021 9:00pm        France   loss         25               40  Wayne Barnes
7    Fri 1st Nov 2019 6:00pm         Wales    win         40               17  Wayne Barnes
8   Sat 17th Nov 2018 7:00pm       Ireland   loss          9               16  Wayne Barnes
9   Sat 25th Aug 2018 7:35pm     Australia    win         40               12  Wayne Barnes
10  Sat 25th Nov 2017 5:15pm         Wales    win         33               18  Wayne Barnes
11  Sat 21st Oct 2017 8:00pm     Australia   loss         18               23  Wayne Barnes
12  Sat 19th Aug 2017 8:00pm     Australia    win         54               34  Wayne Barnes
13  Sat 26th Nov 2016 9:00pm        France    win         24               19  Wayne Barnes
14  Sat 11th Jun 2016 7:35pm         Wales    win         39               21  Wayne Barnes
15  Sun 20th Sep 2015 4:45pm     Argentina    win         26               16  Wayne Barnes
16   Sat 8th Aug 2015 8:05pm     Australia   loss         19               27  Wayne Barnes
17  Sat 22nd Nov 2014 5:30pm         Wales    win         34               16  Wayne Barnes
18   Sat 4th Oct 2014 5:05pm  South Africa   loss         25               27  Wayne Barnes
19   Sat 8th Jun 2013 7:35pm        France    win         23               13  Wayne Barnes
20  Sat 27th Aug 2011 8:05pm     Australia   loss         20               25  Wayne Barnes
21  Sat 12th Jun 2010 7:35pm       Ireland    win         66               28  Wayne Barnes
22   Sat 8th Nov 2008 5:15pm      Scotland    win         32                6  Wayne Barnes
23   Sat 6th Oct 2007 9:00pm        France   loss         18               20  Wayne Barnes
24   Sat 8th Sep 2007 1:45pm         Italy    win         76               14  Wayne Barnes

Other Matches:
                          date      opponent result  nz_points  opponent_points
0    Sun 24th Nov 2024  9:10pm         Italy    win         29               11
1    Sun 17th Nov 2024  9:10pm        France   loss         29               30
2     Fri 8th Nov 2024  8:10pm       Ireland    win         23               13
3     Sun 3rd Nov 2024  3:00pm       England    win         24               22
4    Fri 25th Oct 2024  2:50pm         Japan    win         64               19
..                         ...           ...    ...        ...              ...
317  Sat 22nd Jul 2000  7:35pm  South Africa    win         25               12
318  Sat 15th Jul 2000  8:00pm     Australia    win         39               35
319   Sat 1st Jul 2000  7:35pm      Scotland    win         48               14
320  Sat 24th Jun 2000  7:35pm      Scotland    win         69               20
321  Fri 16th Jun 2000  7:35pm         Tonga    win        102                0

[322 rows x 5 columns]

Barnes Dates:
<DatetimeArray>
['2023-10-28 21:00:00', '2023-10-14 21:00:00', '2023-10-05 21:00:00',
 '2023-07-29 19:45:00', '2022-11-05 15:15:00', '2022-07-16 19:05:00',
 '2021-11-20 21:00:00',                 'NaT', '2018-11-17 19:00:00',
 '2018-08-25 19:35:00', '2017-11-25 17:15:00', '2017-08-19 20:00:00',
 '2016-11-26 21:00:00', '2016-06-11 19:35:00', '2015-09-20 16:45:00',
 '2015-08-08 20:05:00', '2014-10-04 17:05:00', '2013-06-08 19:35:00',
 '2011-08-27 20:05:00', '2010-06-12 19:35:00', '2008-11-08 17:15:00',
 '2007-10-06 21:00:00', '2007-09-08 13:45:00']
Length: 23, dtype: datetime64[ns]

Filtered Other Matches (excluding dates from Barnes matches):
                   date      opponent result  nz_points  opponent_points
0   2024-11-24 21:10:00         Italy    win         29               11
1   2024-11-17 21:10:00        France   loss         29               30
2   2024-11-08 20:10:00       Ireland    win         23               13
4   2024-10-25 14:50:00         Japan    win         64               19
5   2024-09-28 19:05:00     Australia    win         33               13
..                  ...           ...    ...        ...              ...
315 2000-08-19 15:00:00  South Africa   loss         40               46
316 2000-08-05 19:35:00     Australia   loss         23               24
318 2000-07-15 20:00:00     Australia    win         39               35
320 2000-06-24 19:35:00      Scotland    win         69               20
321 2000-06-16 19:35:00         Tonga    win        102                0

[239 rows x 5 columns]

Wayne Barnes Refereed Matches:
Wins: 16, Losses: 9, Draws: 0

Other Refereed Matches:
Wins: 198, Losses: 41, Draws: 0
(venv) rpi@rpi51:~/WayneBarnesBias $ nano analysis2.py 
(venv) rpi@rpi51:~/WayneBarnesBias $ python3 analysis2.py 
Traceback (most recent call last):
  File "/home/rpi/WayneBarnesBias/analysis2.py", line 5, in <module>
    barnes_matches = pd.read_csv('barnes_refereed_matches.csv')
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/rpi/WayneBarnesBias/venv/lib/python3.11/site-packages/pandas/io/parsers/readers.py", line 1026, in read_csv
    return _read(filepath_or_buffer, kwds)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/rpi/WayneBarnesBias/venv/lib/python3.11/site-packages/pandas/io/parsers/readers.py", line 620, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/rpi/WayneBarnesBias/venv/lib/python3.11/site-packages/pandas/io/parsers/readers.py", line 1620, in __init__
    self._engine = self._make_engine(f, self.engine)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/rpi/WayneBarnesBias/venv/lib/python3.11/site-packages/pandas/io/parsers/readers.py", line 1880, in _make_engine
    self.handles = get_handle(
                   ^^^^^^^^^^^
  File "/home/rpi/WayneBarnesBias/venv/lib/python3.11/site-packages/pandas/io/common.py", line 873, in get_handle
    handle = open(
             ^^^^^
FileNotFoundError: [Errno 2] No such file or directory: 'barnes_refereed_matches.csv'
(venv) rpi@rpi51:~/WayneBarnesBias $ nano analysis2.py 
(venv) rpi@rpi51:~/WayneBarnesBias $ python3 analysis2.py 
Wayne Barnes Refereed Matches:
Wins: 16, Losses: 9, Draws: 0

Other Refereed Matches:
Wins: 198, Losses: 34, Draws: 7
(venv) rpi@rpi51:~/WayneBarnesBias $ nano analysis2.py 
(venv) rpi@rpi51:~/WayneBarnesBias $ python3 analysis2.py 
Traceback (most recent call last):
  File "/home/rpi/WayneBarnesBias/analysis2.py", line 7, in <module>
    barnes_matches = pd.read_csv('barnes_refereed_matches.csv')
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/rpi/WayneBarnesBias/venv/lib/python3.11/site-packages/pandas/io/parsers/readers.py", line 1026, in read_csv
    return _read(filepath_or_buffer, kwds)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/rpi/WayneBarnesBias/venv/lib/python3.11/site-packages/pandas/io/parsers/readers.py", line 620, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/rpi/WayneBarnesBias/venv/lib/python3.11/site-packages/pandas/io/parsers/readers.py", line 1620, in __init__
    self._engine = self._make_engine(f, self.engine)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/rpi/WayneBarnesBias/venv/lib/python3.11/site-packages/pandas/io/parsers/readers.py", line 1880, in _make_engine
    self.handles = get_handle(
                   ^^^^^^^^^^^
  File "/home/rpi/WayneBarnesBias/venv/lib/python3.11/site-packages/pandas/io/common.py", line 873, in get_handle
    handle = open(
             ^^^^^
FileNotFoundError: [Errno 2] No such file or directory: 'barnes_refereed_matches.csv'
(venv) rpi@rpi51:~/WayneBarnesBias $ nano analysis2.py 
(venv) rpi@rpi51:~/WayneBarnesBias $ python3 analysis2.py 

Removed Records from Other Matches (matching dates with Barnes matches):
                   date      opponent result  nz_points  opponent_points
3                   NaT       England    win         24               22
6                   NaT     Australia    win         31               28
8                   NaT  South Africa   loss         27               31
14  2023-10-28 21:00:00  South Africa   loss         11               12
16  2023-10-14 21:00:00       Ireland    win         28               24
..                  ...           ...    ...        ...              ...
305                 NaT     Australia   loss         26               29
308                 NaT  South Africa    win         12                3
310                 NaT     Argentina    win         67               19
317                 NaT  South Africa    win         25               12
319                 NaT      Scotland    win         48               14

[83 rows x 5 columns]

Wayne Barnes Refereed Matches:
Wins: 16, Losses: 9, Draws: 0

Other Refereed Matches:
Wins: 198, Losses: 34, Draws: 7
(venv) rpi@rpi51:~/WayneBarnesBias $ nano analysis2.py 
(venv) rpi@rpi51:~/WayneBarnesBias $ python3 analysis2.py 
Traceback (most recent call last):
  File "/home/rpi/WayneBarnesBias/analysis2.py", line 7, in <module>
    barnes_matches = pd.read_csv('barnes_refereed_matches.csv')
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/rpi/WayneBarnesBias/venv/lib/python3.11/site-packages/pandas/io/parsers/readers.py", line 1026, in read_csv
    return _read(filepath_or_buffer, kwds)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/rpi/WayneBarnesBias/venv/lib/python3.11/site-packages/pandas/io/parsers/readers.py", line 620, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/rpi/WayneBarnesBias/venv/lib/python3.11/site-packages/pandas/io/parsers/readers.py", line 1620, in __init__
    self._engine = self._make_engine(f, self.engine)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/rpi/WayneBarnesBias/venv/lib/python3.11/site-packages/pandas/io/parsers/readers.py", line 1880, in _make_engine
    self.handles = get_handle(
                   ^^^^^^^^^^^
  File "/home/rpi/WayneBarnesBias/venv/lib/python3.11/site-packages/pandas/io/common.py", line 873, in get_handle
    handle = open(
             ^^^^^
FileNotFoundError: [Errno 2] No such file or directory: 'barnes_refereed_matches.csv'
(venv) rpi@rpi51:~/WayneBarnesBias $ nano analysis2.py 
(venv) rpi@rpi51:~/WayneBarnesBias $ python3 analysis2.py 
Barnes Matches:
                        date      opponent result  nz_points  opponent_points       referee
0   Sat 28th Oct 2023 9:00pm  South Africa   loss         11               12  Wayne Barnes
1   Sat 14th Oct 2023 9:00pm       Ireland    win         28               24  Wayne Barnes
2    Thu 5th Oct 2023 9:00pm       Uruguay    win         73                0  Wayne Barnes
3   Sat 29th Jul 2023 7:45pm     Australia    win         38                7  Wayne Barnes
4    Sat 5th Nov 2022 3:15pm         Wales    win         55               23  Wayne Barnes
5   Sat 16th Jul 2022 7:05pm       Ireland   loss         22               32  Wayne Barnes
6   Sat 20th Nov 2021 9:00pm        France   loss         25               40  Wayne Barnes
7    Fri 1st Nov 2019 6:00pm         Wales    win         40               17  Wayne Barnes
8   Sat 17th Nov 2018 7:00pm       Ireland   loss          9               16  Wayne Barnes
9   Sat 25th Aug 2018 7:35pm     Australia    win         40               12  Wayne Barnes
10  Sat 25th Nov 2017 5:15pm         Wales    win         33               18  Wayne Barnes
11  Sat 21st Oct 2017 8:00pm     Australia   loss         18               23  Wayne Barnes
12  Sat 19th Aug 2017 8:00pm     Australia    win         54               34  Wayne Barnes
13  Sat 26th Nov 2016 9:00pm        France    win         24               19  Wayne Barnes
14  Sat 11th Jun 2016 7:35pm         Wales    win         39               21  Wayne Barnes
15  Sun 20th Sep 2015 4:45pm     Argentina    win         26               16  Wayne Barnes
16   Sat 8th Aug 2015 8:05pm     Australia   loss         19               27  Wayne Barnes
17  Sat 22nd Nov 2014 5:30pm         Wales    win         34               16  Wayne Barnes
18   Sat 4th Oct 2014 5:05pm  South Africa   loss         25               27  Wayne Barnes
19   Sat 8th Jun 2013 7:35pm        France    win         23               13  Wayne Barnes
20  Sat 27th Aug 2011 8:05pm     Australia   loss         20               25  Wayne Barnes
21  Sat 12th Jun 2010 7:35pm       Ireland    win         66               28  Wayne Barnes
22   Sat 8th Nov 2008 5:15pm      Scotland    win         32                6  Wayne Barnes
23   Sat 6th Oct 2007 9:00pm        France   loss         18               20  Wayne Barnes
24   Sat 8th Sep 2007 1:45pm         Italy    win         76               14  Wayne Barnes

Other Matches:
                          date      opponent result  nz_points  opponent_points
0    Sun 24th Nov 2024  9:10pm         Italy    win         29               11
1    Sun 17th Nov 2024  9:10pm        France   loss         29               30
2     Fri 8th Nov 2024  8:10pm       Ireland    win         23               13
3     Sun 3rd Nov 2024  3:00pm       England    win         24               22
4    Fri 25th Oct 2024  2:50pm         Japan    win         64               19
..                         ...           ...    ...        ...              ...
317  Sat 22nd Jul 2000  7:35pm  South Africa    win         25               12
318  Sat 15th Jul 2000  8:00pm     Australia    win         39               35
319   Sat 1st Jul 2000  7:35pm      Scotland    win         48               14
320  Sat 24th Jun 2000  7:35pm      Scotland    win         69               20
321  Fri 16th Jun 2000  7:35pm         Tonga    win        102                0

[322 rows x 5 columns]

Barnes Matches Dates after Conversion:
0    2023-10-28 21:00:00
1    2023-10-14 21:00:00
2    2023-10-05 21:00:00
3    2023-07-29 19:45:00
4    2022-11-05 15:15:00
5    2022-07-16 19:05:00
6    2021-11-20 21:00:00
7                    NaT
8    2018-11-17 19:00:00
9    2018-08-25 19:35:00
10   2017-11-25 17:15:00
11                   NaT
12   2017-08-19 20:00:00
13   2016-11-26 21:00:00
14   2016-06-11 19:35:00
15   2015-09-20 16:45:00
16   2015-08-08 20:05:00
17                   NaT
18   2014-10-04 17:05:00
19   2013-06-08 19:35:00
20   2011-08-27 20:05:00
21   2010-06-12 19:35:00
22   2008-11-08 17:15:00
23   2007-10-06 21:00:00
24   2007-09-08 13:45:00
Name: date, dtype: datetime64[ns]

Other Matches Dates after Conversion:
0     2024-11-24 21:10:00
1     2024-11-17 21:10:00
2     2024-11-08 20:10:00
3                     NaT
4     2024-10-25 14:50:00
              ...        
317                   NaT
318   2000-07-15 20:00:00
319                   NaT
320   2000-06-24 19:35:00
321   2000-06-16 19:35:00
Name: date, Length: 322, dtype: datetime64[ns]

Removed Records from Other Matches (matching dates with Barnes matches):
                   date      opponent result  nz_points  opponent_points
14  2023-10-28 21:00:00  South Africa   loss         11               12
16  2023-10-14 21:00:00       Ireland    win         28               24
17  2023-10-05 21:00:00       Uruguay    win         73                0
23  2023-07-29 19:45:00     Australia    win         38                7
28  2022-11-05 15:15:00         Wales    win         55               23
36  2022-07-16 19:05:00       Ireland   loss         22               32
39  2021-11-20 21:00:00        France   loss         25               40
72  2018-11-17 19:00:00       Ireland   loss          9               16
80  2018-08-25 19:35:00     Australia    win         40               12
85  2017-11-25 17:15:00         Wales    win         33               18
96  2017-08-19 20:00:00     Australia    win         54               34
101 2016-11-26 21:00:00        France    win         24               19
114 2016-06-11 19:35:00         Wales    win         39               21
121 2015-09-20 16:45:00     Argentina    win         26               16
123 2015-08-08 20:05:00     Australia   loss         19               27
132 2014-10-04 17:05:00  South Africa   loss         25               27
154 2013-06-08 19:35:00        France    win         23               13
176 2011-08-27 20:05:00     Australia   loss         20               25
194 2010-06-12 19:35:00       Ireland    win         66               28
214 2008-11-08 17:15:00      Scotland    win         32                6
226 2007-10-06 21:00:00        France   loss         18               20
230 2007-09-08 13:45:00         Italy    win         76               14

Wayne Barnes Refereed Matches:
Wins: 16, Losses: 9, Draws: 0

Other Refereed Matches:
Wins: 250, Losses: 43, Draws: 7
(venv) rpi@rpi51:~/WayneBarnesBias $ nano analysis2.py 
(venv) rpi@rpi51:~/WayneBarnesBias $ python3 analysis2.py 
Traceback (most recent call last):
  File "/home/rpi/WayneBarnesBias/analysis2.py", line 7, in <module>
    barnes_matches = pd.read_csv('barnes_refereed_matches.csv')
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/rpi/WayneBarnesBias/venv/lib/python3.11/site-packages/pandas/io/parsers/readers.py", line 1026, in read_csv
    return _read(filepath_or_buffer, kwds)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/rpi/WayneBarnesBias/venv/lib/python3.11/site-packages/pandas/io/parsers/readers.py", line 620, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/rpi/WayneBarnesBias/venv/lib/python3.11/site-packages/pandas/io/parsers/readers.py", line 1620, in __init__
    self._engine = self._make_engine(f, self.engine)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/rpi/WayneBarnesBias/venv/lib/python3.11/site-packages/pandas/io/parsers/readers.py", line 1880, in _make_engine
    self.handles = get_handle(
                   ^^^^^^^^^^^
  File "/home/rpi/WayneBarnesBias/venv/lib/python3.11/site-packages/pandas/io/common.py", line 873, in get_handle
    handle = open(
             ^^^^^
FileNotFoundError: [Errno 2] No such file or directory: 'barnes_refereed_matches.csv'
(venv) rpi@rpi51:~/WayneBarnesBias $ nano analysis2.py 
(venv) rpi@rpi51:~/WayneBarnesBias $ python3 analysis2.py 

Barnes Matches Dates after Conversion:
0    2023-10-28 21:00:00
1    2023-10-14 21:00:00
2    2023-10-05 21:00:00
3    2023-07-29 19:45:00
4    2022-11-05 15:15:00
5    2022-07-16 19:05:00
6    2021-11-20 21:00:00
7                    NaT
8    2018-11-17 19:00:00
9    2018-08-25 19:35:00
10   2017-11-25 17:15:00
11                   NaT
12   2017-08-19 20:00:00
13   2016-11-26 21:00:00
14   2016-06-11 19:35:00
15   2015-09-20 16:45:00
16   2015-08-08 20:05:00
17                   NaT
18   2014-10-04 17:05:00
19   2013-06-08 19:35:00
20   2011-08-27 20:05:00
21   2010-06-12 19:35:00
22   2008-11-08 17:15:00
23   2007-10-06 21:00:00
24   2007-09-08 13:45:00
Name: date, dtype: datetime64[ns]

Other Matches Dates after Conversion:
0     2024-11-24 21:10:00
1     2024-11-17 21:10:00
2     2024-11-08 20:10:00
3                     NaT
4     2024-10-25 14:50:00
              ...        
317                   NaT
318   2000-07-15 20:00:00
319                   NaT
320   2000-06-24 19:35:00
321   2000-06-16 19:35:00
Name: date, Length: 322, dtype: datetime64[ns]

Removed Records from Other Matches (matching dates with Barnes matches):
                   date      opponent result  nz_points  opponent_points
14  2023-10-28 21:00:00  South Africa   loss         11               12
16  2023-10-14 21:00:00       Ireland    win         28               24
17  2023-10-05 21:00:00       Uruguay    win         73                0
23  2023-07-29 19:45:00     Australia    win         38                7
28  2022-11-05 15:15:00         Wales    win         55               23
36  2022-07-16 19:05:00       Ireland   loss         22               32
39  2021-11-20 21:00:00        France   loss         25               40
72  2018-11-17 19:00:00       Ireland   loss          9               16
80  2018-08-25 19:35:00     Australia    win         40               12
85  2017-11-25 17:15:00         Wales    win         33               18
96  2017-08-19 20:00:00     Australia    win         54               34
101 2016-11-26 21:00:00        France    win         24               19
114 2016-06-11 19:35:00         Wales    win         39               21
121 2015-09-20 16:45:00     Argentina    win         26               16
123 2015-08-08 20:05:00     Australia   loss         19               27
132 2014-10-04 17:05:00  South Africa   loss         25               27
154 2013-06-08 19:35:00        France    win         23               13
176 2011-08-27 20:05:00     Australia   loss         20               25
194 2010-06-12 19:35:00       Ireland    win         66               28
214 2008-11-08 17:15:00      Scotland    win         32                6
226 2007-10-06 21:00:00        France   loss         18               20
230 2007-09-08 13:45:00         Italy    win         76               14

Wayne Barnes Refereed Matches:
Wins: 16, Losses: 9, Draws: 0

Other Refereed Matches:
Wins: 250, Losses: 43, Draws: 7
(venv) rpi@rpi51:~/WayneBarnesBias $ nano analysis2.py 
(venv) rpi@rpi51:~/WayneBarnesBias $ python3 analysis2.py 
Traceback (most recent call last):
  File "/home/rpi/WayneBarnesBias/analysis2.py", line 7, in <module>
    barnes_matches = pd.read_csv('barnes_refereed_matches.csv')
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/rpi/WayneBarnesBias/venv/lib/python3.11/site-packages/pandas/io/parsers/readers.py", line 1026, in read_csv
    return _read(filepath_or_buffer, kwds)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/rpi/WayneBarnesBias/venv/lib/python3.11/site-packages/pandas/io/parsers/readers.py", line 620, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/rpi/WayneBarnesBias/venv/lib/python3.11/site-packages/pandas/io/parsers/readers.py", line 1620, in __init__
    self._engine = self._make_engine(f, self.engine)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/rpi/WayneBarnesBias/venv/lib/python3.11/site-packages/pandas/io/parsers/readers.py", line 1880, in _make_engine
    self.handles = get_handle(
                   ^^^^^^^^^^^
  File "/home/rpi/WayneBarnesBias/venv/lib/python3.11/site-packages/pandas/io/common.py", line 873, in get_handle
    handle = open(
             ^^^^^
FileNotFoundError: [Errno 2] No such file or directory: 'barnes_refereed_matches.csv'
(venv) rpi@rpi51:~/WayneBarnesBias $ nano analysis2.py 
(venv) rpi@rpi51:~/WayneBarnesBias $ python3 analysis2.py 

Barnes Matches Dates after Conversion:
0    2023-10-28 21:00:00
1    2023-10-14 21:00:00
2    2023-10-05 21:00:00
3    2023-07-29 19:45:00
4    2022-11-05 15:15:00
5    2022-07-16 19:05:00
6    2021-11-20 21:00:00
7                    NaT
8    2018-11-17 19:00:00
9    2018-08-25 19:35:00
10   2017-11-25 17:15:00
11                   NaT
12   2017-08-19 20:00:00
13   2016-11-26 21:00:00
14   2016-06-11 19:35:00
15   2015-09-20 16:45:00
16   2015-08-08 20:05:00
17                   NaT
18   2014-10-04 17:05:00
19   2013-06-08 19:35:00
20   2011-08-27 20:05:00
21   2010-06-12 19:35:00
22   2008-11-08 17:15:00
23   2007-10-06 21:00:00
24   2007-09-08 13:45:00
Name: date, dtype: datetime64[ns]

Other Matches Dates after Conversion:
0     2024-11-24 21:10:00
1     2024-11-17 21:10:00
2     2024-11-08 20:10:00
3                     NaT
4     2024-10-25 14:50:00
              ...        
317                   NaT
318   2000-07-15 20:00:00
319                   NaT
320   2000-06-24 19:35:00
321   2000-06-16 19:35:00
Name: date, Length: 322, dtype: datetime64[ns]

Removed Records from Other Matches (matching dates with Barnes matches):
                   date      opponent result  nz_points  opponent_points
14  2023-10-28 21:00:00  South Africa   loss         11               12
16  2023-10-14 21:00:00       Ireland    win         28               24
17  2023-10-05 21:00:00       Uruguay    win         73                0
23  2023-07-29 19:45:00     Australia    win         38                7
28  2022-11-05 15:15:00         Wales    win         55               23
36  2022-07-16 19:05:00       Ireland   loss         22               32
39  2021-11-20 21:00:00        France   loss         25               40
72  2018-11-17 19:00:00       Ireland   loss          9               16
80  2018-08-25 19:35:00     Australia    win         40               12
85  2017-11-25 17:15:00         Wales    win         33               18
96  2017-08-19 20:00:00     Australia    win         54               34
101 2016-11-26 21:00:00        France    win         24               19
114 2016-06-11 19:35:00         Wales    win         39               21
121 2015-09-20 16:45:00     Argentina    win         26               16
123 2015-08-08 20:05:00     Australia   loss         19               27
132 2014-10-04 17:05:00  South Africa   loss         25               27
154 2013-06-08 19:35:00        France    win         23               13
176 2011-08-27 20:05:00     Australia   loss         20               25
194 2010-06-12 19:35:00       Ireland    win         66               28
214 2008-11-08 17:15:00      Scotland    win         32                6
226 2007-10-06 21:00:00        France   loss         18               20
230 2007-09-08 13:45:00         Italy    win         76               14

Wayne Barnes Refereed Matches:
Wins: 14, Losses: 8, Draws: 0

Other Refereed Matches:
Wins: 198, Losses: 34, Draws: 7
(venv) rpi@rpi51:~/WayneBarnesBias $ 
(venv) rpi@rpi51:~/WayneBarnesBias $ nano analysis2.py 
(venv) rpi@rpi51:~/WayneBarnesBias $ python3 analysis2.py 
Traceback (most recent call last):
  File "/home/rpi/WayneBarnesBias/analysis2.py", line 5, in <module>
    barnes_matches = pd.read_csv('barnes_refereed_matches.csv')
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/rpi/WayneBarnesBias/venv/lib/python3.11/site-packages/pandas/io/parsers/readers.py", line 1026, in read_csv
    return _read(filepath_or_buffer, kwds)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/rpi/WayneBarnesBias/venv/lib/python3.11/site-packages/pandas/io/parsers/readers.py", line 620, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/rpi/WayneBarnesBias/venv/lib/python3.11/site-packages/pandas/io/parsers/readers.py", line 1620, in __init__
    self._engine = self._make_engine(f, self.engine)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/rpi/WayneBarnesBias/venv/lib/python3.11/site-packages/pandas/io/parsers/readers.py", line 1880, in _make_engine
    self.handles = get_handle(
                   ^^^^^^^^^^^
  File "/home/rpi/WayneBarnesBias/venv/lib/python3.11/site-packages/pandas/io/common.py", line 873, in get_handle
    handle = open(
             ^^^^^
FileNotFoundError: [Errno 2] No such file or directory: 'barnes_refereed_matches.csv'
(venv) rpi@rpi51:~/WayneBarnesBias $ nano analysis2.py 
(venv) rpi@rpi51:~/WayneBarnesBias $ python3 analysis2.py 
Original Dates in Barnes Matches:
0     Sat 28th Oct 2023 9:00pm
1     Sat 14th Oct 2023 9:00pm
2      Thu 5th Oct 2023 9:00pm
3     Sat 29th Jul 2023 7:45pm
4      Sat 5th Nov 2022 3:15pm
5     Sat 16th Jul 2022 7:05pm
6     Sat 20th Nov 2021 9:00pm
7      Fri 1st Nov 2019 6:00pm
8     Sat 17th Nov 2018 7:00pm
9     Sat 25th Aug 2018 7:35pm
10    Sat 25th Nov 2017 5:15pm
11    Sat 21st Oct 2017 8:00pm
12    Sat 19th Aug 2017 8:00pm
13    Sat 26th Nov 2016 9:00pm
14    Sat 11th Jun 2016 7:35pm
15    Sun 20th Sep 2015 4:45pm
16     Sat 8th Aug 2015 8:05pm
17    Sat 22nd Nov 2014 5:30pm
18     Sat 4th Oct 2014 5:05pm
19     Sat 8th Jun 2013 7:35pm
20    Sat 27th Aug 2011 8:05pm
21    Sat 12th Jun 2010 7:35pm
22     Sat 8th Nov 2008 5:15pm
23     Sat 6th Oct 2007 9:00pm
24     Sat 8th Sep 2007 1:45pm
Name: date, dtype: object

Original Dates in Other Matches:
0      Sun 24th Nov 2024  9:10pm
1      Sun 17th Nov 2024  9:10pm
2       Fri 8th Nov 2024  8:10pm
3       Sun 3rd Nov 2024  3:00pm
4      Fri 25th Oct 2024  2:50pm
                 ...            
317    Sat 22nd Jul 2000  7:35pm
318    Sat 15th Jul 2000  8:00pm
319     Sat 1st Jul 2000  7:35pm
320    Sat 24th Jun 2000  7:35pm
321    Fri 16th Jun 2000  7:35pm
Name: date, Length: 322, dtype: object

Barnes Matches Dates after Conversion:
0    2023-10-28 21:00:00
1    2023-10-14 21:00:00
2    2023-10-05 21:00:00
3    2023-07-29 19:45:00
4    2022-11-05 15:15:00
5    2022-07-16 19:05:00
6    2021-11-20 21:00:00
7    2019-11-01 18:00:00
8    2018-11-17 19:00:00
9    2018-08-25 19:35:00
10   2017-11-25 17:15:00
11   2017-10-21 20:00:00
12   2017-08-19 20:00:00
13   2016-11-26 21:00:00
14   2016-06-11 19:35:00
15   2015-09-20 16:45:00
16   2015-08-08 20:05:00
17   2014-11-22 17:30:00
18   2014-10-04 17:05:00
19   2013-06-08 19:35:00
20   2011-08-27 20:05:00
21   2010-06-12 19:35:00
22   2008-11-08 17:15:00
23   2007-10-06 21:00:00
24   2007-09-08 13:45:00
Name: date, dtype: datetime64[ns]

Other Matches Dates after Conversion:
0     2024-11-24 21:10:00
1     2024-11-17 21:10:00
2     2024-11-08 20:10:00
3     2024-11-03 15:00:00
4     2024-10-25 14:50:00
              ...        
317   2000-07-22 19:35:00
318   2000-07-15 20:00:00
319   2000-07-01 19:35:00
320   2000-06-24 19:35:00
321   2000-06-16 19:35:00
Name: date, Length: 322, dtype: datetime64[ns]

Removed Records from Other Matches (matching dates with Barnes matches):
                   date      opponent result  nz_points  opponent_points
14  2023-10-28 21:00:00  South Africa   loss         11               12
16  2023-10-14 21:00:00       Ireland    win         28               24
17  2023-10-05 21:00:00       Uruguay    win         73                0
23  2023-07-29 19:45:00     Australia    win         38                7
28  2022-11-05 15:15:00         Wales    win         55               23
36  2022-07-16 19:05:00       Ireland   loss         22               32
39  2021-11-20 21:00:00        France   loss         25               40
60  2019-11-01 18:00:00         Wales    win         40               17
72  2018-11-17 19:00:00       Ireland   loss          9               16
80  2018-08-25 19:35:00     Australia    win         40               12
85  2017-11-25 17:15:00         Wales    win         33               18
90  2017-10-21 20:00:00     Australia   loss         18               23
96  2017-08-19 20:00:00     Australia    win         54               34
101 2016-11-26 21:00:00        France    win         24               19
114 2016-06-11 19:35:00         Wales    win         39               21
121 2015-09-20 16:45:00     Argentina    win         26               16
123 2015-08-08 20:05:00     Australia   loss         19               27
127 2014-11-22 17:30:00         Wales    win         34               16
132 2014-10-04 17:05:00  South Africa   loss         25               27
154 2013-06-08 19:35:00        France    win         23               13
176 2011-08-27 20:05:00     Australia   loss         20               25
194 2010-06-12 19:35:00       Ireland    win         66               28
214 2008-11-08 17:15:00      Scotland    win         32                6
226 2007-10-06 21:00:00        France   loss         18               20
230 2007-09-08 13:45:00         Italy    win         76               14

Wayne Barnes Refereed Matches:
Wins: 16, Losses: 9, Draws: 0

Other Refereed Matches:
Wins: 248, Losses: 42, Draws: 7
(venv) rpi@rpi51:~/WayneBarnesBias $ nano analysis2.py 
(venv) rpi@rpi51:~/WayneBarnesBias $ python3 analysis2.py 
Traceback (most recent call last):
  File "/home/rpi/WayneBarnesBias/analysis2.py", line 7, in <module>
    barnes_matches = pd.read_csv('barnes_refereed_matches.csv')
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/rpi/WayneBarnesBias/venv/lib/python3.11/site-packages/pandas/io/parsers/readers.py", line 1026, in read_csv
    return _read(filepath_or_buffer, kwds)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/rpi/WayneBarnesBias/venv/lib/python3.11/site-packages/pandas/io/parsers/readers.py", line 620, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/rpi/WayneBarnesBias/venv/lib/python3.11/site-packages/pandas/io/parsers/readers.py", line 1620, in __init__
    self._engine = self._make_engine(f, self.engine)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/rpi/WayneBarnesBias/venv/lib/python3.11/site-packages/pandas/io/parsers/readers.py", line 1880, in _make_engine
    self.handles = get_handle(
                   ^^^^^^^^^^^
  File "/home/rpi/WayneBarnesBias/venv/lib/python3.11/site-packages/pandas/io/common.py", line 873, in get_handle
    handle = open(
             ^^^^^
FileNotFoundError: [Errno 2] No such file or directory: 'barnes_refereed_matches.csv'
(venv) rpi@rpi51:~/WayneBarnesBias $ nano analysis2.py 
(venv) rpi@rpi51:~/WayneBarnesBias $ python3 analysis2.py 

Barnes Matches Dates after Conversion:
0    2023-10-28 21:00:00
1    2023-10-14 21:00:00
2    2023-10-05 21:00:00
3    2023-07-29 19:45:00
4    2022-11-05 15:15:00
5    2022-07-16 19:05:00
6    2021-11-20 21:00:00
7                    NaT
8    2018-11-17 19:00:00
9    2018-08-25 19:35:00
10   2017-11-25 17:15:00
11                   NaT
12   2017-08-19 20:00:00
13   2016-11-26 21:00:00
14   2016-06-11 19:35:00
15   2015-09-20 16:45:00
16   2015-08-08 20:05:00
17                   NaT
18   2014-10-04 17:05:00
19   2013-06-08 19:35:00
20   2011-08-27 20:05:00
21   2010-06-12 19:35:00
22   2008-11-08 17:15:00
23   2007-10-06 21:00:00
24   2007-09-08 13:45:00
Name: date, dtype: datetime64[ns]

Other Matches Dates after Conversion:
0     2024-11-24 21:10:00
1     2024-11-17 21:10:00
2     2024-11-08 20:10:00
3                     NaT
4     2024-10-25 14:50:00
              ...        
317                   NaT
318   2000-07-15 20:00:00
319                   NaT
320   2000-06-24 19:35:00
321   2000-06-16 19:35:00
Name: date, Length: 322, dtype: datetime64[ns]

Total Barnes Matches: 25
Total Other Matches: 322

Removed Records from Other Matches (matching dates with Barnes matches):
                   date      opponent result  nz_points  opponent_points
14  2023-10-28 21:00:00  South Africa   loss         11               12
16  2023-10-14 21:00:00       Ireland    win         28               24
17  2023-10-05 21:00:00       Uruguay    win         73                0
23  2023-07-29 19:45:00     Australia    win         38                7
28  2022-11-05 15:15:00         Wales    win         55               23
36  2022-07-16 19:05:00       Ireland   loss         22               32
39  2021-11-20 21:00:00        France   loss         25               40
72  2018-11-17 19:00:00       Ireland   loss          9               16
80  2018-08-25 19:35:00     Australia    win         40               12
85  2017-11-25 17:15:00         Wales    win         33               18
96  2017-08-19 20:00:00     Australia    win         54               34
101 2016-11-26 21:00:00        France    win         24               19
114 2016-06-11 19:35:00         Wales    win         39               21
121 2015-09-20 16:45:00     Argentina    win         26               16
123 2015-08-08 20:05:00     Australia   loss         19               27
132 2014-10-04 17:05:00  South Africa   loss         25               27
154 2013-06-08 19:35:00        France    win         23               13
176 2011-08-27 20:05:00     Australia   loss         20               25
194 2010-06-12 19:35:00       Ireland    win         66               28
214 2008-11-08 17:15:00      Scotland    win         32                6
226 2007-10-06 21:00:00        France   loss         18               20
230 2007-09-08 13:45:00         Italy    win         76               14

Wayne Barnes Refereed Matches:
Wins: 16, Losses: 9, Draws: 0

Other Refereed Matches:
Wins: 250, Losses: 43, Draws: 7
(venv) rpi@rpi51:~/WayneBarnesBias $ nano analysis2.py 
(venv) rpi@rpi51:~/WayneBarnesBias $ python3 analysis2.py 

Barnes Matches Dates after Conversion:
0    2023-10-28 21:00:00
1    2023-10-14 21:00:00
2    2023-10-05 21:00:00
3    2023-07-29 19:45:00
4    2022-11-05 15:15:00
5    2022-07-16 19:05:00
6    2021-11-20 21:00:00
7                    NaT
8    2018-11-17 19:00:00
9    2018-08-25 19:35:00
10   2017-11-25 17:15:00
11                   NaT
12   2017-08-19 20:00:00
13   2016-11-26 21:00:00
14   2016-06-11 19:35:00
15   2015-09-20 16:45:00
16   2015-08-08 20:05:00
17                   NaT
18   2014-10-04 17:05:00
19   2013-06-08 19:35:00
20   2011-08-27 20:05:00
21   2010-06-12 19:35:00
22   2008-11-08 17:15:00
23   2007-10-06 21:00:00
24   2007-09-08 13:45:00
Name: date, dtype: datetime64[ns]

Other Matches Dates after Conversion:
0     2024-11-24 21:10:00
1     2024-11-17 21:10:00
2     2024-11-08 20:10:00
3                     NaT
4     2024-10-25 14:50:00
              ...        
317                   NaT
318   2000-07-15 20:00:00
319                   NaT
320   2000-06-24 19:35:00
321   2000-06-16 19:35:00
Name: date, Length: 322, dtype: datetime64[ns]

Total Barnes Matches: 25
Total Other Matches: 322

Removed Records from Other Matches (matching dates with Barnes matches):
                   date      opponent result  nz_points  opponent_points
14  2023-10-28 21:00:00  South Africa   loss         11               12
16  2023-10-14 21:00:00       Ireland    win         28               24
17  2023-10-05 21:00:00       Uruguay    win         73                0
23  2023-07-29 19:45:00     Australia    win         38                7
28  2022-11-05 15:15:00         Wales    win         55               23
36  2022-07-16 19:05:00       Ireland   loss         22               32
39  2021-11-20 21:00:00        France   loss         25               40
72  2018-11-17 19:00:00       Ireland   loss          9               16
80  2018-08-25 19:35:00     Australia    win         40               12
85  2017-11-25 17:15:00         Wales    win         33               18
96  2017-08-19 20:00:00     Australia    win         54               34
101 2016-11-26 21:00:00        France    win         24               19
114 2016-06-11 19:35:00         Wales    win         39               21
121 2015-09-20 16:45:00     Argentina    win         26               16
123 2015-08-08 20:05:00     Australia   loss         19               27
132 2014-10-04 17:05:00  South Africa   loss         25               27
154 2013-06-08 19:35:00        France    win         23               13
176 2011-08-27 20:05:00     Australia   loss         20               25
194 2010-06-12 19:35:00       Ireland    win         66               28
214 2008-11-08 17:15:00      Scotland    win         32                6
226 2007-10-06 21:00:00        France   loss         18               20
230 2007-09-08 13:45:00         Italy    win         76               14

Wayne Barnes Refereed Matches:
Wins: 16, Losses: 9, Draws: 0

Other Refereed Matches:
Wins: 250, Losses: 43, Draws: 7
(venv) rpi@rpi51:~/WayneBarnesBias $ ls
analysis2.py  analysis.py  arnes_refereed_matches.csv  barnes_refereed_matches_copy.csv  other_refs_copy.csv  other_refs.csv  RefHighGameCount2000s.csv  venv
(venv) rpi@rpi51:~/WayneBarnesBias $ nano analysis2.py 
(venv) rpi@rpi51:~/WayneBarnesBias $ python3 analysis2.py 

Barnes Matches Dates after Conversion:
0    2023-10-28 21:00:00
1    2023-10-14 21:00:00
2    2023-10-05 21:00:00
3    2023-07-29 19:45:00
4    2022-11-05 15:15:00
5    2022-07-16 19:05:00
6    2021-11-20 21:00:00
7                    NaT
8    2018-11-17 19:00:00
9    2018-08-25 19:35:00
10   2017-11-25 17:15:00
11                   NaT
12   2017-08-19 20:00:00
13   2016-11-26 21:00:00
14   2016-06-11 19:35:00
15   2015-09-20 16:45:00
16   2015-08-08 20:05:00
17                   NaT
18   2014-10-04 17:05:00
19   2013-06-08 19:35:00
20   2011-08-27 20:05:00
21   2010-06-12 19:35:00
22   2008-11-08 17:15:00
23   2007-10-06 21:00:00
24   2007-09-08 13:45:00
Name: date, dtype: datetime64[ns]

Other Matches Dates after Conversion:
0     2024-11-24 21:10:00
1     2024-11-17 21:10:00
2     2024-11-08 20:10:00
3                     NaT
4     2024-10-25 14:50:00
              ...        
317                   NaT
318   2000-07-15 20:00:00
319                   NaT
320   2000-06-24 19:35:00
321   2000-06-16 19:35:00
Name: date, Length: 322, dtype: datetime64[ns]

Total Barnes Matches: 25
Total Other Matches: 322

Removed Records from Other Matches (matching dates with Barnes matches):
                   date      opponent result  nz_points  opponent_points
14  2023-10-28 21:00:00  South Africa   loss         11               12
16  2023-10-14 21:00:00       Ireland    win         28               24
17  2023-10-05 21:00:00       Uruguay    win         73                0
23  2023-07-29 19:45:00     Australia    win         38                7
28  2022-11-05 15:15:00         Wales    win         55               23
36  2022-07-16 19:05:00       Ireland   loss         22               32
39  2021-11-20 21:00:00        France   loss         25               40
72  2018-11-17 19:00:00       Ireland   loss          9               16
80  2018-08-25 19:35:00     Australia    win         40               12
85  2017-11-25 17:15:00         Wales    win         33               18
96  2017-08-19 20:00:00     Australia    win         54               34
101 2016-11-26 21:00:00        France    win         24               19
114 2016-06-11 19:35:00         Wales    win         39               21
121 2015-09-20 16:45:00     Argentina    win         26               16
123 2015-08-08 20:05:00     Australia   loss         19               27
132 2014-10-04 17:05:00  South Africa   loss         25               27
154 2013-06-08 19:35:00        France    win         23               13
176 2011-08-27 20:05:00     Australia   loss         20               25
194 2010-06-12 19:35:00       Ireland    win         66               28
214 2008-11-08 17:15:00      Scotland    win         32                6
226 2007-10-06 21:00:00        France   loss         18               20
230 2007-09-08 13:45:00         Italy    win         76               14

Wayne Barnes Refereed Matches:
Wins: 16, Losses: 9, Draws: 0

Other Refereed Matches:
Wins: 250, Losses: 43, Draws: 7
(venv) rpi@rpi51:~/WayneBarnesBias $ ls
analysis2.py  analysis.py  arnes_refereed_matches.csv  barnes_refereed_matches_cleaned.csv  barnes_refereed_matches_copy.csv  other_refs_cleaned.csv  other_refs_copy.csv  other_refs.csv  RefHighGameCount2000s.csv  venv
(venv) rpi@rpi51:~/WayneBarnesBias $ mv analysis2.py clean.py
(venv) rpi@rpi51:~/WayneBarnesBias $ nano analysis.py
(venv) rpi@rpi51:~/WayneBarnesBias $ python3 analysis.py 
Traceback (most recent call last):
  File "/home/rpi/WayneBarnesBias/analysis.py", line 3, in <module>
    from scipy import stats
ModuleNotFoundError: No module named 'scipy'
(venv) rpi@rpi51:~/WayneBarnesBias $ pip install scipy
Looking in indexes: https://pypi.org/simple, https://www.piwheels.org/simple
Collecting scipy
  Downloading scipy-1.14.1-cp311-cp311-manylinux_2_17_aarch64.manylinux2014_aarch64.whl (35.6 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 35.6/35.6 MB 597.3 kB/s eta 0:00:00
Requirement already satisfied: numpy<2.3,>=1.23.5 in ./venv/lib/python3.11/site-packages (from scipy) (2.2.0)
Installing collected packages: scipy
Successfully installed scipy-1.14.1
(venv) rpi@rpi51:~/WayneBarnesBias $ python3 analysis.py 

Wayne Barnes Refereed Matches:
Wins: 16, Losses: 9, Draws: 0
Win Ratio: 0.64

Other Refereed Matches:
Wins: 264, Losses: 51, Draws: 7
Win Ratio: 0.82

Chi-squared Test Statistic: 4.97, p-value: 0.0259
(venv) rpi@rpi51:~/WayneBarnesBias $ nano analysis.md
(venv) rpi@rpi51:~/WayneBarnesBias $ ls
analysis.md  analysis.py  arnes_refereed_matches.csv  barnes_refereed_matches_cleaned.csv  barnes_refereed_matches_copy.csv  clean.py  other_refs_cleaned.csv  other_refs_copy.csv  other_refs.csv  RefHighGameCount2000s.csv  venv
(venv) rpi@rpi51:~/WayneBarnesBias $ nano analysis.md

  GNU nano 7.2                                  analysis.md                                           
# Overall Analysis of Referee Performance and Bias Against Wayne Barnes

## Key Components of the Analysis

1. **Loading Cleaned Data**: The analysis begins by loading the cleaned CSV files containing match st>

2. **Win/Loss Calculation**: The script calculates the number of wins, losses, and draws for both Way>
   - Wins: **16**
   - Losses: **9**
   - Draws: **0**
   - Total Matches: **25**
   - Win Ratio: **64%**

   In contrast, other referees have the following statistics:
   - Wins: **264**
   - Losses: **51**
   - Draws: **7**
   - Total Matches: **322**
   - Win Ratio: **82%**

3. **Win Ratio Calculation**: The win ratios highlight a significant difference between Barnes and hi>

4. **Statistical Test**: A Chi-squared test is performed to assess whether the differences in outcome>

5. **Visualization**: The results are visualized using bar charts, allowing for easy comparison of wi>

## Referee Performance Data

| Referee            | Country  | Games | Wins | Win % | Loss | Draw | Duration Start     | Duration >
|--------------------|----------|-------|------|-------|------|------|---------------------|--------->
| Nigel Owens        | gb-wls   | 26    | 22   | 85%   | 4    | 0    | 21st Jul 2007      | 26th Oct >
| Wayne Barnes       | gb-eng   | 25    | 16   | 64%   | 9    | 0    | 8th Sep 2007       | 28th Oct >
| Craig Joubert      | za       | 19    | 17   | 89%   | 1    | 1    | 9th Jun 2007       | 10th Sep >
| Jaco Peyper        | za       | 18    | 15   | 83%   | 2    | 1    | 29th Sep 2012      | 8th Sep 2>
| Jonathan Kaplan     | za       | 18    | 14   | 78%   | 4    | 0    | 5th Aug 2000       | 7th Aug >

## Analysis of the Data

- **Win Ratios**:
  - Nigel Owens has the highest win percentage at **85%**, winning **22 out of 26** matches.
  - Wayne Barnes, with a win percentage of **64%**, ranks significantly lower than his peers, indicat>

- **Comparison with Other Referees**:
  - Barnes's win percentage (64%) is lower than all other referees listed, suggesting that he may be >
  - The average win percentage for the referees listed (excluding Barnes) is approximately **82.2%**.

- **Games Officiated**:
  - Barnes has officiated **25 games**, which is a reasonable sample size for analysis. However, it i>

- **Losses and Draws**:
  - Barnes has **9 losses** and no draws, indicating that the matches he officiated were often decisi>

- **Duration of Officiating**:
  - The duration of officiating for each referee varies. For example, Nigel Owens officiated from **2>

## Conclusion

The data indicates that Wayne Barnes has a lower win percentage compared to other referees, particula>

Further investigation, including a deeper analysis of specific match circumstances and contexts, coul>








                                          [ Read 60 lines ]
^G Help       ^O Write Out  ^W Where Is   ^K Cut        ^T Execute    ^C Location   M-U Undo
^X Exit       ^R Read File  ^\ Replace    ^U Paste      ^J Justify    ^/ Go To Line M-E Redo
