import streamlit as st
import pandas as pd
import os
from io import BytesIO

# Page Configurations
st.set_page_config(page_title="Data Sweeper", layout='wide')

# Custom Styling
st.markdown(
    """
    <style>
    .stApp {
        background-color: #1E1E1E;
        color: #FFFFFF;
    }
    .stButton>button {
        color: #FFFFFF;
        background-color: #4CAF50;
        border-radius: 8px;
        padding: 10px;
        width: 100%;
    }
    .stSelectbox, .stMultiSelect {
        color: #FFFFFF;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title
st.title("📀 Data Sweeper - Sterling Integrator")
st.write("A powerful tool to clean, transform, and visualize CSV & Excel files.")

# File Upload
uploaded_files = st.file_uploader("Upload CSV or Excel files:", type=["csv", "xlsx"], accept_multiple_files=True)

if uploaded_files:
    for file in uploaded_files:
        file_ext = os.path.splitext(file.name)[-1].lower()
        df = pd.read_csv(file) if file_ext == ".csv" else pd.read_excel(file)
        
        st.subheader(f"📂 Preview: {file.name}")
        st.dataframe(df.head())

        # Data Cleaning Options
        st.subheader("🛠 Data Cleaning")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button(f"Remove Duplicates ({file.name})"):
                before = len(df)
                df.drop_duplicates(inplace=True)
                st.success(f"✅ Removed {before - len(df)} duplicate rows!")

        with col2:
            if st.button(f"Fill Missing Values ({file.name})"):
                numeric_cols = df.select_dtypes(include=['number']).columns
                df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
                st.success("✅ Missing values filled with column means!")

        with col3:
            if st.button(f"Remove Rows with Missing Values ({file.name})"):
                before = len(df)
                df.dropna(inplace=True)
                st.success(f"✅ Removed {before - len(df)} rows with missing values!")

        # Column Selection
        st.subheader("🎯 Select Columns")
        selected_columns = st.multiselect(f"Choose columns to keep ({file.name})", df.columns, default=df.columns)
        df = df[selected_columns]

        # Data Visualization
        st.subheader("📊 Data Visualization")
        if st.checkbox(f"Show Visualization ({file.name})"):
            viz_type = st.selectbox("Choose Chart Type", ["Bar Chart", "Line Chart", "Scatter Plot", "Histogram"])
            numeric_columns = df.select_dtypes(include=['number']).columns
            
            if viz_type in ["Bar Chart", "Line Chart", "Histogram"]:
                column = st.selectbox("Select a Numeric Column", numeric_columns)
                
                fig = px.bar(df, y=column, title=f"Bar Chart: {column}") if viz_type == "Bar Chart" else \
                      px.line(df, y=column, title=f"Line Chart: {column}") if viz_type == "Line Chart" else \
                      px.histogram(df, x=column, title=f"Histogram: {column}")
            else:
                x_col, y_col = st.selectbox("X-Axis", numeric_columns), st.selectbox("Y-Axis", numeric_columns)
                fig = px.scatter(df, x=x_col, y=y_col, title=f"Scatter Plot: {x_col} vs {y_col}")
            
            st.plotly_chart(fig, use_container_width=True)

        # File Conversion
        st.subheader("🔄 Convert & Download")
        conversion_type = st.radio(f"Convert {file.name} to:", ["CSV", "Excel"], key=file.name)
        
        if st.button(f"Download {file.name} as {conversion_type}"):
            buffer = BytesIO()
            
            if conversion_type == "CSV":
                df.to_csv(buffer, index=False)
                file_name, mime_type = file.name.replace(file_ext, ".csv"), "text/csv"
            else:
                df.to_excel(buffer, index=False)
                file_name, mime_type = file.name.replace(file_ext, ".xlsx"), "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            
            buffer.seek(0)
            st.download_button("Download File", buffer, file_name=file_name, mime=mime_type)

    st.success("🎉 Processing complete!")
else:
    st.info("Please upload one or more CSV/Excel files to start.")
