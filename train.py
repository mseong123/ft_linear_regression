import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math

def main():
	learningRate0 = 1 #1 step to reach mean which translate into mean square error of 0 with slope at constant
	learningRate1 = 0.00006 #minimum at which gradient decrease at second iteration, 0.00007 will cause it to diverge
	data = pd.read_csv("./data.csv")
	denominator = 1000
	theta0, theta1 = 0, 0
	normalized_km = (data["km"].values / denominator)
	price = data["price"].values
	gradient_theta0 = ((theta0 + (theta1 * normalized_km)) - price).mean()
	gradient_theta1 = (((theta0 + (theta1 * normalized_km)) - price) * normalized_km).mean()
	iteration = 0
	while (abs(gradient_theta0) > 1 or abs(gradient_theta1) > 1):
		gradient_theta0 = ((theta0 + (theta1 * normalized_km)) - price).mean()
		step_theta0 = learningRate0 * gradient_theta0
		temptheta0 = theta0 - step_theta0
		gradient_theta1 = (((theta0 + (theta1 * normalized_km)) - price) * normalized_km).mean()
		step_theta1 = learningRate1 * gradient_theta1
		temptheta1 = theta1 - step_theta1
		theta0 = temptheta0
		theta1 = temptheta1
		iteration += 1
	with open(".env","w") as f:
		f.write(f"THETA_0={theta0:.0f}\n")
		f.write(f"THETA_1={theta1 / denominator:.6f}\n")
		f.write(f"ITERATION={iteration}\n")




if __name__ == "__main__":
	main()
