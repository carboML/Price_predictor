#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


def create_colors(red,green,blue,length,change):
    
    ''''
    INPUTS:
            red,gree,blue: RGB Values from 0 to 1 
            length: Number of colors required to create
            Change: The gradual change between one color an the other, values from 0.05-1.5 create good results
            
    OUTPUT:
            3D array with RGB values
    '''
            
    colores = np.zeros((length,3))

    r,g,b = [red,green,blue]
    change = change
    g_modo_menos = 1
    b_modo_menos = 0
    r_modo_menos = 1

    for i in range(len(colores)):

        if i == 0:
            colores[i,:] = [r,g,b]
        else:
            #print('Asi es como entra',g)


            if g+change*2>1:
                g_modo_menos = 1
            elif g-change*2<0:
                g_modo_menos = 0


            if g_modo_menos == 1:
                g = g-change
            else:
                g = g+change



            #print('Asi es como sale',g)


    ########################################
            #print('Asi es como entra',r)


            if r+change>1:
                r_modo_menos = 1
            elif r-change<0:
                r_modo_menos = 0


            if r_modo_menos == 1:
                r = r-change
            else:
                r = r+change



            #print('Asi es como sale',r)


    ######################################333       
            if b+change>1:
                b_modo_menos = 1
            elif b-change<0:
                b_modo_menos = 0


            if b_modo_menos == 1:
                b = b-change
            else:
                b = b+change

            colores[i,:] = [r,g,b]
            #colores[i,:] = 
            #colores[i,:] = np.random.rand(3,)




    return colores


# In[3]:


def get_null_info(df):
    no_nulls = set(df.columns[df.isnull().mean()==0])
    nulls = df.shape[1]-len(no_nulls)
    aux = df.isnull()
    count_null_perc = np.zeros(nulls)
    j = 0
    
    
    index = np.zeros(nulls)
    for i in range(len(aux.columns)):
        valor = aux.iloc[:,i].sum()
        if valor > 0:
            count_null_perc[j] = aux.iloc[:,i].sum() / len(aux)*100
            index[j] = i
            j = j+1
        
    null_values_info = pd.DataFrame()
    vector_indices = index
    columnas = []
    
    for i in range(len(vector_indices)):
        columnas.append(df.columns[vector_indices[i]])
    
    null_values_info['Column'] = columnas
    null_values_info['Percetaje_null_values'] = count_null_perc
    
    fig = plt.figure()  # an empty figure with no Axes
    fig, ax = plt.subplots()  # a figure with a single Axes
    fig.set_figheight(12)
    fig.set_figwidth(12)
    plt.barh(y = null_values_info['Column'],  width = null_values_info['Percetaje_null_values'], height = 1, color=(0/255,62/255, 97/255),edgecolor = 'black')
    ax.set_facecolor((27/255,151/255, 223/255))

    ax.set_xlabel('Percentage of NaN values in the column', fontsize=15)
    ax.set_ylabel('Feature', fontsize=15)

    
    
    
    
    
        
    return count_null_perc, index

def coef_weights(coefficients, X_train):
    '''
    INPUT:
    coefficients - the coefficients of the linear model 
    X_train - the training data, so the column names can be used
    OUTPUT:
    coefs_df - a dataframe holding the coefficient, estimate, and abs(estimate)
    
    Provides a dataframe that can be used to understand the most influential coefficients
    in a linear model by providing the coefficient estimates along with the name of the 
    variable attached to the coefficient.
    '''
    coefs_df = pd.DataFrame()
    coefs_df['est_int'] = X_train.columns
    coefs_df['coefs'] = lm_model.coef_
    coefs_df['abs_coefs'] = np.abs(lm_model.coef_)
    coefs_df = coefs_df.sort_values('abs_coefs', ascending=False)
    return coefs_df

def create_dummy_df(df, cat_cols, dummy_na):
    '''
    INPUT:
    df - pandas dataframe with categorical variables you want to dummy
    cat_cols - list of strings that are associated with names of the categorical columns
    dummy_na - Bool holding whether you want to dummy NA vals of categorical columns or not
    
    OUTPUT:
    df - a new dataframe that has the following characteristics:
            1. contains all columns that were not specified as categorical
            2. removes all the original columns in cat_cols
            3. dummy columns for each of the categorical columns in cat_cols
            4. if dummy_na is True - it also contains dummy columns for the NaN values
            5. Use a prefix of the column name with an underscore (_) for separating 
    '''
    for col in  cat_cols:
        try:
            # for each cat add dummy var, drop original column
            df = pd.concat([df.drop(col, axis=1), pd.get_dummies(df[col], prefix=col, prefix_sep='_', drop_first=True, dummy_na=dummy_na)], axis=1)
        except:
            continue
    return df


