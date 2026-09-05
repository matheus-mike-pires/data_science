[ENGLISH VERSION]
# Refugee Analysis in Brazil: The Venezuelan Crisis and Operação Acolhida

This repository contains the quantitative data and Python scripts supporting an academic paper on the Venezuelan refugee crisis and Operação Acolhida in Brazil. The overarching research evaluates the effectiveness of the Brazilian internalization model and the mass recognition of refugees, rooted in the application of the expanded refugee concept from the 1984 Cartagena Declaration by the National Committee for Refugees (CONARE).

The broader academic project integrates this quantitative data with a qualitative historical analysis of the international conjuncture to form a comprehensive conclusion.

## Objective and Methodology

The primary goal of the quantitative analysis is to mathematically demonstrate the impact of the 2017 Brazilian Migration Law and the subsequent *Operação Acolhida*. By utilizing the Pandas library to process official government datasets of refugee requests (1994–2023), the code tracks the physical entrance and institutional registration of migrants at the border.

To isolate the effects of the new legislation, the script segments the data into three distinct timeframes:

* **Pre-Law Baseline (2013–2016):** The standard rate of refugee requests prior to the new migration policies.
* **Transition and Implementation (2017–2018):** The critical years encompassing the passing of the law and the launch of Operação Acolhida.
* **Consolidation (2019–2023):** The aftermath period to verify if the initial surge stabilized into a consistent demographic shift.

By calculating the annual averages across these periods, the analysis identifies both the global increase in refugee requests and the specific relative prevalence of Venezuelan migrants, proving the tangible flexibilization of Brazilian borders.

## Repository Structure

* **`main.py`**: The fully optimized, primary Python script used to execute the final quantitative analysis and generate the statistical ratios.
* **`python_scripts/`**: An educational and documentation directory. It contains developmental iterations of the code, including a didactic version of the script that explains the methodology, coding logic, and data preparation process step-by-step.
* **`raw_data/`**: Contains the base datasets used for the analysis, provided as compressed files (`refugees_2.zip` and `request_refugee_1.zip`).

## How to Use

1. Ensure Python and the Pandas library are installed in your environment.
2. Extract the datasets located in the `raw_data` folder.
3. Update the file path variables within `main.py` to point to your local extracted CSV files.
4. Run `main.py` to output the cleaned DataFrames and the final comparative statistical ratios directly to your terminal.
5. For a detailed, step-by-step breakdown of the analytical logic, explore the didactic scripts inside the `python_scripts/` folder.


[Portuguese Version]

# Análise de Refugiados no Brasil: A Crise Venezuelana e a Operação Acolhida

Este repositório contém os dados quantitativos e scripts em Python que fundamentam um artigo acadêmico sobre a crise de refúgio venezuelana e a Operação Acolhida no Brasil. A pesquisa geral avalia a eficácia do modelo brasileiro de interiorização e o reconhecimento em massa de refugiados, enraizado na aplicação do conceito ampliado de refúgio da Declaração de Cartagena de 1984 pelo Comitê Nacional para os Refugiados (CONARE).

O projeto acadêmico mais amplo integra esses dados quantitativos a uma análise histórica qualitativa da conjuntura internacional para formar uma conclusão abrangente.

## Objetivo e Metodologia

O objetivo principal da análise quantitativa é demonstrar matematicamente o impacto da Lei de Migração brasileira de 2017 e da subsequente *Operação Acolhida*. Ao utilizar a biblioteca Pandas para processar bases de dados governamentais oficiais de solicitações de refúgio (1994–2023), o código rastreia a entrada física e o registro institucional dos migrantes na fronteira.

Para isolar os efeitos da nova legislação, o script segmenta os dados em três períodos distintos:

* **Linha de Base Pré-Lei (2013–2016):** A taxa padrão de solicitações de refúgio antes das novas políticas migratórias.
* **Transição e Implementação (2017–2018):** Os anos críticos que englobam a aprovação da lei e o lançamento da Operação Acolhida.
* **Consolidação (2019–2023):** O período subsequente para verificar se o aumento inicial se estabilizou em uma mudança demográfica consistente.

Ao calcular as médias anuais nesses períodos, a análise identifica tanto o aumento global nas solicitações de refúgio quanto a prevalência relativa específica dos migrantes venezuelanos, provando a flexibilização tangível das fronteiras brasileiras.

## Estrutura do Repositório

* **`main.py`**: O script principal em Python, totalmente otimizado, usado para executar a análise quantitativa final e gerar as proporções estatísticas.
* **`python_scripts/`**: Um diretório educacional e de documentação. Contém iterações de desenvolvimento do código, incluindo uma versão didática do script que explica a metodologia, a lógica de programação e o processo de preparação dos dados passo a passo.
* **`raw_data/`**: Contém as bases de dados originais usadas para a análise, fornecidas como arquivos compactados (`refugees_2.zip` e `request_refugee_1.zip`).

## Como Usar

1. Certifique-se de que o Python e a biblioteca Pandas estão instalados no seu ambiente.
2. Extraia os conjuntos de dados localizados na pasta `raw_data`.
3. Atualize as variáveis de caminho de arquivo dentro de `main.py` para apontar para os seus arquivos CSV extraídos localmente.
4. Execute o `main.py` para exibir os DataFrames limpos e as proporções estatísticas comparativas finais diretamente no seu terminal.
5. Para uma análise detalhada e passo a passo da lógica analítica, explore os scripts didáticos dentro da pasta `python_scripts/`.
