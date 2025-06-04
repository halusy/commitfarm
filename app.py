import os
import time
import random
import datetime
import subprocess
import json
import string

os.chdir("/path/to/CommitFarm")

with open("season.json", "r") as a:
    season = json.load(a)

cycle = season["cycle"]
today = season["today"]
day_off = season["day_off"]

if day_off != today:
    num_of_commits = random.randint(1, 17)

    with open("harvest.txt", "a") as h:
        for i in range(num_of_commits):
            now = datetime.datetime.now().isoformat() + " EST"

            harvest_length = random.randint(50, 100)
            harvest_text = ''.join(random.choices(string.ascii_letters, k=harvest_length))
            h.write(now + "\n" + harvest_text + "\n\n")
            h.flush()

            subprocess.run(["git", "add", "harvest.txt"], check=True)
            subprocess.run(["git", "commit", "-m", "small update"], check=True)
            subprocess.run(["git", "push"], check=True)

            sleep_time = random.randint(180, 1380)
            time.sleep(sleep_time)
            print("waiting " + str(sleep_time) + " seconds")

if today == 4:
    season["today"] = 0
    season["day_off"] = random.randint(0, 4)
    season["cycle"] += 1
else:
    season["today"] += 1

with open("season.json", "w") as b:
    json.dump(season, b, indent=3)

print("donezo")
