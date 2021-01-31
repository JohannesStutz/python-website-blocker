# Python Website Blocker
Focus on your work by blocking your favorite productivity killers.

## Features
This Python script blocks certain websites from being accessed. You can customize the URLs you want to block by editing `blocklist.txt`.

## How to Install
**The Python Website Blocker currently only works for Windows.**
Download `blocker.py`, `pomodoro.py` and `blocklist.txt` and place them in the same directory.
You can `pip install win10toast` for [nice Windows notifications](https://github.com/jithurjacob/Windows-10-Toast-Notifications) from. But you don't have to, notifications are also printed in your command line tool.

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

## How to Run Pomodoro Timer
The [Pomodoro](https://en.wikipedia.org/wiki/Pomodoro_Technique) feature blocks your defined websites for 25 minutes. It notifies you after the 25 minutes are over and gives you access to all websites for 5 minutes (although I recommend getting up and stretching instead :slightly_smiling_face:). This cycle is repeated 4 times. **You have to run your command line tool with administrator privileges.**
```
python pomodoro.py
```

## Behind the Scenes
The script blocks URLs by modifying the `hosts` file. Blocked URLs are redirected to `127.0.0.1`. The script backs up the original `hosts` file, you will not lose any customizations and you can always reset to the original state.

## To Do
- Turn script into installable Python package
- extend to Linux and MacOS
- Add ability to schedule or block for specific period of time