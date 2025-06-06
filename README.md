
# 🏎️ Projeto ETL - Fórmula 1 (F1 Data ETL)

## 📌 Objetivo

Realizar um processo de **ETL (Extração, Transformação e Carga)** utilizando dados abertos de Fórmula 1, disponíveis no GitHub, com o intuito de preparar um conjunto de dados limpo, estruturado e pronto para análise ou visualização em ferramentas como Power BI, Excel ou Dashboards web.

---

## 🧰 Tecnologias Utilizadas

- Python 3
- Pandas
- Openpyxl
- OS (módulo padrão)
- Jupyter Notebook

---

## 📁 Estrutura de Diretórios

```bash
extracao/
├── saída/
│   ├── construtores.xlsx
│   ├── corridas.xlsx
│   ├── pilotos.xlsx
│   └── resultados.xlsx
```

---

## 🧪 Etapas do Processo

### 1. 📥 Extração

Os arquivos CSV foram baixados diretamente das URLs:

- `constructors.csv`
- `drivers.csv`
- `races.csv`
- `results.csv`

Utilizamos `pandas.read_csv()` para importar os dados diretamente das URLs hospedadas no GitHub.

---

### 2. 🧹 Transformação

Cada DataFrame passou por um processo de limpeza e renomeação de colunas.

#### a) Construtores (`constructors.csv`)

- Colunas removidas: `constructorRef`, `url`
- Colunas renomeadas:
  - `constructorId` → `montadora_id`
  - `name` → `nome`
  - `nationality` → `nacionalidade`

#### b) Pilotos (`drivers.csv`)

- Coluna criada: `nome_completo` (`forename` + `surname`)
- Colunas removidas: `forename`, `surname`, `url`, `number`, `dob`, `code`, `driverRef`
- Colunas renomeadas:
  - `driverId` → `piloto_id`
  - `nomeCompleto` → `nome_completo`
  - `nationality` → `nacionalidade`

#### c) Corridas (`races.csv`)

- Colunas removidas: `time`, `url`, `fp1_date`, `fp1_time`, `fp2_date`, `fp2_time`, `fp3_date`, `fp3_time`, `quali_date`, `quali_time`, `sprint_date`, `sprint_time`, `round`, `circuitId`
- Colunas renomeadas:
  - `raceId` → `corrida_id`
  - `year` → `ano`
  - `name` → `nome`
  - `date` → `corrida_data`

#### d) Resultados (`results.csv`)

- Colunas removidas: `number`, `grid`, `position`, `positionText`, `laps`, `time`, `milliseconds`, `fastestLap`, `rank`, `fastestLapSpeed`, `statusId`
- Colunas renomeadas:
  - `resultId` → `resultado_id`
  - `raceId` → `corrida_id`
  - `driverId` → `piloto_id`
  - `constructorId` → `montadora_id`
  - `positionOrder` → `posicao_ordem`
  - `points` → `pontos`
  - `fastestLapTime` → `volta_mais_rapida_tempo`

---

### 3. 📊 Validação dos Dados

Foram realizadas as seguintes validações:

- Verificação da forma dos DataFrames com `.shape`
- Análise das colunas com `.info()`
- Cálculo do percentual de valores nulos por coluna com `.isnull().sum()`

---

### 4. 💾 Carga

Os dados transformados foram exportados como arquivos `.xlsx`, utilizando `pandas.to_excel()` e salvos na pasta `extracao/saída/`.

---

## 📈 Possíveis Próximos Passos

- Integração com banco de dados (PostgreSQL, MySQL, etc.)
- Automatização com agendador (cron jobs, Apache Airflow)
- Visualizações com Dash, Power BI ou Tableau
- Expansão para outros datasets da F1 (como `lap_times.csv`, `pit_stops.csv`)


# 🗂️ Estrutura de Diretórios do Projeto

A organização em pastas do projeto foi estruturada para facilitar a separação de responsabilidades e garantir clareza no fluxo de trabalho. A estrutura é a seguinte:

```bash
📁 Projeto_ETL_F1/
├── 1 - TELAS/              # Imagens ou capturas de tela dos dashboards ou análises
├── 2 - PBIX/               # Arquivos do Power BI (.pbix)
├── 3 - ETL/                # Scripts e notebooks do processo de ETL
├── 4 - EXECUTAVEL ETL/     # Versão compilada do script ETL (ex: .exe gerado com PyInstaller)
└── ETL_F1_Documentacao.md  # Documentação do projeto em Markdown
```

## ✅ Explicação:

- **1 - TELAS/**  
  Contém evidências visuais como capturas de tela ou mockups do dashboard em funcionamento, útil para apresentações ou validação visual do projeto.

- **2 - PBIX/**  
  Armazena o arquivo `.pbix` do Power BI com as visualizações criadas a partir dos dados tratados no ETL.

- **3 - ETL/**  
  Contém o código-fonte do processo de ETL, como Jupyter Notebooks e scripts `.py`.

- **4 - EXECUTAVEL ETL/**  
  Guarda o executável gerado a partir do código do ETL. Ideal para rodar o processo sem depender do ambiente de desenvolvimento Python.

- **ETL_F1_Documentacao.md**  
  Documento explicativo com todas as etapas do projeto, desde a extração até a exportação dos arquivos finais.

---

## 👨‍💻 Autor

Paulo Vitor Jeronimo de Almeida 
https://br.linkedin.com/in/paulo-vitor-a17796175?trk=public_post_follow-view-profile

---
