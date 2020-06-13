# MacBook-Backlight-KDE
#### A (very) simple python script to fix the MacBook Backlight problem for KDE

*Note: This will only work with the fn key being pressed at the same time.*

##### To install:
First, open the terminal and type in <br> `git clone https://github.com/alex209175/MacBook-Backlight-KDE.git`<br><br>
Next install dependencies:<br>
`sudo apt-get install xbacklight python3-pip`<br>
`pip3 install keyboard`

##### Finally, to execute the script:
`cd MacBook-Backlight-KDE`<br>
`sudo python3 script.py`

As of yet, there is no way to execute the script on boot, as it requires your sudo credentials. You will manually have to execute the script every time your computer restarts.<br><br>

After executing the script, you are able to safely close the terminal window, ignoring the warnings. The script will stay executing as long as you don't press ctrl+c.

<br><br><br>
#### Website: www.42-incorporated.rf.gd 
