### Boston House Pricing Prediction

### Software And Tools Requirement

1. [Github Accounts](https://github.com)

2. [AWSAccount](https://aws.amazon.com/)

3. [VSCodeIDE](https://code.visualstudio.com/Download)

4. [GitCLI](https://cli.github.com/)

Create a new enviornment for project
    
    
    conda create -p venv python==3.7 -y
    

Activate the enviornment
    
    conda activate venv/
    
Update Requirement libraries

    pip install -r requirements.txt

Create a pythonic file in which web application is made using flask

    application.py

Build the machine learning model using jupyter notebook
     
    file_name.ipynb

Get the output as a pickled file out of the built model

    regmodel.pkl and scaling.pkl

Create a templates folder to write all the html code

    home.html

Create the required folder for beanstalk deployment

    .ebextentions
    .elasticbeanstalk

Finally add all the file to github

    git add .
    git status
    git commit -m "comments"
    git push origin main



