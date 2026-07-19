import streamlit as st
import pandas as pd
from datetime import datetime

# Configure page with SEO optimization
st.set_page_config(
    page_title="AILYN HOUSE - Construction & Payroll Planner",
    page_icon="🏗️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# SEO Meta Tags
st.markdown("""
    <meta name="description" content="Professional construction project management and payroll planning system with receipt tracking and financial dashboard.">
    <meta name="keywords" content="construction management, project planning, receipt tracking, payroll system">
    <meta property="og:title" content="AILYN HOUSE - Construction & Payroll Planner">
    <meta property="og:description" content="Advanced project management platform for construction and payroll">
    <meta name="robots" content="index, follow">
""", unsafe_allow_html=True)

# Custom CSS Styling
st.markdown("""
    <style>
    html, body, [data-testid="stAppViewContainer"] {
        background: linear-gradient(rgba(10, 25, 20, 0.75), rgba(10, 25, 20, 0.75)), 
                    url('https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&w=1920&q=80');
        background-size: cover;
        color: #ffffff;
    }
    
    [data-testid="stMainBlockContainer"] {
        background: rgba(6, 35, 25, 0.4);
        backdrop-filter: blur(10px);
        padding: 40px !important;
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.05);
    }
    
    .header-container {
        text-align: center;
        margin-bottom: 40px;
        padding: 20px;
    }
    
    .header-container h1 {
        color: #22c55e !important;
        font-size: 2.3rem !important;
        font-weight: 700 !important;
        letter-spacing: 1.5px;
        margin: 0;
        text-transform: uppercase;
    }
    
    .header-container p {
        color: #a7f3d0 !important;
        font-weight: 500;
        font-size: 0.9rem;
    }
    
    h2, h3, label {
        color: #22c55e !important;
        font-weight: 600 !important;
    }
    
    .stat-card-container {
        display: flex;
        gap: 20px;
        margin-bottom: 25px;
    }
    
    .stat-card {
        flex: 1;
        background: rgba(6, 25, 18, 0.6);
        border: 1px solid rgba(34, 197, 94, 0.2);
        padding: 20px;
        border-radius: 12px;
    }
    
    .stat-card .label {
        font-size: 0.75rem;
        color: #22c55e;
        text-transform: uppercase;
        font-weight: bold;
    }
    
    .stat-card .value {
        font-size: 1.8rem;
        font-weight: 700;
        color: #ffffff;
    }
    
    div.stButton > button {
        background-color: rgba(10, 45, 30, 0.7) !important;
        color: #22c55e !important;
        border: 1px solid rgba(34, 197, 94, 0.4) !important;
        border-radius: 8px !important;
        font-weight: 600 !important;
        padding: 12px 24px !important;
    }
    
    div.stButton > button:hover {
        background-color: #047857 !important;
        box-shadow: 0 0 15px rgba(34, 197, 94, 0.4) !important;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if "tasks_df" not in st.session_state:
    st.session_state.tasks_df = pd.DataFrame(
        columns=["Date", "Month", "Year", "Day of Week", "Week Number", "Receipt No", "Vendor", "Amount", "Description of Work"]
    )

if "current_page" not in st.session_state:
    st.session_state.current_page = "dashboard"

# Header
st.markdown("""
    <div class="header-container">
        <h1>🏗️ AILYN HOUSE PROJECT & PAYROLL PLANNER</h1>
        <p>Combined System | Mobile Operating Engine v30000</p>
    </div>
""", unsafe_allow_html=True)

# Navigation
col1, col2 = st.columns(2)
with col1:
    if st.button("📊 INPUT DASHBOARD", use_container_width=True):
        st.session_state.current_page = "dashboard"
with col2:
    if st.button("📑 ORGANISED PROJECT LEDGER", use_container_width=True):
        st.session_state.current_page = "ledger"

st.markdown("<br>", unsafe_allow_html=True)

# Month list
month_list = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

# PAGE 1: INPUT DASHBOARD
if st.session_state.current_page == "dashboard":
    st.subheader("📋 Advanced Activity & Receipt Entry")
    
    with st.form("construction_form", clear_on_submit=True):
        day = st.number_input("Day", min_value=1, max_value=31, value=datetime.now().day)
        current_month_idx = datetime.now().month - 1
        month = st.selectbox("Month", options=month_list, index=current_month_idx)
        year = st.number_input("Year", min_value=2020, max_value=2035, value=datetime.now().year)
        
        st.markdown("<hr style='border: 0.5px solid rgba(34, 197, 94, 0.2)'>", unsafe_allow_html=True)
        st.write("🧾 Receipt Tracking Details (Optional)")
        
        col_r1, col_r2, col_r3 = st.columns(3)
        with col_r1:
            receipt_no = st.text_input("Receipt / Invoice Number", placeholder="e.g. OR-10234")
        with col_r2:
            vendor = st.text_input("Vendor / Store Name", placeholder="e.g. Citi Hardware")
        with col_r3:
            amount = st.number_input("Total Receipt Amount (PHP)", min_value=0.0, step=50.0, value=0.0)
        
        st.markdown("<hr style='border: 0.5px solid rgba(34, 197, 94, 0.2)'>", unsafe_allow_html=True)
        desc = st.text_area("Description of Structural/Material Work", placeholder="Specify masonry details, item descriptions, quantities...")
        
        submit_btn = st.form_submit_button("Secure Log Into Ledger")
        
        if submit_btn:
            if not desc.strip():
                st.error("❌ Please input execution details.")
            else:
                try:
                    month_num = month_list.index(month) + 1
                    date_obj = datetime(year, month_num, day)
                    day_name = date_obj.strftime("%A")
                    formatted_date = f"{day:02d}"
                    week_num = f"Week {date_obj.strftime('%U')} ({year})"
                    
                    new_row = {
                        "Date": formatted_date,
                        "Month": month,
                        "Year": str(year),
                        "Day of Week": day_name,
                        "Week Number": week_num,
                        "Receipt No": receipt_no if receipt_no else "N/A",
                        "Vendor": vendor if vendor else "N/A",
                        "Amount": float(amount),
                        "Description of Work": desc
                    }
                    
                    st.session_state.tasks_df = pd.concat(
                        [st.session_state.tasks_df, pd.DataFrame([new_row])],
                        ignore_index=True
                    )
                    st.success("✅ Activity secured in ledger!")
                except ValueError:
                    st.error("❌ Date error. Please verify your Day/Month/Year.")

# PAGE 2: LEDGER
elif st.session_state.current_page == "ledger":
    st.subheader("📊 Quick Stats & Materials Ledger Preview")
    
    total_spent = 0.0 if st.session_state.tasks_df.empty else st.session_state.tasks_df['Amount'].sum()
    
    st.markdown(f"""
        <div class="stat-card-container">
            <div class="stat-card">
                <div class="label">Total Logs Count</div>
                <div class="value">{len(st.session_state.tasks_df)} Entries</div>
            </div>
            <div class="stat-card">
                <div class="label">Total Materials Spent</div>
                <div class="value">PHP {total_spent:,.2f}</div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    if st.session_state.tasks_df.empty:
        st.info("📭 No records yet. Go to INPUT DASHBOARD to create entries.")
    else:
        display_df = st.session_state.tasks_df.copy()
        display_df['Month_Num'] = display_df['Month'].map(lambda m: month_list.index(m) + 1 if m in month_list else 1)
        display_df = display_df.sort_values(by=['Year', 'Month_Num', 'Date']).drop(columns=['Month_Num'])
        
        st.dataframe(display_df, use_container_width=True, hide_index=True)
        
        # HTML Export Function
        def generate_html(dataframe):
            sorted_df = dataframe.copy()
            sorted_df['Month_Num'] = sorted_df['Month'].map(lambda m: month_list.index(m) + 1 if m in month_list else 1)
            sorted_df = sorted_df.sort_values(by=['Year', 'Month_Num', 'Date'])
            
            html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AILYN HOUSE - Project Ledger</title>
    <style>
        body {{
            font-family: 'Segoe UI', Arial, sans-serif;
            background: linear-gradient(rgba(10, 25, 20, 0.85), rgba(10, 25, 20, 0.85)),
                        url('https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&w=1920&q=80');
            background-size: cover;
            color: #ffffff;
            margin: 0;
            padding: 40px;
        }}
        .container {{
            max-width: 1000px;
            margin: 0 auto;
            background: rgba(6, 35, 25, 0.7);
            backdrop-filter: blur(10px);
            padding: 30px;
            border-radius: 12px;
            border: 1px solid rgba(255,255,255,0.05);
        }}
        .header {{
            text-align: center;
            border-bottom: 2px solid #22c55e;
            padding-bottom: 20px;
            margin-bottom: 30px;
        }}
        .header h1 {{
            color: #22c55e;
            margin: 0;
            font-size: 28px;
            text-transform: uppercase;
        }}
        .header p {{
            color: #a7f3d0;
            margin: 5px 0 0 0;
        }}
        .week-section {{
            margin-bottom: 35px;
        }}
        .week-title {{
            background: rgba(34, 197, 94, 0.2);
            border-left: 4px solid #22c55e;
            color: #22c55e;
            padding: 10px 15px;
            font-weight: bold;
            margin-bottom: 12px;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
        }}
        th, td {{
            padding: 12px 15px;
            text-align: left;
            border-bottom: 1px solid rgba(255,255,255,0.05);
        }}
        th {{
            background-color: rgba(10, 35, 25, 0.5);
            color: #22c55e;
            font-weight: bold;
            text-transform: uppercase;
        }}
        tr:nth-child(even) td {{
            background-color: rgba(255,255,255,0.02);
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>AILYN HOUSE PROJECT LEDGER</h1>
            <p>Total Material Expenditures: PHP {total_spent:,.2f}</p>
        </div>
"""
            
            grouped = sorted_df.groupby("Week Number")
            for week, group in grouped:
                html_content += f"""
        <div class="week-section">
            <div class="week-title">📅 {week}</div>
            <table>
                <thead>
                    <tr>
                        <th>Date / Day</th>
                        <th>Receipt & Vendor</th>
                        <th>Description</th>
                    </tr>
                </thead>
                <tbody>
"""
                for _, row in group.iterrows():
                    html_content += f"""
                    <tr>
                        <td>{row['Month']} {row['Date']}, {row['Year']}<br><small style="color:#94a3b8;">{row['Day of Week']}</small></td>
                        <td><b>No:</b> {row['Receipt No']}<br><b>Store:</b> {row['Vendor']}<br><span style='color:#22c55e; font-weight:bold;'>PHP {row['Amount']:,.2f}</span></td>
                        <td>{row['Description of Work']}</td>
                    </tr>
"""
                html_content += """
                </tbody>
            </table>
        </div>
"""
            
            html_content += """
    </div>
</body>
</html>
"""
            return html_content
        
        html_string = generate_html(display_df)
        
        st.download_button(
            label="📥 Export Weekly Ledger as HTML",
            data=html_string,
            file_name=f"ailyn_ledger_{datetime.now().strftime('%Y%m%d')}.html",
            mime="text/html",
            use_container_width=True
        )
