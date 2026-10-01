# Standard Operating Procedure

[![Documentation Status](https://img.shields.io/readthedocs/mvspain-sop?style=flat&label=readthedocs&logo=readthedocs)](https://mvspain-sop.readthedocs.io/en/latest/?badge=latest)
[![Static Badge](https://img.shields.io/github/license/rainville-lab/mvspain-sop?style=flat)](https://github.com/rainville-lab/mvspain-sop/blob/master/LICENSE)

This repository contains the source files for the Standard Operating Procedure for the
Metaphorical Verbal Suggestion for Modulating Pain Experience project.

## How to contribute

1. Clone the repository

```bash
git clone git@github.com:rainville-lab/mvspain-sop.git
```

2. Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

3. Install the requirements to build the docs
```bash
pip install -r docs/requirements.txt
```

4. Create a new branch
```bash
git switch -c <name_of_your_branch>
```
Alternatively:
```bash
git checkout -b <name_of_your_branch>
```

5. Add your modifications

6. Build the docs locally
```bash
cd docs
make html
```
This will generate the output in the `docs/build` folder. You can nagivate this folder and
open the file `docs/build/html/index.html` in your browser or any other html file.

7. Push your changes
```bash
git add <files_you_changed>
git commit -m '<you_descriptive_commit_message>'
git push origin <name_of_your_branch>
```

8. Create a PR on Github to merge your branch in `main`

Add the appropriate reviewers, and wait for the review :tada:

## Acknowledgement

The requirements and structure of that repository is based on the [physiopy-community-practices repository](https://github.com/physiopy/physiopy-community-practices) 🙌
