# piechart.py
Python script which takes the .csv file as an input and analyzes the migrated accounts

## Installation
macOS comes with python pre-installed but it is always better to check the version and stay updated. So run the following commands on terminal

**For Python 2.7.x**
```bash
which python
python --version
python -m pip --version
```
**For Python 3.x.x**
```bash
which python3
python3 --version
python3 -m pip --version
```

pip is already installed if you are using Python 2 >=2.7.9 or Python 3 >=3.4 downloaded from python.org. **BUT** If error pop-ups saying no pip was found, you will have to install it from [Get pip](https://pip.pypa.io/en/stable/installing/)

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install matplotlib and pandas by running commands

```bash
python -m pip install -U pip
python -m pip install -U matplotlib
pip install pandas
```

## Usage

**For the .csv file**
- Raise a TUNEUP ticket to create a read-only Member DB account for yourself on Production.
- Follow steps mentioned [on this OpenRoad page](https://openroad.zipcar.com/display/COCO/Connecting+to+Redshift) to setup your RedShift DB
- Open zipcar > core > migration_accounts
- Export the data as a .csv file in your local directory

**To execute the program**

Once python and pip modules installed (refer [requirements.txt](https://stash.zipcar.com/projects/QE/repos/qa_acc_migration_script/browse/requirements.txt) for details of packages to install) proceed with the following commands to execute the script
```bash
python piechart.py
```
If you have Python3 installed, run
```bash
python3 piechart.py
```
Upon prompt for input, enter the path to your locally stored .csv file
```bash
Enter the path of your .csv file : /Users/shuchitamishra/Desktop/Prod-Migration/migration_accounts_202105181812.csv
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[Zipcar](https://www.zipcar.com)
