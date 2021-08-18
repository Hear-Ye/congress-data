import glob
import shutil
import subprocess
from datetime import datetime
from math import floor
from pathlib import Path
from uuid import uuid4

from congress_crawler.votes import run as _run_votes

ROOT_DIR = Path(__file__).parent.parent.parent


def archive_data(data_type: str):
    temp_dir = ROOT_DIR / str(uuid4())
    temp_dir.mkdir(exist_ok=False)
    for _dir in glob.glob(f"{ROOT_DIR / 'data'}/*/{data_type}/*"):
        shutil.copytree(_dir, _dir.replace(str(ROOT_DIR / "data"), str(temp_dir)))
    shutil.make_archive(data_type, "zip", temp_dir)
    shutil.rmtree(temp_dir)


def run_votes():
    # To get beginning to now:
    # run_votes(dict(congress="101", session="1989", chamber="senate"))
    # run_votes(dict(congress="101", session="1990"))
    # for x in range(datetime.now().year - 1991 + 1):
    #     run_votes(dict(congress=str(floor(102 + x/2)), session=str(1991 + x)))

    # Gets the latest votes along with updated votes for our entire year
    latest = datetime.now().year - 1991
    _run_votes(dict(congress=str(floor(102 + latest / 2)), session=str(1991 + latest)))
    prior = latest - 1
    _run_votes(dict(congress=str(floor(102 + prior / 2)), session=str(1991 + prior)))
    
    # Restore modified files that only changed the updated_at field
    # git diff does not include new files
    git_diff = subprocess.check_output(["git", "diff", "--stat"]).decode("utf-8")
    all_unnecessary_paths = [
        # Gets that path
        x.split("|")[0].strip()
        # Splits the git diff --stat command
        for x in git_diff.split("\n")
        # Checks if it's a path with changes
        # Then sees if it's 1 addition + 1 subtraction only (just the updated field)
        if "|" in x and "2 +-" in x.split("|", maxsplit=1)[1]
    ]
    subprocess.run(["git", "restore"] + all_unnecessary_paths)

    # Congress doesn't pass anything on Jan 1+2 and then Congress
    # swears in new members on the 3rd when the new bills roll in
    # for the new Congress.
    archive_data("votes")


if __name__ == "__main__":
    run_votes()

