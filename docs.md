- Data source and variables table
	- https://archive.ics.uci.edu/dataset/320/student+performance

## Setup
- `python3 -m venv venv`
- `pip install -r requirements.txt`
- `source ./venv/bin/activate`
- `nbstripout --install --attributes .gitattributes`
	- should filter notebook for git
## Building
- `python -m pip freeze > requirements.txt`

## Development
- `nbstripout main.ipynb`
	- removes metadata before committing
- `nbdime config-git --enable --global && git mergetool --tool nbdime -- *.ipynb`
	- setup jupiter notebook mergetool
- `nbdime main.ipynb`
	- run mergetool