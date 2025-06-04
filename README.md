CommitFarm 
By: Nicholas Ryan

unzip the file somwhere 

the json file tracks state. day off set to 4 is the default for the first cycle. 

you will need to fix all the file paths. i have them labeled with the typical path/to/file thing

you will need to configure git in the CommitFarm folder.
in terminal, navigate to you folder and initalize git, connect it to your github directory. google this shit if you dont know how. 

go to terminal, type crontab -e to edit your cron schedule 
paste the command in "cron_scrip.txt" to the crontab file (in the cron_script.txt file, you can edit the 30 19 to adjust the time is runs. 30 19 = 7:30pm )

cron will need full disk access to execute this code:
system setting > privacy & security > full disk access > click on the "+" > enter: cmd + shift + g > type the path - usr/sbin/cron > add cron to full disk access > toggel it on > restart mac 

should be good after this
cheers!

