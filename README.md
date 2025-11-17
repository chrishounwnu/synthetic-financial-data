## Synthetic Financial Data Generation for Enhanced Financial Modeling

---

### Summary

This project explores the generation of synthetic financial data to address the challenges of privacy, scarcity, and access to real financial datasets.  
We combine statistical models (ARIMA, GARCH) and deep learning models (TimeGAN, Variational Autoencoder) to create realistic synthetic time series data.  
The synthetic data is evaluated using PCA visualization and Maximum Mean Discrepancy (MMD) metrics, and is tested in practical financial use cases like portfolio optimization and stress testing.

The project demonstrates that deep generative models, especially TimeGAN, can successfully produce synthetic datasets that retain the statistical properties of real financial data, making them highly useful for research and model development without violating data privacy.

---

### Project Structure

project_root/ │ 

├── data/ │ ├── raw/ # Raw real-world data (e.g., S&P500 historical prices) │ ├── processed/ # Intermediate synthetic data (saved .npy files) │ └── synthetic/ # Final synthetic datasets (.csv files) ready for use │ 

├── models/ # Trained and saved models (ARIMA, GARCH, TimeGAN, VAE) │ 

├── notebooks/ # Jupyter notebooks documenting each stage │ ├── 01_data_exploration.ipynb │ ├── 02_arima_garch_modeling.ipynb │ ├── 03_timegan_training.ipynb │ ├── 04_vae_training.ipynb │ ├── 05_evaluation.ipynb │ └── 06_use_cases.ipynb │ 

├── utils/ # Python utility scripts │ ├── data_loader.py │ ├── model_utils.py │ └── evaluation_metrics.py │ 

├── main.py # Main pipeline script to run the full workflow 

│ └── README.md # Project description and instructions (this file)

├── download_fun.ipynb ( to downolad the real data from yahoo finance

├── Christophe_Essay.pdf (my proposal)


---

## How to Run the Project

1. Clone the repository to your local machine:

```bash
git clone https://github.com/chrishounwnu/synthetic-financial-data.git
cd synthetic-financial-data

````

2. Install the required Python packages (create a virtual environment if needed):

pip install -r requirements.txt

3. Run the full pipeline from the terminal:

python main.py

4. Explore each notebook in the notebooks/ folder to understand detailed steps, modeling, training, and evaluation.

 ### Key Results
 
- TimeGAN generated synthetic sequences that closely match real financial time series based on:

 __PCA Visualization ➔ synthetic and real data clusters overlap.

__MMD Distance ➔ Real vs TimeGAN = very low (≈ 0.0044), indicating high similarity.

- Portfolio Optimization:

___Portfolios built on synthetic TimeGAN data were similar and realistic compared to real data portfolios.

___Simulated VAE synthetic data showed unrealistic behavior under stress conditions.

- Stress Testing:

_____TimeGAN synthetic portfolios remained stable and coherent under extreme market simulations.

_____Simulated VAE portfolios exhibited unrealistic explosive growth (expected due to random noise).

- Backtesting:

__________TimeGAN and real data produced stable and plausible returns.

_________Simulated VAE was highly volatile and unreliable.

These results confirm that deep generative models like TimeGAN can produce ethically usable and statistically valid financial datasets.

#### 👨‍🏫 Supervisor

This project was conducted under the supervision of:

Supervisor Name: Prof. Dr. Ulrich GABA

Affiliation: AIMS Rwanda

Email: yae@aims.ac.za 


📜 License

This project is developed for academic purposes.

Reuse, distribution, and modification should credit me and  my supervisor.

