
import numpy as pd
import pandas as pd
import plotly.express as px
import streamlit as st
import io

df = pd.read_csv('data/fifa_eda.csv')
df['Joined'] = df['Joined'].astype(str)
st.set_page_config(layout='wide' , initial_sidebar_state="expanded")

def mainPage():
    st.title('FIFA19 Data Description')
    st.markdown('## Data Head')
    st.write(df.head())
    
    st.markdown("## Descriptive Statstics")
    st.write(df.describe())
    
    st.markdown("## Data Info")
    buffer = io.StringIO()
    df.info(buf=buffer)
    s= buffer.getvalue()
    st.text(s)
    
    st.markdown('## Categorical Distribution')
    c1, c2, c3, c4, c5 = st.columns(5)
    with c1:
        st.write(df['Nationality'].value_counts())
    with c2:
        st.write(df['Club'].value_counts())
    with c3:
        st.write(df['Preferred Foot'].value_counts())
    with c4:
        st.write(df['Position'].value_counts())
    with c5:
        st.write(df['Joined'].value_counts())

def secondPage():
    st.title('FIFA19 Numerical Data Visualization')
    
    st.sidebar.markdown('## Histogram Chart options')
    HistNumColumn = st.sidebar.selectbox('Select Histogram Column', ['Age', 'Overall', 'Potential', 'Value', 'Wage', 'International Reputation', 'Skill Moves', 'Height', 'Weight', 'Release Clause'])
    
    st.sidebar.markdown('## Scatter Chart Options')
    ScattX_Column = st.sidebar.selectbox('Select x-axis column', ['Age', 'Overall', 'Potential', 'Value', 'Wage', 'International Reputation', 'Skill Moves', 'Height', 'Weight', 'Release Clause'])
    ScattY_Column = st.sidebar.selectbox('Select y-axis column', ['Age', 'Overall', 'Potential', 'Value', 'Wage', 'International Reputation', 'Skill Moves', 'Height', 'Weight', 'Release Clause'])
    colorOption = st.sidebar.checkbox('Scatter with color')
    
    st.markdown('## Histogram Chart')
    st.plotly_chart(px.histogram(data_frame=df, x=HistNumColumn, title=HistNumColumn.capitalize() + ' Distribution', labels={HistNumColumn : HistNumColumn.capitalize()}))
    
    if colorOption:
        ColorColumn = st.sidebar.selectbox('Choose color column', ['Nationality', 'Club', 'Preferred Foot', 'Position', 'Joined'])
        st.plotly_chart(px.scatter(data_frame=df, x=ScattX_Column, y=ScattY_Column, color=ColorColumn, hover_data=[ColorColumn], title='corrleation between ' + ScattX_Column.capitalize() + ' and ' + ScattX_Column.capitalize(), labels={ScattX_Column : ScattX_Column.capitalize() , ScattY_Column:ScattY_Column.capitalize()}))
    else:
        st.plotly_chart(px.scatter(data_frame=df, x=ScattX_Column, y=ScattY_Column, title='corrleation between ' + ScattX_Column.capitalize() + ' and ' + ScattY_Column.capitalize(), labels={ScattX_Column : ScattX_Column.capitalize() , ScattY_Column:ScattY_Column.capitalize()}))
    
    
    
    
def thirdPage():
    st.title('FIFA19 Categorical Data Visualization')
    
    st.sidebar.markdown('## Count-Plot Chart Options')
    CountPlotColumn = st.sidebar.selectbox('Select column', ['Nationality', 'Club', 'Preferred Foot', 'Position', 'Joined'])
    CountPlotColor = st.sidebar.checkbox('Count Plot With Color')
    
    if CountPlotColor:
        CountPlotColorColumn = st.sidebar.selectbox('(Count-Plot) Choose color column', ['Nationality', 'Club', 'Preferred Foot', 'Position', 'Joined'])
        st.plotly_chart(px.histogram(data_frame=df, x=CountPlotColumn, color=CountPlotColorColumn, barmode='group', title=CountPlotColumn.capitalize() + 'Distribution', labels={CountPlotColumn : CountPlotColumn.capitalize()}))
    else:
        st.plotly_chart(px.histogram(data_frame=df, x=CountPlotColumn, title=CountPlotColumn.capitalize() + ' Distribution ', labels={CountPlotColumn : CountPlotColumn.capitalize()}))
    
    st.sidebar.markdown('## Bar-Plot Chart Options')
    BarPlot_X_Col = st.sidebar.selectbox('Select Bar X Column', ['Nationality', 'Club', 'Preferred Foot', 'Position', 'Joined'])
    BarPlot_Y_Col = st.sidebar.selectbox('Select Bar Y Column', ['Age', 'Overall', 'Potential', 'Value', 'Wage', 'International Reputation', 'Skill Moves', 'Height', 'Weight', 'Release Clause'])
    BarPlotColor = st.sidebar.checkbox('Bar_Plot With Color')
    
    if BarPlotColor:
        BarPlotColorColumn = st.sidebar.selectbox('(Bar-Plot) Choose color column ', ['Nationality', 'Club', 'Preferred Foot', 'Position', 'Joined'])
        st.plotly_chart(px.bar(data_frame=df, x=BarPlot_X_Col, y=BarPlot_Y_Col, color=BarPlotColorColumn, barmode='group', hover_data=[BarPlotColorColumn], title='Summation of '+BarPlot_Y_Col.capitalize() + ' grouped by '+BarPlot_X_Col.capitalize(), labels={BarPlot_X_Col : BarPlot_X_Col.capitalize(), BarPlot_Y_Col : BarPlot_Y_Col.capitalize()}))
    else:
        st.plotly_chart(px.bar(data_frame=df, x=BarPlot_X_Col, y=BarPlot_Y_Col, title='Summation of '+BarPlot_Y_Col.capitalize() + ' grouped by '+BarPlot_X_Col.capitalize(), labels={BarPlot_X_Col : BarPlot_X_Col.capitalize(), BarPlot_Y_Col : BarPlot_Y_Col.capitalize()}))
    
    
pages_to_funcs = {
    'FIFA19 Data Description' : mainPage,
    'FIFA19 Numerical Charts' : secondPage,
    'FIFA19 Categorical Charts' : thirdPage
}

selected_page = st.sidebar.selectbox('Select Page', pages_to_funcs.keys())
pages_to_funcs[selected_page]()
