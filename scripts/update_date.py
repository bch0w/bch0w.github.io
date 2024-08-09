"""
I'm tired of manually update the date on pages I update so here's a QnD script
to do it for me
"""
import sys
from datetime import datetime


datestr = datetime.today().strftime("%b %d, %Y")
fids = sys.argv[1:]
for fid in fids:
    with open(fid, "r") as f:
        lines = f.readlines()
        for i, line in enumerate(lines[:]):
            if "Last updated" in line:
                new_line = f"\t\t\t\t<li>Last updated {datestr}</li>\n"
                lines[i] = new_line
                break

    with open(fid, "w") as f:
        f.writelines(lines)

