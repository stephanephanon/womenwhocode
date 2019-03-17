Tutorial python files for WWC DC Python presentation on flask.

The slide deck that goes with these exercises is at: <URL>

# Prereqs
1. Clone the repo. You'll need the 'intro_to_flask' directory.
1. Install python if you don't have it. Python 3 is preferred.
1. Make a python virtual environment for flask.
    * python with pip. put the virtualenv in your flask tutorial directory
    ```
    cd /path/to/repo/intro_to_flask
    python -m venv flask_venv
    source flask_venv/bin/activate
    pip install flask
    ```
    * python with conda. conda will put the virtual env in your conda envs directory
    ```
    conda create -n flask_venv python=3.6
    conda install -n flask_venv
    source activate flask_venv
	  ```
1. We'll run flask from the terminal (mac) or cmd prompt (windows)
   * open a terminal or cmd prompt
   * `cd /path/to/the/repo/intro_to_flask`
   * set the flask environment variable
     * in the mac terminal, type: `export FLASK_APP=tutorial.py`
     * in the windows cmd prompt, type: `set FLASK_APP=tutorial.py`
   * run flask: `flask run`
1. Load your flask application. Open your browser and go to http://127.0.0.1:5000/
