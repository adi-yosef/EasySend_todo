<<<<<<< HEAD
=======
<<<<<<< HEAD
# EasySend_todo
=======
# ToDoAPP

* clone this repo
* make sure you have python3 installed
* run commands if you want to open venv:
    * windows: 
        python -m venv venv
        venv\Scripts\activate
    * mac/linux:
        python3 -m venv venv
        source venv/bin/activate

* run this command to install requirements:
    * pip install -r requirements.txt

* run this command to install playwright browsers drivers:
    * playwright install


run commands:
* pytest: runs all tests
* pytest -v -s: runs all tests with verbose and prints
* pytest -k <expression>: runs test with test name as string exp. pytest -v -s -k "test_add_task_from_home_page" 
* pytest -v -s -m <mark>: runs all tests with pytest mark exp. pytest -v -s -m "ui"  
* pytest --html=report.html --self-contained-html: runs all tests and generate a report 
* pytest -n <number of workers>: runs tests in parallel with the number of workers exp. pytest -n 4

* all pytest commands can be added to one command exp. pytest -n 4 -m "ui"


