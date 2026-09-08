# Refugee Analysis in Brazil: Comprehensive Asylum Request Mapping

This repository provides an interactive Python tool built to process, filter, and analyze official government datasets of all asylum and refugee requests in Brazil from 1994 to the present. While initially developed to study the Venezuelan migration crisis, the project has been expanded into a generalized data science tool capable of mapping continental and global asylum flows into Brazilian territory.

## Core Functionalities

* **Interactive Filtering Engine:** Users can query the massive dataset through a command-line interface via `main.py`, isolating specific demographics by nationality, entry date, municipality of arrival, marital status, and sex.
* **Statistical Extraction:** Automates the calculation of demographic distributions, temporal entrance rates, and dataset aggregations based on user-defined parameters.
* **Data Consolidation:** Merges multiple annual CSV datasets (spanning 1994–2026) into a single, clean Pandas DataFrame, automatically handling bad lines, dropping unnecessary columns, and resolving encoding errors.

## Repository Structure

* **`main.py`:** The primary interactive script. Run this file to access the main menu, apply custom filters, and extract statistical insights from the general database.
* **`raw_data/`:** The directory where the official `.csv` and `.zip` datasets must be extracted and stored for the script to ingest.
* **`python_scripts/`:** Contains secondary modules, didactic documentation, and earlier developmental iterations of the analytical code.
* **`asylum-seekers-from-venezuela/`:** A dedicated sub-directory housing the specific, hard-coded quantitative analysis used for the academic paper regarding *Operação Acolhida* and the Venezuelan crisis.
* **`ABOUT.md`:** The original context document (formerly the README) detailing the legal and academic methodology specifically tailored to the Venezuelan case study.

## How to Use

1. **Environment Setup:** Ensure Python 3.x and the `pandas` library are installed on your machine.
2. **Data Extraction:** Unzip the source files located in `raw_data/` so the raw `.csv` files are exposed.
3. **Path Configuration:** Open `main.py` and verify that the file paths in the data insertion block point correctly to your local `raw_data/` directory.
4. **Execution:** Run `python main.py` in your terminal. Use the numerical menu to interact with the database. For example, selecting the nationality filter and inputting "SYRIA" or "SENEGAL" will instantly isolate those specific migrant demographics for targeted analysis.
