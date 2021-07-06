import glob
import shutil
from datetime import datetime
from math import floor
from pathlib import Path
from uuid import uuid4

from congress_crawler.votes import run as run_votes

ROOT_DIR = Path(__file__).parent.parent.parent


def organize_files_to_temp_dir(data_type):
    temp_dir = ROOT_DIR / str(uuid4())
    temp_dir.mkdir(exist_ok=False)
    for _dir in glob.glob(f"{ROOT_DIR / 'data'}/*/{data_type}/*"):
        shutil.copytree(_dir, _dir.replace(str(ROOT_DIR / "data"), str(temp_dir)))
    shutil.make_archive(data_type, "zip", temp_dir)
    shutil.rmtree(temp_dir)


def _run_votes():
    # To get beginning to now:
    # run_votes(dict(congress="101", session="1989", chamber="senate"))
    # run_votes(dict(congress="101", session="1990"))
    # for x in range(datetime.now().year - 1991 + 1):
    #     run_votes(dict(congress=str(floor(102 + x/2)), session=str(1991 + x)))

    # Gets the latest votes along with updated votes for our entire year
    latest = datetime.now().year - 1991
    run_votes(dict(congress=str(floor(102 + latest / 2)), session=str(1991 + latest)))
    # Congress doesn't pass anything on Jan 1+2 and then Congress
    # swears in new members on the 3rd when the new bills roll in
    # for the new Congress.
    organize_files_to_temp_dir("votes")


if __name__ == "__main__":
    _run_votes()

