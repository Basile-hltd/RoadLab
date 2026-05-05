## Tech Stack

- **Language:** Python
- **Interpreter Version:** 3.14.4
- **Target Platform:** Windows/MacOS/Linux
- **Version Control:** Git

## How to run ?

move to `.../RoadLab/RoadGraphEngine/` folder, create a python virtual environement, activate it and run :
```
pip install -r requirements.txt
```
to install all the needed dependencies.

Run the engine using :
```
python RoadGraphEngine.py <latitude in deg> <longitude in deg> <diameter_in_meters>
```

Exemple for Geneva with 1km diamater
```
python RoadGraphEngine.py 46.204833 6.143056 1000
```