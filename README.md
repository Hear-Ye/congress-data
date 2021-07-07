# Congress Data

GitHub API for downloading Congress data in bulk
instead of using govtrack, govinfo, or other
websites.

---
### Usage

#### Bulk Data

Every day, we compile all the types of data from
[Hear-Ye/congress](https://github.com/Hear-Ye/congress) into a ZIP
file. The zip file are stored in GitHub release assets. The GitHub
tag format is in the format of YEAR-MONTH-DAY (e.g. 2020-01-01).

The zip file url format is: 
https://github.com/Hear-Ye/congress-data/releases/download/2021-07-06/votes.zip

To get the latest release, there's an API endpoint that gives you information:
https://api.github.com/repos/Hear-Ye/congress-data/releases/latest

#### Individual Data

We use GitHub Pages so that you can download any individual piece
of data using a simple url that follows this git repository's directory format.
You can grab any individual piece of data by following the format:

http://congress-data.hearye.us/data/101/votes/1989/s1/data.json

Note: `https` is also allowed. We do not force `http` so that data
transmission is faster.

---

### License and Attribution

Created on 6 July 2020 for Hear Ye backend developers.
This repository is also designed to be a safe place
to download bulk data from the GitHub API as a reliable
source  rather than the govtrack or govinfo websites.

This data was gathered from the congress.gov website
using the [unitedstates/congress](https://github.com/unitedstates/congress)
repository (we technically use a port at
[Hear-Ye/congress](https://github.com/Hear-Ye/congress))

The data of this project itself is licensed under
the CC0 1.0 Universal license (which can be found in
the [LICENSE](./LICENSE) file), and the underlying 
source code used to update the data is licensed under
the Apache 2.0 license (which can be found in the
[LICENSE-CODE](./LICENSE-CODE) file).
