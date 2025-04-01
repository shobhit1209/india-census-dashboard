import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
final_df=pd.read_csv("India.csv")
final_df.rename(columns={"Households_with_Internet":"Household With Internet",
                         "Housholds_with_Electric_Lighting":"Households With Electricity",
                         "Literacy_rate":"Literacy Rate",
                         "Sex_ratio":"Sex Ratio"},inplace=True)
list_of_state=list(final_df["State"].unique())
list_of_state.insert(0,"Overall India")
st.set_page_config(layout="wide")
st.sidebar.title("India Data")
selected_state=st.sidebar.selectbox("Select A State",list_of_state)
primary=st.sidebar.selectbox("Select Primary Parameter",list(final_df.columns[6:]))
secondary=st.sidebar.selectbox("Select Secondary Secondary",list(final_df.columns[5:]))
plot=st.sidebar.button("Plot Graph")
if plot:
    st.text("Size Represent Primary Parameter")
    st.text("Color Represents Secondary Parameter")
    if selected_state=="Overall India":
        fig=px.scatter_mapbox(final_df,lat="Latitude",lon="Longitude",zoom=3,size=primary,color=secondary,size_max=35,mapbox_style="carto-positron",width=1200,height=700,hover_name="District")
        st.plotly_chart(fig,use_container_width=True)
    else:
        state_df=final_df[final_df.State==selected_state]
        fig=px.scatter_mapbox(state_df,lat="Latitude",lon="Longitude",zoom=5,size=primary,color=secondary,size_max=35,mapbox_style="carto-positron",width=1200,height=700,hover_name="District")
        st.plotly_chart(fig,use_container_width=True)
        

