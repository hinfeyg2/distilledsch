# distilledsch
Graduate Data Engineer Technical Challenge

### Running the application locally
* ###### Clone the repository (might need access)
 ```$ git clone https://github.com/charlawl/DublinBikeApp.git```
 * ###### Create virtual environment
 ```$ virtualenv bikes_env```
* ###### Source bikes_env
```$ source bikes_env/bin/activate```
* ###### Install the required packages
```$ pip install -r requirements.txt```
If new packages are used, they should be appended on to the requirements.txt file
* ###### Run the app
```$ python dublinbikeapp/__init__.py```

### Testing
We are using Python's [unittest](https://docs.python.org/3/library/unittest.html#module-unittest) testing framework for unit testing. Locally, tests can be run with the following command :

```$ python test.py -v```
