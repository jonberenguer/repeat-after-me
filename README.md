# repeat-after-me
simple python script to record actions and repeat them


```
usage: repeat_after_me.py [-h] -t RTYPE [-f FNAME] [-i ITER]

repeat-after-me simple macro record and playback.

optional arguments:
  -h, --help            show this help message and exit
  -t RTYPE, --type RTYPE
                        define type: 1=record new actions, 2=replay actions from file
  -f FNAME, --filename FNAME
                        filename, if not defined yyyymmdd_HHMM_action-log.txt
  -i ITER, --num-iteration ITER
                        number of time to loop actions. (default: 0 will not loop, but will print actions)
```
