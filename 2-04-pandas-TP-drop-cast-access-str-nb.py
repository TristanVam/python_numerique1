# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     cell_metadata_json: true
#     text_representation:
#       extension: .py
#       format_name: percent
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
#   language_info:
#     name: python
#     nbconvert_exporter: python
#     pygments_lexer: ipython3
#   nbhosting:
#     title: TP sur le tri d'une dataframe
# ---

# %% [markdown]
# License CC BY-NC-ND, Valérie Roy & Thierry Parmentelat

# %% {"scrolled": true}
from IPython.display import HTML
HTML(filename="_static/style.html")

# %% [markdown]
# # TP on the moon

# %% [markdown]
# **Notions intervenant dans ce TP**
#
# * suppression de colonnes avec `drop` sur une `DataFrame`
# * suppression de colonne entièrement vide avec `dropna` sur une `DataFrame`
# * accès aux informations sur la dataframe avec `info`
# * valeur contenues dans une `Series` avec `unique` et `value_counts` 
# * conversion d'une colonne en type numérique avec `to_numeric` et `astype` 
# * accès et modification des chaînes de caractères contenues dans une colonne avec l'accesseur `str` des `Series`
# * génération de la liste Python des valeurs d'une série avec `tolist`
#    
# **N'oubliez pas d'utiliser le help en cas de problème.**
#
# **Répartissez votre code sur plusieurs cellules**

# %% [markdown]
# 1. importez les librairies `pandas` et `numpy`

# %%
# votre code
import pandas as pd
import numpy as np

# %% [markdown]
# 2. 1. lisez le fichier de données `data/objects-on-the-moon.csv`
#    2.  affichez sa taille et regardez quelques premières lignes

# %%
# votre code
pd.read_csv('data/objects-on-the-moon.csv')

# %% [markdown]
# 3. 1. vous remarquez une première colonne franchement inutile  
#      utiliser la méthode `drop` des dataframes pour supprimer cette colonne de votre dataframe  
#      `pd.DataFrame.drop?` pour obtenir de l'aide

# %%
df=pd.read_csv('data/objects-on-the-moon.csv')

# %%
# votre code
df = df.drop('Unnamed: 0', axis=1)

# %%
df

# %% [markdown]
# 4. 1. appelez la méthode `info` des dataframes  
#    (`non-null` signifie `non-nan` i.e. non manquant)
#    1. remarquez une colonne entièrement vide

# %%
# votre code
pd.DataFrame.info(df)
#Count est entièrement vide

# %% [markdown]
# 5. 1. utilisez la méthode `dropna` des dataframes  
#      pour supprimer *en place* les colonnes qui ont toutes leurs valeurs manquantes  
#      (et pas uniquement la colonne `'Size'`)
#    2. vérifiez que vous avez bien enlevé la colonne `'Size'`

# %%
# pd.DataFrame.dropna?

# %%
# votre code
df.dropna(axis=1, how='all', inplace=True)
df

# %% [markdown]
# 6. 1. affichez la ligne d'`index` $88$, que remarquez-vous ?
#    2. toutes ses valeurs sont manquantes  
#      utilisez la méthode `dropna` des dataframes  
#      pour supprimer *en place* les lignes qui ont toutes leurs valeurs manquantes
#      (et pas uniquement la ligne d'index $88$)

# %%
# votre code
df.tail(1)

# %%
df.dropna(axis=0, how='all', inplace=True)

# %% [markdown]
# 7. 1. utilisez l'attribut `dtypes` des dataframes pour voir le type de vos colonnes
#    2. que remarquez vous sur la colonne des masses ?

# %%
# votre code
df.dtypes
#la colonne des masses est de type object et non de type float

# %% [markdown]
# 8. 1. la colonne des masses n'est pas de type numérique mais de type `object`  
#       (ici des `str`)   
#    1. utilisez la méthode `unique` des `Series`pour en regarder le contenu
#    2. que remarquez vous ?

# %%
# votre code
df['Mass (lb)'].unique()

# %% [markdown]
# 9. 1. conservez la colonne `'Mass (lb)'` d'origine  
#       (par exemple dans une colonne de nom `'Mass (lb) orig'`)  
#    1. utilisez la fonction `pd.to_numeric` pour convernir  la colonne `'Mass (lb)'` en numérique    
#    (en remplaçant  les valeurs invalides par la valeur manquante)
#    1. naturellement vous vérifiez votre travail en affichant le type de la série `df['Mass (lb)']`

# %%
# votre code
df['Mass (lb) orig'] = df['Mass (lb)']
df['Mass (lb)'] = pd.to_numeric(df['Mass (lb)'], errors='coerce')
print(df['Mass (lb)'].dtype)

# %% [markdown]
# 10. 1. cette solution ne vous satisfait pas, vous ne voulez perdre aucune valeur  
#        (même au prix de valeurs approchées)  
#     1. vous décidez vaillamment de modifier les `str` en leur enlevant les caractères `<` et `>`  
#        afin de pouvoir en faire des entiers
#     - *hint*  
#        les `pandas.Series` formées de chaînes de caractères sont du type `pandas` `object`  
#        mais elle possèdent un accesseur `str` qui permet de leur appliquer les méthodes python des `str`  
#        (comme par exemple `replace`)
#         ```python
#         df['Mass (lb) orig'].str
#         ```
#         remplacer les `<` et les `>` par des '' (chaîne vide)
#      3. utilisez la méthode `astype` des `Series` pour la convertir finalement en `int` 

# %%
df['Mass (lb) orig']

# %%
df['Mass (lb) orig'] = df['Mass (lb) orig'].astype(str)
#Pour une raison que j'ignore, .str.replace n'a pas marché dans la celleule suivante d'où la nécessité de cette ligne.

# %%
# votre code
df['Mass (lb) orig'] = df['Mass (lb) orig'].str.replace('<', '').str.replace('>', '')
df['Mass (lb) orig'] = df['Mass (lb) orig'].astype(float).astype(int)

# %% [markdown]
# 11. 1. sachant `1 kg = 2.205 lb`  
#    créez une nouvelle colonne `'Mass (kg)'` en convertissant les lb en kg  
#    arrondissez les flottants en entiers en utilisant `astype`

# %%
# votre code
df['Mass (kg)'] = df['Mass (lb)'] / 2.205
df['Mass (kg)'] = df['Mass (kg)'].round().astype(int)

# %% [markdown]
# 12. 1. Quels sont les pays qui ont laissé des objets sur la lune ?
#     2. Combien en ont-ils laissé en pourcentage (pas en nombre) ?  
#      *hint* regardez les paramètres de `value_counts`

# %%
# votre code
n = df['Country'].value_counts()
p = (n / n.sum()) * 100
print(p)

# %% [markdown]
# 13. 1. Quel est le poid total des objets sur la lune en kg ?
#     2. quel est le poids total des objets laissés par les `United States`  ?

# %%
# votre code
m = df['Mass (kg)'].sum()
m_us = df[df['Country'] == 'United States']['Mass (kg)'].sum()

print(f"Poids total des objets sur la Lune : {total_weight} kg")
print(f"Poids total des objets laissés par les États-Unis : {us_weight} kg")

# %% [markdown]
# 14. 1. quel pays a laissé l'objet le plus léger ?  
#      *hint* comme il existe une méthode `min` des séries, il existe une méthode `argmin` 

# %%
# votre code
plus_petit_objet = df['Mass (kg)'].argmin()

# Obtenir le pays associé à cet objet
pays = df.loc[lightest_object_index, 'Country']
plus_petit_objet = df.loc[lightest_object_index, 'Mass (kg)']

# Afficher le résultat
print(f"Le pays qui a laissé l'objet le plus léger est : {lightest_country} avec un poids de {lightest_weight} kg.")

# %% [markdown]
# 15. 1. y-a-t-il un Memorial sur la lune ?  
#      *hint*  
#      en utilisant l'accesseur `str` de la colonne `'Artificial object'`  
#      regardez si une des description contient le terme `'Memorial'`
#     2. quel pays qui a mis ce mémorial ?  

# %%
# votre code
memorial = df[df['Artificial object'].str.contains('Memorial', case=False, na=False)]

# Étape 2 : Vérifier si des mémoriaux existent et afficher le pays
if not memorial.empty:
    pays_memo = memorial['Country'].values[0]
    print(f"Il y a un mémorial sur la Lune, mis par le pays : {memorial_country}.")
else:
    print("Il n'y a pas de mémorial sur la Lune.")


# %% [markdown]
# 16. 1. faites la liste Python des objets sur la lune  
#      *hint*  
#      utilisez la méthode `tolist` des séries

# %%
# votre code
object_on_moon = df['Artificial object'].tolist()

# Afficher la liste
print(object_on_moon)

# %% [markdown]
# ***