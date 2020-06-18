#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Desafio-1" data-toc-modified-id="Desafio-1-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Desafio 1</a></span><ul class="toc-item"><li><span><a href="#Set-up-da-análise" data-toc-modified-id="Set-up-da-análise-1.1"><span class="toc-item-num">1.1&nbsp;&nbsp;</span><em>Set up</em> da análise</a></span></li><li><span><a href="#Inicie-sua-análise-a-partir-daqui" data-toc-modified-id="Inicie-sua-análise-a-partir-daqui-1.2"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>Inicie sua análise a partir daqui</a></span></li><li><span><a href="#Questão-1" data-toc-modified-id="Questão-1-1.3"><span class="toc-item-num">1.3&nbsp;&nbsp;</span>Questão 1</a></span></li><li><span><a href="#Questão-2" data-toc-modified-id="Questão-2-1.4"><span class="toc-item-num">1.4&nbsp;&nbsp;</span>Questão 2</a></span></li><li><span><a href="#Questão-3" data-toc-modified-id="Questão-3-1.5"><span class="toc-item-num">1.5&nbsp;&nbsp;</span>Questão 3</a></span></li><li><span><a href="#Questão-4" data-toc-modified-id="Questão-4-1.6"><span class="toc-item-num">1.6&nbsp;&nbsp;</span>Questão 4</a></span></li><li><span><a href="#Questão-5" data-toc-modified-id="Questão-5-1.7"><span class="toc-item-num">1.7&nbsp;&nbsp;</span>Questão 5</a></span></li><li><span><a href="#Questão-6" data-toc-modified-id="Questão-6-1.8"><span class="toc-item-num">1.8&nbsp;&nbsp;</span>Questão 6</a></span></li><li><span><a href="#Questão-7" data-toc-modified-id="Questão-7-1.9"><span class="toc-item-num">1.9&nbsp;&nbsp;</span>Questão 7</a></span></li><li><span><a href="#Questão-8" data-toc-modified-id="Questão-8-1.10"><span class="toc-item-num">1.10&nbsp;&nbsp;</span>Questão 8</a></span></li><li><span><a href="#Questão-9" data-toc-modified-id="Questão-9-1.11"><span class="toc-item-num">1.11&nbsp;&nbsp;</span>Questão 9</a></span></li><li><span><a href="#Questão-10" data-toc-modified-id="Questão-10-1.12"><span class="toc-item-num">1.12&nbsp;&nbsp;</span>Questão 10</a></span></li></ul></li></ul></div>

# # Desafio 1
# 
# Para esse desafio, vamos trabalhar com o data set [Black Friday](https://www.kaggle.com/mehdidag/black-friday), que reúne dados sobre transações de compras em uma loja de varejo.
# 
# Vamos utilizá-lo para praticar a exploração de data sets utilizando pandas. Você pode fazer toda análise neste mesmo notebook, mas as resposta devem estar nos locais indicados.
# 
# > Obs.: Por favor, não modifique o nome das funções de resposta.

# ## _Set up_ da análise

# In[2]:


import pandas as pd
import numpy as np


# In[3]:


black_friday = pd.read_csv("black_friday.csv")


# ## Inicie sua análise a partir daqui

# In[4]:


black_friday.head(5)


# ## Questão 1
# 
# Quantas observações e quantas colunas há no dataset? Responda no formato de uma tuple `(n_observacoes, n_colunas)`.

# In[5]:


def q1():
    return black_friday.shape


# In[6]:


black_friday.shape


# ## Questão 2
# 
# Há quantas mulheres com idade entre 26 e 35 anos no dataset? Responda como um único escalar.

# In[43]:


def q2():
    return int(black_friday.query('Gender == "F" and Age=="26-35"')['Age'].value_counts()[0])


# In[8]:


black_friday.Age.unique()


# In[9]:


genders = black_friday.groupby('Gender')
genders


# In[10]:


black_friday.query('Gender == "F" and Age=="26-35"')['Age'].value_counts()


# In[44]:


int(black_friday.query('Gender == "F" and Age=="26-35"')['Age'].value_counts()[0])


# ## Questão 3
# 
# Quantos usuários únicos há no dataset? Responda como um único escalar.

# In[12]:


def q3():
    return len(black_friday.User_ID.unique())


# In[13]:


len(black_friday.User_ID.unique())


# ## Questão 4
# 
# Quantos tipos de dados diferentes existem no dataset? Responda como um único escalar.

# In[14]:


def q4():
    return len(black_friday.dtypes.unique())


# In[15]:


black_friday.dtypes


# In[16]:


len(black_friday.dtypes.unique())


# ## Questão 5
# 
# Qual porcentagem dos registros possui ao menos um valor null (`None`, `ǸaN` etc)? Responda como um único escalar entre 0 e 1.

# In[17]:


def q5():
    return (black_friday.shape[0] - black_friday.dropna().shape[0])/black_friday.shape[0]


# In[18]:


black_friday.info()


# In[19]:


black_friday.isna()


# In[20]:


black_friday.shape[0]


# In[21]:


black_friday.dropna().shape[0]


# In[22]:


percentual = (black_friday.shape[0] - black_friday.dropna().shape[0])/black_friday.shape[0]
percentual


# ## Questão 6
# 
# Quantos valores null existem na variável (coluna) com o maior número de null? Responda como um único escalar.

# In[46]:


def q6():
    return int(black_friday['Product_Category_3'].isna().sum())


# In[24]:


black_friday['Product_Category_3'].isna().sum()


# ## Questão 7
# 
# Qual o valor mais frequente (sem contar nulls) em `Product_Category_3`? Responda como um único escalar.

# In[25]:


def q7():
    return black_friday['Product_Category_3'].value_counts().index[0]


# In[26]:


black_friday['Product_Category_3'].value_counts().index[0]


# ## Questão 8
# 
# Qual a nova média da variável (coluna) `Purchase` após sua normalização? Responda como um único escalar.

# In[52]:


def q8():
    normalized = black_friday[['Purchase']]
    normalized_min = black_friday[['Purchase']].min()
    normalized_max = black_friday[['Purchase']].max()
    normalized_DF = (normalized - normalized_min) / (normalized_max - normalized_min)
    return float(normalized_DF.mean()[0])


# In[28]:


black_friday['Purchase'].isna().sum()


# In[29]:


normalized = black_friday[['Purchase']]
normalized


# In[30]:


normalized_min = black_friday[['Purchase']].min()
normalized_min


# In[31]:


normalized_max = black_friday[['Purchase']].max()
normalized_max


# In[32]:


normalized_DF = (normalized - normalized_min) / (normalized_max - normalized_min)
normalized_DF


# In[33]:


normalized_DF.mean()[0]


# ## Questão 9
# 
# Quantas ocorrências entre -1 e 1 inclusive existem da variáel `Purchase` após sua padronização? Responda como um único escalar.

# In[34]:


def q9():
    stand = black_friday[['Purchase']]
    stand_mean = black_friday[['Purchase']].mean()
    stand_std = black_friday[['Purchase']].std()
    stand_DF = (stand - stand_mean) / (stand_std)
    return stand_DF.query('Purchase >= -1 and Purchase <= 1').Purchase.shape[0]


# In[35]:


stand = black_friday[['Purchase']]


# In[36]:


stand_mean = black_friday[['Purchase']].mean()
stand_mean


# In[37]:


stand_std = black_friday[['Purchase']].std()
stand_std


# In[38]:


stand_DF = (stand - stand_mean) / (stand_std)
stand_DF


# In[39]:


stand_DF.query('Purchase >= -1 and Purchase <= 1').Purchase.shape[0]


# ## Questão 10
# 
# Podemos afirmar que se uma observação é null em `Product_Category_2` ela também o é em `Product_Category_3`? Responda com um bool (`True`, `False`).

# In[58]:


def q10():
    return bool(black_friday.isna().query('Product_Category_2 == True & Product_Category_3 == True').Product_Category_2.unique()[0])


# In[59]:


resultado = bool(black_friday.isna().query('Product_Category_2 == True & Product_Category_3 == True').Product_Category_2.unique()[0])
resultado

