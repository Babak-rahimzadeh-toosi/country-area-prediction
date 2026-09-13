# Population and Area Prediction Using Machine Learning

## Description

This project aims to collect country information, including the country name, capital, population, and area, from the ScrapeThisSite website and store it in a database. Then, using machine learning and a linear regression algorithm, the relationship between vpopulation and area is analyzed, and the area of countries is estimated based on their population.

## Features
- Extract country information from ScrapeThisSite
- Store the collected data in a database
- Use linear regression for machine learning
- Estimate country area based on population

## Technologies

- **Python** — Main programming language
- **Requests** — Sending HTTP requests
- **BeautifulSoup** — Web scraping and HTML parsing
- **re** — Data cleaning and structuring
- **SQLite** — Database
- **Scikit-learn** — Machine learning

## Project Structure

```text
project/
├── first_ml.py
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

## Installation

### 1. Clone the repository

```bash
git clone <repository-url>
cd <repository-directory>
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

On Windows:

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the project

```bash
python first_ml.py
```

The script will scrape country data, store it in a SQLite database, and perform the machine learning analysis.

## Usage

```bash
python first_ml.py
```

The script handles data collection, database storage, model training, prediction, and evaluation automatically.

## Machine Learning
The project uses **Linear Regression** to estimate country area based on population.

- **Feature (X):** Population
- **Target (y):** Area
- **Test size:** 20%
- **Random state:** 1

The model is evaluated using:

- **R² (R-squared):** Measures how well the model explains the variation in the target.
- **MAE (Mean Absolute Error):** Measures the average absolute prediction error.
- **RMSE (Root Mean Squared Error):** Measures prediction error while giving more weight to larger errors.

## Results

The current model produced the following results on the test set:

|**Metric**|**Result**|
| ------ | ------|
|  R² | -0.7184 |
| MAE | 475,552.48 |
| RMSE | 523,961.12 |

The results show that population alone is not a strong linear predictor of country area in this dataset. The negative R² indicates that the model performs worse than a simple baseline that predicts the mean area for every country.

Because the dataset is relatively small and the relationship between population and area is not necessarily linear, the model is mainly intended to demonstrate the machine learning workflow rather than provide highly accurate predictions.

## License

This project is available under the MIT License.



    