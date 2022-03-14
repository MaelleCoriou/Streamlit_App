from xml.etree.ElementInclude import include
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# dataset cars
url = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"

data = pd.read_csv(url)

st.title("Analyse du jeu de données : cars.")

st.write("Exploration du jeu de données :")

st.write("Coup d'oeil sur les 5 premières lignes du data set :")
st.write(data.head())

st.write("Répartition des données :")
st.write(data.describe())

st.write("Types des données et remplissage des colonnes :\n")
st.write(print(pd.DataFrame(data.info())))

def box_plot():
    st.write("Distribution des données par colonnes :")
    
    fig = plt.figure(figsize=(13, 5))
    data.boxplot()
    fig.show()
    st.pyplot(fig)

data_count = pd.DataFrame(data.value_counts()).reset_index()
nb_pays = data_count.groupby("continent")[0].sum().reset_index().rename(columns={0:'total'}).sort_values(by="continent")
nb_year = data_count.groupby("year")[0].sum().reset_index().rename(columns={0:'total'})


def repart_continent_year():
    st.write("Distribution des données par continents et années :")
    
    fig = plt.figure(figsize=(15, 5))

    plt.subplot(1, 2, 1)
    sns.barplot(data=nb_pays, x="continent", y="total", color="#1D3557")

    plt.subplot(1, 2, 2)
    sns.barplot(data=nb_year, x="year", y="total", color="#1D3557")

    plt.tight_layout()
    fig.show()
    st.pyplot(fig)

def repart_violin_continent():
    st.write("Distribution des données de chaque métrique par continent :")
    
    fig = plt.figure(figsize=(18, 15))
    plt.subplot(4, 3, 1)
    sns.violinplot(data=data, x="continent", y=data.columns[0], palette="mako")
    plt.subplot(4, 3, 2)
    sns.violinplot(data=data, x="continent", y=data.columns[1], palette="mako")
    plt.subplot(4, 3, 3)
    sns.violinplot(data=data, x="continent", y=data.columns[2], palette="mako")
    plt.subplot(4, 3, 4)
    sns.violinplot(data=data, x="continent", y=data.columns[3], palette="mako")
    plt.subplot(4, 3, 5)
    sns.violinplot(data=data, x="continent", y=data.columns[4], palette="mako")
    plt.subplot(4, 3, 6)
    sns.violinplot(data=data, x="continent", y=data.columns[5], palette="mako")
    plt.subplot(4, 3, 7)
    sns.violinplot(data=data, x="continent", y=data.columns[6], palette="mako")
    fig.show()
    st.pyplot(fig)

def repart_violin_year():
    st.write("Distribution des données de chaque métrique par années :")
    
    fig = plt.figure(figsize=(18, 15))
    plt.subplot(4, 2, 1)
    sns.violinplot(data=data, x="year", y=data.columns[0], palette="mako")
    plt.xticks(rotation=90)
    plt.subplot(4, 2, 2)
    sns.violinplot(data=data, x="year", y=data.columns[1], palette="mako")
    plt.xticks(rotation=90)
    plt.subplot(4, 2, 3)
    sns.violinplot(data=data, x="year", y=data.columns[2], palette="mako")
    plt.xticks(rotation=90)
    plt.subplot(4, 2, 4)
    sns.violinplot(data=data, x="year", y=data.columns[3], palette="mako")
    plt.xticks(rotation=90)
    plt.subplot(4, 2, 5)
    sns.violinplot(data=data, x="year", y=data.columns[4], palette="mako")
    plt.xticks(rotation=90)
    plt.subplot(4, 2, 6)
    sns.violinplot(data=data, x="year", y=data.columns[5], palette="mako")
    plt.xticks(rotation=90)
    fig.show()
    st.pyplot(fig)

def heatmap_graph():
    st.write("Corrélation des variables :")
    data_corr = data.corr()

    # heatmap de toutes les variables du data_clean
    fig = plt.figure(figsize=(10, 10))
    sns.heatmap(data_corr, annot=True, cmap="vlag")
    fig.show()
    st.pyplot(fig)

def pairplot_graph_year():
    st.write("Corrélation des variables pair plot:\nEvolution par années")  
    fig = plt.figure()
    sns.pairplot(data, hue="year", corner=True)
    plt.xticks(rotation=90)
    fig.show()
    st.pyplot(fig)

def pairplot_graph_continent():
    st.write("Corrélation des variables pair plot:\nEvolution par années")  
    fig = plt.figure()
    sns.pairplot(data, hue="continent", corner=True)
    plt.xticks(rotation=90)
    fig.show()
    st.pyplot(fig)

if __name__ == "__main__":
    box_plot()
    repart_continent_year()
    repart_violin_continent()
    repart_violin_year()
    heatmap_graph()
    pairplot_graph_year()
    pairplot_graph_continent()