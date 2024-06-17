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
`python train.py` will train the regression model based on the dataset(data.csv). `python prediction` will then execute the program and prompt for an input (mileage) which will then output the predicted price of car based on the regression mode including a scatterplot showing the results and the precision of the model (R-square and Root Mean Square Deviation)

## To install jupyter lab
```
pip install jupyterlab
jupyter lab
```

In web interface, open notebook (ft_linear_regression.ipynb) and run the cells. The notebook will provide visualisation to the gradient descent algorithm in action in particular:
* Animation of the individual cost functions derivatives w.r.t each coefficient alongside the steps taken to reach the optimum solution.
* The number of steps taken for the associated learning rate.
* a 3D wireframe showing update of the GD for both coefficient at the same time. 
