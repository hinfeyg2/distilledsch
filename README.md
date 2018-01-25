# distilledsch
Graduate Data Engineer Technical Challenge




### Running the application locally
* ###### Clone the repository
 ```$ git clone https://github.com/hinfeyg2/distilledsch.git```
 * ###### Create virtual environment
 ```$ virtualenv venv```
* ###### Activate virtual environment
```$ source bikes_env/bin/activate```
* ###### Install the required packages
```$ pip install -r requirements.txt```
* ###### Create and populate database
```python input_data.py```
or run the sql commands in ddl_dml_scripts.txt
* ###### Run the app
```$ python app.py```

### Testing
Testing is done with Python's [unittest](https://docs.python.org/3/library/unittest.html#module-unittest) testing framework for unit testing. Locally, tests can be run with the following command :
```$ python test.py -v```
