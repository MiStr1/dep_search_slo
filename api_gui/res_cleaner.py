import os
import glob
import time

limit = time.time() - 1 # 60*60

skip_cleaning = set()

try:
    with open("skip_cache_clean.txt", "r") as skip_clean_file:
        for line in skip_clean_file:
            skip_cleaning.add(line.strip())
except:
    pass

print(skip_cleaning)

for f in glob.glob('./res/*'):
    tmp_f = f[5:]
    tmp_f = tmp_f[:tmp_f.rfind(".")]
    print(tmp_f)
    if not tmp_f in skip_cleaning and os.stat(f).st_mtime < limit:
        os.remove(f)


