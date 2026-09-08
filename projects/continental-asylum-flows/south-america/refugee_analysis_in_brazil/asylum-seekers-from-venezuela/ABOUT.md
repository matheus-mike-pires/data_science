About This Research: Quantitative Analysis of the Venezuelan Refugee Crisis

This document outlines the methodological and computational framework supporting the academic research paper on the Venezuelan refugee crisis and the efficacy of Operação Acolhida in Brazil. The overarching research evaluates the impact of the 2017 Brazilian Migration Law and the mass recognition of refugees based on the expanded refugee concept from the 1984 Cartagena Declaration, as applied by the National Committee for Refugees (CONARE).

Script Designation and Repository Architecture

While the root directory of this repository features a generalized main.py script designed to dynamically filter and map all historical asylum flows into Brazil, the quantitative foundation for this specific academic article relies on a dedicated, hard-coded script. The file refugee_from_venezuela.py is the exact program utilized to extract the data, calculate the statistical proportions, and validate the core premises of this research.

Methodological Framework

The computational analysis processes official Brazilian government datasets encompassing refugee recognition requests spanning from 1994 to 2023. Because Brazilian legal frameworks dictate that asylum requests can exclusively be filed from within the national territory, the database acts as a mathematically verifiable metric of physical border entry and institutional reception.

To empirically isolate and demonstrate the border flexibilization resulting from the 2017 legislation, refugee_from_venezuela.py relies on the Pandas library to segment the temporal data into three distinct analytical periods:

Pre-Law Baseline (2013–2016): Establishes the historical average of global and Venezuelan refugee requests prior to the implementation of the new migration policies.

Transition and Implementation (2017–2018): Captures the critical phase during the formal enactment of the law and the initial structural deployment of Operação Acolhida in Roraima.

Consolidation (2019–2023): Evaluates the sustained aftermath, confirming whether the initial surge stabilized into a permanent demographic and institutional shift.

Quantitative Objectives

By calculating and comparing the annual averages across these three periods, the script isolates two primary indicators: the absolute growth rate of global asylum seekers entering Brazil, and the specific relative prevalence of Venezuelan nationals within that broader influx. This statistical extraction directly substantiates the qualitative historical analysis presented in the paper, proving the tangible effectiveness of the Brazilian internalization model.