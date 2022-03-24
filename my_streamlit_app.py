from email.policy import default
from xml.etree.ElementInclude import include
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import plotly.express as px

# dataset cars
url = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"

data = pd.read_csv(url)

st.title("Analyse du jeu de données : Cars.")

st.header("Exploration du jeu de données :")

st.subheader("Coup d'oeil sur les 5 premières lignes du data set :")
st.write(data.head())

st.subheader("Répartition des données :")
st.write(data.describe())

def box_plot():
    st.subheader("Distribution des données par colonne :")
    
    fig = plt.figure(figsize=(13, 5))
    data.boxplot()
    fig.show()
    st.pyplot(fig)

data_count = pd.DataFrame(data.value_counts()).reset_index()
nb_pays = data_count.groupby("continent")[0].sum().reset_index().rename(columns={0:'total'}).sort_values(by="continent")
nb_year = data_count.groupby("year")[0].sum().reset_index().rename(columns={0:'total'})


def repart_continent_year():
    st.subheader("Distribution des données par continent, année :")
    
    fig = plt.figure(figsize=(15, 5))

    plt.subplot(1, 2, 1)
    sns.barplot(data=nb_pays, x="continent", y="total", color="#1D3557")

    plt.subplot(1, 2, 2)
    sns.barplot(data=nb_year, x="year", y="total", color="#1D3557")

    plt.tight_layout()
    fig.show()
    st.pyplot(fig)

def repart_violin_continent():
    st.subheader("Distribution des métriques par continent :")
    
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
    st.subheader("Distribution des métriques par année :")
    
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
    st.header("Etude des corrélations :")
    st.subheader("Corrélation des variables :")
    data_corr = data.corr()
    # heatmap de toutes les variables du data_clean
    fig = plt.figure()
    sns.heatmap(data_corr, annot=True, cmap="vlag")
    fig.show()
    st.pyplot(fig)

def pairplot_graph_year():
    st.subheader("Corrélation des variables pair plot :\nEvolution par année")  
    fig = sns.pairplot(data, hue="year", corner=True, palette="mako")
    plt.xticks(rotation=90)
    st.pyplot(fig)

def pairplot_graph_continent():
    st.subheader("Corrélation des variables pair plot :\nEvolution par continent")  
    fig = sns.pairplot(data, hue="continent", corner=True, palette="mako")
    plt.xticks(rotation=90)
    fig.map_lower(sns.regplot)
    st.pyplot(fig)
    
def select_box():
    option_2 = st.selectbox(
     'Sélectionnez un métrique :',
     (data.columns[:-2]))
    return option_2

def hist_plot_select_continent():
    st.subheader("Evolution d'une métrique par année, continent")
    option_2 = select_box()
    fig = px.scatter(data, x="year", y=option_2,
	         size=option_2, color="continent",
            log_x=True, size_max=50)
    st.plotly_chart(fig)
    
    st.subheader(f"Evolution de {option_2} par année, continent")
    option_4 = st.selectbox(
     'Sélectionnez un continent :',
     (list(data.continent.unique())))
    df = data[data["continent"].str.contains(option_4)]
    fig = px.scatter(
        df, y=option_2, x="year", color=option_2)
    st.plotly_chart(fig)
    
    
    
def scatter_plot_var():
    st.subheader(f"Corrélations entre 2 métriques")
    option_5 = st.selectbox(
     'Sélectionnez une métrique :',
     (data.columns), index=0)
    option_6 = st.selectbox(
     'Sélectionnez une seconde métrique :',
     (data.columns), index=1)
    df = data[[option_5, option_6]]
    fig = px.scatter(
        df , x=option_5, y=option_6, color="continent")
    st.plotly_chart(fig)


if __name__ == "__main__":
    box_plot()
    repart_continent_year()
    repart_violin_continent()
    repart_violin_year()
    heatmap_graph()
    pairplot_graph_year()
    pairplot_graph_continent()
    hist_plot_select_continent()
    scatter_plot_var()
    