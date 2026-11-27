"""
Course Number: ENGR 13100

Description:
    This program reads a CSV file containing stress and strain data for mild steel, and plots the stress-strain curve using matplotlib.
Assignment Information:
    Assignment:     11.1.3
    Author:         Paul Wever, weverp@purdue.edu
    Section:        215
    Team:           06 

"""

""" Write any import statements here (and delete this line)."""
import pandas as pd
import matplotlib.pyplot as plt

def main():
    """Write your code here (and delete this line)."""
    CSV_PATH = "mild_steel_stress_strain.csv"
    data = pd.read_csv(CSV_PATH)
    stress_mean = data["stress_MPa"].mean()
    strain_mean = data["strain_percent"].mean()
    stress_median = data["stress_MPa"].median()
    strain_median = data["strain_percent"].median()
    stress_std = data["stress_MPa"].std()
    strain_std = data["strain_percent"].std()
    stress_min = data["stress_MPa"].min()
    strain_min = data["strain_percent"].min()
    stress_max = data["stress_MPa"].max()
    strain_max = data["strain_percent"].max()

    print("---Mild Steel Stress-Strain Data---")
    print()
    print(data[0:5])
    print()
    print("Mean Stress:", f"{stress_mean:.2f} MPa")
    print("Median Stress:", f"{stress_median:.2f} MPa")
    print("Standard Deviation Stress:", f"{stress_std:.2f} MPa")
    print("Min Stress:", f"{stress_min:.2f} MPa")
    print("Max Stress:", f"{stress_max:.2f} MPa")
    print()
    print("Mean Strain:", f"{strain_mean:.2f} %")
    print("Median Strain:", f"{strain_median:.2f} %")
    print("Standard Deviation Strain:", f"{strain_std:.2f} %")
    print("Min Strain:", f"{strain_min:.2f} %")
    print("Max Strain:", f"{strain_max:.2f} %")

    plt.plot(data["strain_percent"], data["stress_MPa"], color="blue", marker="o")
    plt.title("Mild Steel Stress-Strain Curve", fontsize=14, pad=15)
    plt.xlabel("Strain (%)",fontsize=12, labelpad=10)
    plt.ylabel("Stress (MPa)", fontsize=12, labelpad=10)
    plt.xlim(0, 45)
    plt.ylim(0, 500)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.minorticks_on()
    plt.grid()
    plt.show()

if __name__ == "__main__":
    main()
