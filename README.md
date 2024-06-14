# ft_linear_regression | 42KL

This project aims to introduce the concept of gradient descent which is an important optimisation algorithm used in the Machine Learning field. The Gradient Descent method is used to solve for the line of best fit of a simple linear regression based on small dataset of price of cars vs mileage (which is included in the repo).

The gradient descent algorithm can be optimised further using line search (not implemented in the project).  
The project is coded in Python together with Matplotlib.py and Numpy. The concepts are further illustrated in Jupyter Lab (file is also attached in repo).

See [`Subject PDF`](https://github.com/mseong123/ft_linear_regression/blob/master/en.subject.pdf) link.

## To run MANDATORY and BONUS
```
python train.py
python prediction.py
```
The program will prompt for an input (mileage) which will then output the predicted price of car based on the regression mode including a scatterplot showing the results and the precision of the model (R-square and Root Mean Square Deviation)

## To install jupyter lab
```
pip install jupyterlab
jupyter lab
```

In web interface, open notebook (ft_linear_regression.ipynb) and run the cells.
