import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math
import os
from dotenv import load_dotenv

def main():
	theta0, theta1 = 0, 0
	load_dotenv()
	if "THETA_0" in os.environ or "THETA_1" in os.environ:
		theta0 = int(os.getenv("THETA_0"))
		theta1 = float(os.getenv("THETA_1"))

	mileage = input("Please input mileage(km) in integer whole numbers:")
	try: 
		mileage = int(mileage)
	except:
		print("Incorrect input. Program terminating")
	else:
		result = theta0 + (theta1 * mileage)
		print(f"Estimate price for your car is:{result}")
		if result == 0:
			print("Training on dataset not started")
		else:
			print(f"Number of iterations taken for algo: {os.getenv("ITERATION")}")
			bonus(theta0, theta1)

def bonus(theta0, theta1):
	data = pd.read_csv("./data.csv")
	fig, axes = plt.subplots(figsize=(8,6))
	axes.set_title("ft_linear_regression")
	axes.set_ylabel("price")
	axes.set_xlabel("km")

	axes.scatter(data["km"], data["price"], label="Data points") 
	axes.axline((0,theta0), slope=theta1, color="g",linewidth=2, label=f"GD regression line:\nPrice = {theta0} - {-theta1}(Mileage)")
	result = np.polyfit(data["km"] / 1000, data["price"], 1)
	axes.axline((0,result[1]), slope=result[0]/1000, linewidth=0.5, color="y", label=f"numpy.polyfit regression line:\nPrice = {result[1]:.0f} - {-result[0]/1000:.6f}(Mileage)")
	axes.legend(loc="upper right")
	#calculate R^2
	sumResidualPrice = np.sum((data["price"] - np.array(data["price"]).mean())**2)
	sumGDResidualRegression = np.sum((data["price"] - (theta0 + (theta1 * data["km"])))**2)
	r_squared = 1 - (sumGDResidualRegression / sumResidualPrice)
	rootMeanSquaredDeviation = math.sqrt(((data["price"] - (theta0 + (theta1 * data["km"])))**2).mean())
	axes.text(125000,7300, f"Precision measurement\nR-squared:{r_squared:.2f}\nRMSD:{rootMeanSquaredDeviation:.2f}", verticalalignment="top")
	plt.show()
	


if __name__ == "__main__":
	main()