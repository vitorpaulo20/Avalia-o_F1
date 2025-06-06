#!/usr/bin/env python
# coding: utf-8

# ## Importação das bibliotecas

# In[2]:


import pandas as pd
import openpyxl
import os


# ## Criar a pasta 'saída' se não existir

# In[4]:


os.makedirs('extracao', exist_ok=True)


# ## URLs dos arquivos

# In[6]:


url_constructors = 'https://github.com/CaioSobreira/dti_arquivos/raw/main/constructors.csv'
url_drivers = 'https://github.com/CaioSobreira/dti_arquivos/raw/main/drivers.csv'
url_races = 'https://github.com/CaioSobreira/dti_arquivos/raw/main/races.csv'
url_results = 'https://github.com/CaioSobreira/dti_arquivos/raw/main/results.csv'


# ## Carregando os DataFrames

# In[8]:


df_constructors = pd.read_csv(url_constructors)
df_drivers = pd.read_csv(url_drivers)
df_races = pd.read_csv(url_races)
df_results = pd.read_csv(url_results)


# ## Tratamento df_constructors

# In[10]:


df_constructors = df_constructors.drop(['constructorRef', 'url'], axis=1)

renomear_colunas = {
    "constructorId": "montadora_id",
    "name": "nome",
    "nationality": "nacionalidade"

}
df_constructors = df_constructors.rename(columns=renomear_colunas)

df_constructors.head()


# ## Tratamento df_drivers

# In[12]:


df_drivers['nomeCompleto'] = df_drivers['forename'] + ' ' + df_drivers['surname']

df_drivers = df_drivers.drop(['forename', 'surname','url','number','dob','code','driverRef'], axis=1)

renomear_colunas2 = {
    "driverId": "piloto_id",
    "nomeCompleto": "nome_completo",
    "nationality": "nacionalidade"
}
df_drivers = df_drivers.rename(columns=renomear_colunas2)

df_drivers.head()


# ## Tratamento df_races

# In[14]:


df_races = df_races.drop(['time', 'url', 'fp1_date', 'fp1_time', 'fp2_date', 'fp2_time', 'fp3_date', 'fp3_time', 'quali_date', 'quali_time', 'sprint_date', 'sprint_time', 'round', 'circuitId'], axis=1)

renomear_colunas3 = {
    "raceId": "corrida_id",
    "year": "ano",
    "name": "nome",
    "date": "corrida_data"
}
df_races = df_races.rename(columns=renomear_colunas3)

df_races.head()


# ## Tratamento df_results

# In[16]:


df_results = df_results.drop(['number', 'grid', 'position', 'positionText', 'laps', 'time', 'milliseconds', 'fastestLap', 'rank', 'fastestLapSpeed', 'statusId'], axis=1)

renomear_colunas4 = {
    "resultId": "resultado_id",
    "raceId": "corrida_id",
    "driverId": "piloto_id",
    "constructorId": "montadora_id",
    "positionOrder": "posicao_ordem",
    "points": "pontos",
    "fastestLapTime": "volta_mais_rapida_tempo"
}
df_results = df_results.rename(columns=renomear_colunas4)

df_results.head()  


# ## Consultando a saúde dos dados

# In[18]:


df_constructors.shape


# In[19]:


df_drivers.shape


# In[20]:


df_races.shape


# In[21]:


df_results.shape


# In[22]:


df_constructors.info()


# In[23]:


df_drivers.info()


# In[24]:


df_races.info()


# In[25]:


df_results.info()


# In[26]:


df_constructors.isnull().sum() / df_constructors.shape[0] * 100


# In[27]:


df_drivers.isnull().sum() / df_drivers.shape[0] * 100


# In[28]:


df_races.isnull().sum() / df_races.shape[0] * 100


# In[29]:


df_results.isnull().sum() / df_results.shape[0] * 100


# In[30]:


df_constructors.head()


# ## Criar a pasta 'saída' se não existir

# In[32]:


os.makedirs('extracao/saída', exist_ok=True)

# Caminho do arquivo Excel dentro da pasta
pasta_saida = 'extracao/saída'

# Salvando cada DataFrame em um arquivo Excel separado
df_results.to_excel(os.path.join(pasta_saida, 'resultados.xlsx'), index=False)
df_races.to_excel(os.path.join(pasta_saida, 'corridas.xlsx'), index=False)
df_drivers.to_excel(os.path.join(pasta_saida, 'pilotos.xlsx'), index=False)
df_constructors.to_excel(os.path.join(pasta_saida, 'construtores.xlsx'), index=False)

