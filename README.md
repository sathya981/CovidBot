## Description
CovidBot is a coronavirus helpline chatbot. It is rule-based chatbot with an ability to answer basic FAQs related to the covid-19.It can also give statistical analysis of different countries and different states within India.

## Install
This project requires Python and the following Python libraries installed:

1. [tensorflow](https://www.tensorflow.org/)
2. [pandas](https://pandas.pydata.org/)
3. [nltk](https://www.nltk.org/)
4. [numpy](https://numpy.org/)
5. json 
    -pip install json
6. random 
    -pip install random
7. pickle
    -pip install random
8. [requests](https://pypi.org/project/requests/)
    
9. [tkinter](https://docs.python.org/3/library/tkinter.html)

it is highly recommended that you install the [Anaconda](https://www.anaconda.com/) distribution of Python, which already has most of the above packages.The remaining can also be installed by going to Environments in Anaconda Navigator.

## Model Training
The colab notebook shared consists of code to train the model. It is stored in ipython notebook [chatbot.ipynb](chatbot.ipynb).
The dataset used for training is stored in [intents](chatbot/intents.json). The trained model are stored in [chatbot.h5](chatbot/chatbot.h5)

### Run
The project is a gui-based application. 
It also uses APIs to fetch realtime data, hence internet connectivity is required to run it.
Download the folder named chatbot. In chatbot folder, open the [gui.py](chatbot/gui.py) in spyder environment. Run the python file. It is highly recommended to run on spyder as it is application on Anaconda Distribution.

## Features
CovidBOT can answer the following queries related to coronavirus pandemic:

1. What is coronavirus ?
2. What is covid-19?
3. What are the symptoms of covid-19?
4. How does covid-19 spread?
5. What are the precautions?
6. What is death rate of disease?
7. What is the first covid-19 case in India?
8. Can cats and dogs spread the disease?
9. What are the vaccines available for coronavirus?
10. What is the procedure for interstate movement?
11. What is coronavirus helpline number?
12. What is the current statistics of coronavirus cases?
13. How to contribute to nation to fight against pandemic?
14. What is Arogya setu app?
