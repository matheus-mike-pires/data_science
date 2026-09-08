# Continental Asylum Flows: South America Refugee Research Engine

This repository is an interactive data science tool built to process, map, and analyze official government datasets of asylum and refugee requests across South America. Initially conceived to study the Venezuelan migration crisis in Brazil, the project has evolved into a comprehensive, generalized research engine designed to track continental human mobility and border policies.

**Current Status: Work in Progress**
Building a standardized continental database from disparate national records is a massive undertaking. Currently, the engine is fully operational exclusively for **Brazil**. Modules for **Argentina, Chile, and Paraguay** are actively on the roadmap and will be integrated into this repository over time.

## The Brazil Module (Active)

The current iteration processes Brazilian government data from 1994 to the present. By cleaning, merging, and filtering raw CSV files using Python and Pandas, the engine transforms fragmented government data into actionable sociological and legal insights.

**Core Engine Features:**

* **Unified Data Consolidation:** Automatically merges multiple annual datasets, bypassing bad lines and resolving encoding errors to create a single, clean DataFrame.
* **Interactive CLI Engine:** Users can run queries directly from the terminal to isolate specific migrant demographics.
* **Dynamic Filtering:** Search the historical database by country of nationality, specific entry dates, municipality of arrival, sex, or marital status.
* **Automated Statistical Extraction:** Instantly generates demographic distributions and entrance rates based on custom user parameters.

## Repository Structure

* **`main.py`**: The primary research engine. Run this file to launch the interactive terminal interface and query the general Brazilian database.
* **`raw_data/`**: The storage directory for official government `.csv` and `.zip` files. (Ensure your datasets are extracted here before running the engine).
* **`python_scripts/`**: Contains secondary modules, didactic documentation, and developmental iterations of the code.
* **`asylum-seekers-from-venezuela/`**: A dedicated sub-directory housing the hard-coded script (`refugee_from_venezuela.py`) and specific quantitative data used to write an academic paper on the 2017 Brazilian Migration Law and *Operação Acolhida*.
* **`ABOUT.md`**: The methodological document detailing the legal framework and mathematical approach used specifically for the Venezuelan case study.

## Getting Started

1. Ensure Python 3.x and the `pandas` library are installed.
2. Extract the Brazilian government datasets inside the `raw_data/` folder.
3. Open `main.py` and verify the file paths point correctly to your local `raw_data/` directory.
4. Execute `python main.py` in your terminal and follow the numerical menu to begin querying the database.
