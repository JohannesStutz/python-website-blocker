# Python Website Blocker
Focus on your work by blocking your favorite productivity killers.

## Features
This Python script blocks certain websites from being accessed. You can customize the URLs you want to block by editing `blocklist.txt`.

## How to install
**The Python Website Blocker currently only works for Windows.**
Download `blocker.py` and `blocklist.txt` and place them in the same directory.
You can `pip install win10toast` for nice Windows notifications. But you don't have to, notifications are also printed in your command line tool.

## How to run
To run the block script, **you have to run your command line tool with administrator privileges.**
To block websites:
```
cd /your/directory/
python blocker.py
```
To unblock all websites:
```
python blocker.py unblock
```

## Behind the scenes
The script blocks URLs by modifying the `hosts` file. Blocked URLs are redirected to `127.0.0.1`. The script backs up the original `hosts` file, you will not lose any customizations and you can always reset to the original state.

## To Do
- Turn script into installable Python package
- extend to Linux and MacOS
- Add scheduling, custom times or Pomodoro timer