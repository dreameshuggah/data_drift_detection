#!/usr/bin/env python
# coding: utf-8

# In[2]:

# cd /Users/dreameshuggah/Documents/Rizal_Analytics/Data_Drift_Detection/
# streamlit run streamlit_data_drift.py 
import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np
from pandasql import sqldf
import asyncio

try:
    asyncio.get_event_loop()
except RuntimeError:
    asyncio.set_event_loop(asyncio.new_event_loop())

from evidently import Report
from evidently.presets import DataDriftPreset

st.set_page_config(page_title="Data Drift Detection Dashboard", page_icon="✨", layout="wide", initial_sidebar_state="expanded")

# --- Custom Premium CSS ---
st.markdown("""
<style>

.stApp {
        #background-color: var(--bg-color);
        background: radial-gradient(circle at top left, #141c2f 0%, #0b0f19 50%, #05080e 100%);
        color: var(--text-main);
        font-family: 'Inter', sans-serif;
    }
    
/* Gradient Title */
.gradient-text {
    background: -webkit-linear-gradient(45deg, #FF6B6B, #5F27CD);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-size: 4.5rem;
    font-weight: 800;
    margin-bottom: 0px;
    padding-bottom: 0px;
}
.subtitle {
    font-size: 1.2rem;
    color: #A0A0A0;
    margin-bottom: 30px;
}
/* Glassmorphism containers (applies to standard st.info, st.success, etc) */
.stAlert {
    background: rgba(255, 255, 255, 0.05); /* very light transparent */
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    border: 1px solid rgba(255, 255, 255, 0.1);
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    border-radius: 12px;
}
</style>
""", unsafe_allow_html=True)

# Main Header
#st.markdown('<p class="gradient-text">✨ Data Drift Analysis Dashboard</p>', unsafe_allow_html=True)
st.title("Data Drift Detection Dashboard")
st.markdown('<p class="subtitle">Detect Data Drift in datasets over time</p>', unsafe_allow_html=True)


# --- Sidebar Setup ---
st.sidebar.markdown('### ⚙️ Configuration')

use_example_files = st.sidebar.checkbox("Use example files", True, 
                                        help="Use in-built example files to demo the app")

st.sidebar.markdown("---")

if use_example_files:
    reference_file = 'small_ref_df.csv'
    current_file = 'small_cur_df.csv'
    reference_df = pd.read_csv(reference_file)
    current_df = pd.read_csv(current_file)
else:
    reference_file = st.sidebar.file_uploader("Upload Reference Data (csv)")
    current_file = st.sidebar.file_uploader("Upload Current Data (csv)")
    
    if reference_file and current_file:
        reference_df = pd.read_csv(reference_file)
        current_df = pd.read_csv(current_file)
    else:
        reference_df = None
        current_df = None

# Proceed if data is available
if (reference_df is not None) and (current_df is not None) and (len(reference_df) > 0) and (len(current_df) > 0):
    
    cols = list(reference_df.columns)
    
    # Elegant Data Previews
    with st.expander("🔍 View Data Samples", expanded=True):
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("#### Reference Data Sample")
            st.dataframe(reference_df.head(), use_container_width=True)
            st.caption(f"Rows: {len(reference_df)} • Columns: {len(cols)}")
        with col2:
            st.markdown("#### Current Data Sample")
            st.dataframe(current_df.head(), use_container_width=True)
            st.caption(f"Rows: {len(current_df)} • Columns: {len(current_df.columns)}")

    st.sidebar.markdown("---")
    st.sidebar.markdown('### 📊 Analysis Settings')
    
    if use_example_files:
        selected_cols = st.sidebar.multiselect('Select Columns for Detection', cols, ['cc_num', 'merchant', 'category', 'amt'])
    else:
        selected_cols = st.sidebar.multiselect('Select Columns for Detection', cols)

    st.sidebar.markdown("---")
    
    # Generate Button
    generate_btn = st.sidebar.button("🚀 Generate Drift Report", type="primary", use_container_width=True)
    
    if generate_btn and selected_cols:
        with st.status("🔮 Analyzing Data Drift... Please wait", expanded=True) as status:
            st.write("Initializing Evidently AI report...")
            data_drift_dataset_report = Report(metrics=[
                                              DataDriftPreset(),
                                              ])
            
            st.write("Processing datasets and calculating drift metrics...")
            snapshot = data_drift_dataset_report.run(reference_data=reference_df[selected_cols], 
                                                     current_data=current_df[selected_cols])
            
            fileName = "data_drift_dataset_report.html"
            st.write("Building final HTML visualization...")
            snapshot.save_html(fileName)
            
            status.update(label="✨ Analysis Complete!", state="complete", expanded=False)
            
        st.success("Successfully generated Data Drift Report.")
        
        # Display HTML
        with open(fileName, 'r', encoding='utf-8') as HtmlFile:
            components.html(HtmlFile.read(), height=2000, scrolling=True)
            
elif not use_example_files:
    st.info("⬅️ Please upload both a Reference and Current CSV file in the sidebar to begin.")
