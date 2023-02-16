import streamlit as st
import keras
import pandas as pd

st.set_page_config(
    page_title='Stock Prediction Dashboard',
    page_icon = '❤️',
    layout="centered"

)

st.title('Stock Prediction')

df = pd.read_csv("Hello.csv")
st.write(df.head(5))

st.subheader('Customizable Plot')
all_columns_names = df.columns.tolist()
type_of_plots = st.selectbox('Select Type of Plot',["area","bar","line","hist","box","kde"])
selected_columns_names = st.multiselect("Select columns to plot",all_columns_names)


if st.button("Generate Plot"):
    st.success("Generating Customizable Plot {} for {}".format(type_of_plots,selected_columns_names))
        
    # Plot By Streamlit
    if type_of_plots == 'area':
        cust_data = df[selected_columns_names]
        st.area_chart(cust_data)
    elif type_of_plots == 'bar':
        cust_data = df[selected_columns_names]
        st.bar_chart(cust_data)
    elif type_of_plots == 'line':
        cust_data = df[selected_columns_names]
        st.line_chart(cust_data)
    # Custom By 
    elif type_of_plots:
        cust_plot = df[selected_columns_names].plot(kind=type_of_plots)
        st.write(cust_plot)
        st.pyplot()
            
old_model_insured = keras.models.load_model('saved_model.h5',compile=False)
old_model_insured.compile()

with st.container():
    st.markdown('Hello')