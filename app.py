import streamlit as st
import medical_data_visualizer

# title
st.title('Medical Data Visualizer')

st.write("Using data gathered from medical examinations, I created visuals for a project on Free Code Camp. I used the dataset to explore the relationship between cardiac disease, body measurements, blood markers, and lifestyle choices. Hit the show buttons below to see the results")

if st.button('Show Categorical Plot'):
    fig_cat = medical_data_visualizer.draw_cat_plot()
    st.pyplot(fig_cat)

if st.button('Show Heat Map'):
    fig_heat = medical_data_visualizer.draw_heat_map()
    st.pyplot(fig_heat)
