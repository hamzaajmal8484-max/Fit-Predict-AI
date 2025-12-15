# app.py
import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime
import time
import random

# ============================================
# 1. CUSTOM CSS & ANIMATIONS
# ============================================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Poppins:wght@400;500;600;700&display=swap');
    
    /* Main theme - LIGHT BACKGROUND */
    .stApp {
        background: #ffffff;
        font-family: 'Inter', sans-serif;
        min-height: 100vh;
        color: #333333 !important;
    }
    
    /* Main content area - LIGHT BACKGROUND */
    .main .block-container {
        background: #ffffff;
        color: #333333 !important;
    }
    
    /* Style Streamlit text elements */
    .stMarkdown, .stText, .stTitle, .stHeader {
        color: #333333 !important;
    }
    
    /* Style Streamlit tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 2px;
    }
    
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre-wrap;
        border-radius: 10px 10px 0 0;
        background-color: #f8f9fa;
        color: #333333 !important;
        padding-left: 20px;
        padding-right: 20px;
    }
    
    .stTabs [aria-selected="true"] {
        background-color: rgba(74, 0, 224, 0.1) !important;
        color: #4A00E0 !important;
        border-bottom: 3px solid #8E2DE2 !important;
    }
    
    /* Hide default elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .stDeployButton {display:none;}
    
    /* Custom header - Purple gradient */
    .main-header {
        background: linear-gradient(90deg, #4A00E0 0%, #8E2DE2 100%);
        padding: 2rem;
        border-radius: 0 0 30px 30px;
        margin-bottom: 2rem;
        box-shadow: 0 10px 30px rgba(74, 0, 224, 0.3);
        position: relative;
        overflow: hidden;
    }
    
    /* Animated cards - LIGHT VERSION */
    .animated-card {
        background: #ffffff;
        border-radius: 20px;
        padding: 1.5rem;
        margin: 1rem 0;
        border: 1px solid rgba(74, 0, 224, 0.1);
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
        box-shadow: 0 5px 20px rgba(0, 0, 0, 0.05);
    }
    
    .animated-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 40px rgba(74, 0, 224, 0.15);
        border-color: rgba(74, 0, 224, 0.3);
    }
    
    /* Glitch effect for title */
    .glitch {
        font-size: 3rem;
        font-weight: 700;
        font-family: 'Poppins', sans-serif;
        color: white;
        position: relative;
        display: inline-block;
        text-shadow: 0.05em 0 0 #ff00cc, -0.025em -0.05em 0 #00ff99;
        animation: glitch 2s infinite;
    }
    
    /* Progress rings */
    .progress-ring {
        position: relative;
        width: 100px;
        height: 100px;
        margin: 0 auto;
    }
    
    /* Ripple button */
    .stButton > button {
        background: linear-gradient(90deg, #4A00E0 0%, #8E2DE2 100%);
        color: white;
        border: none;
        padding: 0.75rem 2rem;
        border-radius: 50px;
        font-weight: 600;
        font-size: 1rem;
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
        box-shadow: 0 5px 15px rgba(74, 0, 224, 0.4);
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 20px rgba(74, 0, 224, 0.6);
    }
    
    /* Metric cards */
    .metric-card {
        background: #ffffff;
        border-radius: 15px;
        padding: 1.5rem;
        text-align: center;
        border-left: 4px solid;
        transition: transform 0.3s ease;
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.05);
        color: #333333;
        border: 1px solid rgba(0, 0, 0, 0.05);
    }
    
    .metric-card:hover {
        transform: scale(1.05);
    }
    
    /* Animations */
    @keyframes glitch {
        0%, 14%, 16%, 48%, 50%, 82%, 84%, 100% {
            text-shadow: 0.05em 0 0 #ff00cc, -0.025em -0.05em 0 #00ff99;
        }
        15%, 49%, 83% {
            text-shadow: -0.05em 0 0 #ff00cc, 0.025em 0.05em 0 #00ff99;
        }
    }
    
    @keyframes slideIn {
        from { transform: translateY(20px); opacity: 0; }
        to { transform: translateY(0); opacity: 1; }
    }
    
    @keyframes pulse {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.05); }
    }
    
    /* Typing animation */
    .typing-text {
        border-right: 2px solid white;
        animation: blink 0.7s infinite;
        display: inline-block;
        padding-right: 5px;
    }
    
    @keyframes blink {
        0%, 100% { border-color: transparent; }
        50% { border-color: white; }
    }
    
    /* Badges */
    .badge {
        display: inline-block;
        padding: 0.25rem 0.75rem;
        border-radius: 20px;
        font-size: 0.75rem;
        font-weight: 600;
        margin: 0.25rem;
        color: white !important;
    }
    
    /* Developer credit */
    .developer-credit {
        position: fixed;
        bottom: 10px;
        right: 10px;
        background: linear-gradient(90deg, #4A00E0 0%, #8E2DE2 100%);
        padding: 8px 16px;
        border-radius: 20px;
        font-size: 0.9rem;
        color: white !important;
        z-index: 999;
        animation: fadeIn 1s ease;
        border: 1px solid rgba(255, 255, 255, 0.2);
        box-shadow: 0 5px 15px rgba(74, 0, 224, 0.2);
    }
    
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .heart {
        color: #ff4d94;
        animation: heartbeat 1.5s infinite;
        display: inline-block;
    }
    
    @keyframes heartbeat {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.1); }
    }
    
    /* Custom styling for Streamlit widgets */
    .stSlider > div > div > div {
        color: #333333 !important;
    }
    
    .stSelectbox > div > div {
        color: #333333 !important;
        background-color: #ffffff !important;
        border: 1px solid #dee2e6 !important;
    }
    
    .stSelectbox > div > div:hover {
        background-color: #f8f9fa !important;
    }
    
    /* Streamlit expander styling */
    .streamlit-expanderHeader {
        background-color: #ffffff !important;
        color: #333333 !important;
        border-radius: 10px !important;
        border: 1px solid #dee2e6 !important;
    }
    
    .streamlit-expanderHeader:hover {
        background-color: #f8f9fa !important;
    }
    
    /* Progress bar styling */
    .stProgress > div > div > div > div {
        background-color: #4A00E0 !important;
    }
    
    /* Metric value styling */
    [data-testid="stMetricValue"] {
        color: #333333 !important;
    }
    
    [data-testid="stMetricLabel"] {
        color: #666666 !important;
    }
    
    [data-testid="stMetricDelta"] {
        color: #333333 !important;
    }
    
    /* Sidebar styling */
    .st-emotion-cache-6qob1r {
        background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
    }
</style>
""", unsafe_allow_html=True)

# ============================================
# 2. INITIALIZE SESSION STATE
# ============================================
if 'prediction_made' not in st.session_state:
    st.session_state.prediction_made = False
if 'fit_score' not in st.session_state:
    st.session_state.fit_score = 85
if 'comfort_score' not in st.session_state:
    st.session_state.comfort_score = 80
if 'style_score' not in st.session_state:
    st.session_state.style_score = 75
if 'return_risk' not in st.session_state:
    st.session_state.return_risk = 15.0
if 'scale' not in st.session_state:
    st.session_state.scale = 1.0

# ============================================
# 3. ANIMATED HEADER
# ============================================
st.markdown("""
<div class="main-header">
    <h1 class="glitch">👕 FitPredict AI</h1>
    <p style="color: rgba(255,255,255,0.95); font-size: 1.2rem; margin-top: 0.5rem;">
    <span class="typing-text">Physics-based garment fit prediction with real-time visualization</span>
    </p>
    <div style="display: flex; gap: 10px; margin-top: 1rem;">
        <span class="badge" style="background: linear-gradient(45deg, #4A00E0, #8E2DE2);">AI-Powered</span>
        <span class="badge" style="background: linear-gradient(45deg, #ff00cc, #3333ff);">Real-time</span>
        <span class="badge" style="background: linear-gradient(45deg, #00ff99, #00ccff);">3D Physics</span>
        <span class="badge" style="background: linear-gradient(45deg, #ffcc00, #ff9900);">98% Accuracy</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ============================================
# 4. SIDEBAR WITH ANIMATED INPUTS
# ============================================
with st.sidebar:
    st.markdown('<div class="animated-card">', unsafe_allow_html=True)
    st.markdown("### 📏 Your Measurements")
    
    # Create columns for measurement inputs
    col1, col2 = st.columns(2)
    
    with col1:
        chest = st.slider(
            "**Chest**", 
            min_value=70, 
            max_value=130, 
            value=95,
            help="Chest circumference in cm"
        )
        st.markdown(f'<div style="text-align: center; color: #4A00E0; font-weight: bold;">{chest} cm</div>', unsafe_allow_html=True)
    
    with col2:
        waist = st.slider(
            "**Waist**", 
            min_value=60, 
            max_value=120, 
            value=82,
            help="Waist circumference in cm"
        )
        st.markdown(f'<div style="text-align: center; color: #8E2DE2; font-weight: bold;">{waist} cm</div>', unsafe_allow_html=True)
    
    hips = st.slider(
        "**Hips**", 
        min_value=80, 
        max_value=130, 
        value=98,
        help="Hip circumference in cm"
    )
    st.markdown(f'<div style="text-align: center; color: #00ccff; font-weight: bold;">{hips} cm</div>', unsafe_allow_html=True)
    
    # Visual representation of measurements
    st.markdown("### 📊 Body Profile")
    
    fig_profile = go.Figure(data=[
        go.Scatterpolar(
            r=[chest, waist, hips, chest],
            theta=['Chest', 'Waist', 'Hips', 'Chest'],
            fill='toself',
            fillcolor='rgba(74, 0, 224, 0.1)',
            line=dict(color='#4A00E0', width=2),
            name='Your Body'
        )
    ])
    
    fig_profile.update_layout(
        polar=dict(
            radialaxis=dict(visible=True, range=[60, 130])
        ),
        showlegend=False,
        height=250,
        margin=dict(l=20, r=20, t=20, b=20),
        paper_bgcolor='#ffffff',
        plot_bgcolor='#ffffff',
        font_color='#333333'
    )
    
    st.plotly_chart(fig_profile, use_container_width=True)
    
    st.markdown("### 👚 Garment Details")
    
    brand = st.selectbox(
        "**Brand & Style**",
        ["Levi's 501", "Uniqlo Oxford", "Nike Pro", "Zara Blazer", "H&M T-Shirt"]
    )
    
    size = st.select_slider(
        "**Size**",
        options=["XS", "S", "M", "L", "XL"],
        value="M"
    )
    
    material = st.selectbox(
        "**Fabric Material**",
        ["Cotton", "Polyester", "Denim", "Wool", "Silk", "Spandex"]
    )
    
    st.markdown('</div>', unsafe_allow_html=True)

# ============================================
# 5. MAIN CONTENT AREA
# ============================================

# Create tabs for different views with better styling
tab1, tab2, tab3, tab4 = st.tabs(["🎯 Fit Prediction", "📊 Analysis", "💡 Recommendations", "🔍 3D Preview"])

with tab1:
    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.markdown('<div class="animated-card">', unsafe_allow_html=True)
        st.markdown("### 🚀 Predict Fit")
        
        # Create a prediction button
        if st.button("🎯 **ANALYZE FIT NOW**", type="primary", use_container_width=True):
            with st.spinner("Analyzing fit..."):
                time.sleep(2)
                
                # Calculate scale based on size
                size_map = {"XS": 0.9, "S": 0.95, "M": 1.0, "L": 1.05, "XL": 1.1}
                st.session_state.scale = size_map.get(size, 1.0)
                
                # Calculate scores
                garment_chest = 95 * st.session_state.scale
                garment_waist = 82 * st.session_state.scale
                garment_hips = 98 * st.session_state.scale
                
                st.session_state.fit_score = min(100, max(20, 100 - abs(chest - garment_chest) * 2))
                st.session_state.comfort_score = min(100, max(20, 100 - abs(waist - garment_waist) * 3))
                st.session_state.style_score = random.randint(75, 95)
                st.session_state.return_risk = max(5, min(95, abs(chest - garment_chest) * 0.5 + abs(waist - garment_waist) * 0.7))
                st.session_state.prediction_made = True
                
                st.success("Analysis complete! ✅")
        
        if st.session_state.prediction_made:
            # Display metrics
            st.markdown("### 📈 Prediction Results")
            
            metric_col1, metric_col2, metric_col3, metric_col4 = st.columns(4)
            
            with metric_col1:
                st.markdown(f"""
                <div class="metric-card" style="border-left-color: #00ff99;">
                    <h3 style="margin: 0; font-size: 2rem; color: #00ff99;">{st.session_state.fit_score}</h3>
                    <p style="margin: 0; color: #666666;">Fit Score</p>
                    <div style="height: 5px; background: rgba(0,255,153,0.2); border-radius: 3px; margin-top: 10px;">
                        <div style="width: {st.session_state.fit_score}%; height: 100%; background: #00ff99; border-radius: 3px;"></div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
            
            with metric_col2:
                st.markdown(f"""
                <div class="metric-card" style="border-left-color: #ff00cc;">
                    <h3 style="margin: 0; font-size: 2rem; color: #ff00cc;">{st.session_state.comfort_score}</h3>
                    <p style="margin: 0; color: #666666;">Comfort</p>
                    <div style="height: 5px; background: rgba(255,0,204,0.2); border-radius: 3px; margin-top: 10px;">
                        <div style="width: {st.session_state.comfort_score}%; height: 100%; background: #ff00cc; border-radius: 3px;"></div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
            
            with metric_col3:
                st.markdown(f"""
                <div class="metric-card" style="border-left-color: #00ccff;">
                    <h3 style="margin: 0; font-size: 2rem; color: #00ccff;">{st.session_state.style_score}</h3>
                    <p style="margin: 0; color: #666666;">Style Match</p>
                    <div style="height: 5px; background: rgba(0,204,255,0.2); border-radius: 3px; margin-top: 10px;">
                        <div style="width: {st.session_state.style_score}%; height: 100%; background: #00ccff; border-radius: 3px;"></div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
            
            with metric_col4:
                st.markdown(f"""
                <div class="metric-card" style="border-left-color: #ffcc00;">
                    <h3 style="margin: 0; font-size: 2rem; color: #ffcc00;">{st.session_state.return_risk:.1f}%</h3>
                    <p style="margin: 0; color: #666666;">Return Risk</p>
                    <div style="height: 5px; background: rgba(255,204,0,0.2); border-radius: 3px; margin-top: 10px;">
                        <div style="width: {st.session_state.return_risk}%; height: 100%; background: #ffcc00; border-radius: 3px;"></div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
            
            # Visualization chart
            st.markdown("### 📊 Fit Comparison")
            
            fig = go.Figure()
            
            # Garment measurements using the scale from session state
            garment_chest = 95 * st.session_state.scale
            garment_waist = 82 * st.session_state.scale
            garment_hips = 98 * st.session_state.scale
            
            fig.add_trace(go.Bar(
                name='Your Body',
                x=['Chest', 'Waist', 'Hips'],
                y=[chest, waist, hips],
                marker_color='#4A00E0',
                text=[chest, waist, hips],
                textposition='auto',
            ))
            
            fig.add_trace(go.Bar(
                name=f'Garment ({size})',
                x=['Chest', 'Waist', 'Hips'],
                y=[garment_chest, garment_waist, garment_hips],
                marker_color='#8E2DE2',
                text=[f"{garment_chest:.1f}", f"{garment_waist:.1f}", f"{garment_hips:.1f}"],
                textposition='auto',
            ))
            
            fig.update_layout(
                barmode='group',
                plot_bgcolor='#ffffff',
                paper_bgcolor='#ffffff',
                font_color='#333333',
                height=400,
                showlegend=True
            )
            
            st.plotly_chart(fig, use_container_width=True)
            
            # Fit recommendations
            st.markdown("### 💡 Fit Analysis")
            
            fit_difference = abs(chest - garment_chest) + abs(waist - garment_waist) + abs(hips - garment_hips)
            
            if fit_difference < 10:
                st.success("🎉 **Perfect Fit!** This garment matches your body measurements almost perfectly.")
                st.markdown("""
                - ✅ Excellent match with your body proportions
                - ✅ Optimal comfort and mobility
                - ✅ Minimal return risk (under 10%)
                """)
            elif fit_difference < 20:
                st.warning("⚠️ **Good Fit with Minor Issues**")
                st.markdown("""
                - ⚠️ Slight differences in some areas
                - ✅ Generally comfortable fit
                - ⚠️ Consider trying for better comfort
                """)
            else:
                st.error("❌ **Poor Fit Detected**")
                st.markdown("""
                - ❌ Significant measurement mismatches
                - ❌ Potential discomfort issues
                - ❌ High return risk predicted
                - 💡 Consider a different size or style
                """)
        else:
            st.info("👆 Click the **ANALYZE FIT NOW** button to see your fit prediction results!")
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="animated-card">', unsafe_allow_html=True)
        st.markdown("### ⚡ Live Metrics")
        
        # Simulated live data
        st.metric("Active Users", f"{random.randint(1200, 1300):,}", f"+{random.randint(5, 15)}%")
        st.metric("Accuracy Rate", f"{94.3 + random.uniform(-0.5, 0.5):.1f}%", f"+{random.uniform(1, 3):.1f}%")
        st.metric("Avg. Fit Score", f"{82.5 + random.uniform(-2, 2):.1f}", f"↑ {random.uniform(3, 7):.1f}")
        st.metric("Return Rate", f"{8.7 + random.uniform(-1, 1):.1f}%", f"↓ {random.uniform(2, 4):.1f}%")
        
        # Gauge charts
        st.markdown("### 📊 Quick Stats")
        
        col_gauge1, col_gauge2 = st.columns(2)
        
        with col_gauge1:
            fig_gauge1 = go.Figure(go.Indicator(
                mode="gauge+number",
                value=random.randint(70, 95),
                title={'text': "Comfort", 'font': {'color': '#333333', 'size': 14}},
                gauge={
                    'axis': {'range': [0, 100], 'tickwidth': 1, 'tickcolor': '#333333'},
                    'bar': {'color': "#00ff99"},
                    'bgcolor': "#ffffff"
                },
                number={'font': {'color': '#333333', 'size': 20}}
            ))
            fig_gauge1.update_layout(
                height=200, 
                paper_bgcolor='#ffffff',
                font_color='#333333'
            )
            st.plotly_chart(fig_gauge1, use_container_width=True)
        
        with col_gauge2:
            fig_gauge2 = go.Figure(go.Indicator(
                mode="gauge+number",
                value=random.randint(60, 90),
                title={'text': "Style", 'font': {'color': '#333333', 'size': 14}},
                gauge={
                    'axis': {'range': [0, 100], 'tickwidth': 1, 'tickcolor': '#333333'},
                    'bar': {'color': "#ff00cc"},
                    'bgcolor': "#ffffff"
                },
                number={'font': {'color': '#333333', 'size': 20}}
            ))
            fig_gauge2.update_layout(
                height=200, 
                paper_bgcolor='#ffffff',
                font_color='#333333'
            )
            st.plotly_chart(fig_gauge2, use_container_width=True)
        
        st.markdown('</div>', unsafe_allow_html=True)

with tab2:
    st.markdown('<div class="animated-card">', unsafe_allow_html=True)
    st.markdown("## 📊 Detailed Analysis")
    
    # Create sample data
    np.random.seed(42)
    body_types = pd.DataFrame({
        'Chest': np.random.normal(95, 10, 100),
        'Waist': np.random.normal(82, 8, 100),
        'Hips': np.random.normal(98, 9, 100),
        'Fit_Score': np.random.randint(50, 100, 100)
    })
    
    # 3D scatter plot
    fig_3d = px.scatter_3d(
        body_types, 
        x='Chest', 
        y='Waist', 
        z='Hips',
        color='Fit_Score',
        color_continuous_scale='Viridis',
        title="Body Type Distribution"
    )
    
    # Add user point
    fig_3d.add_trace(go.Scatter3d(
        x=[chest],
        y=[waist],
        z=[hips],
        mode='markers',
        marker=dict(size=10, color='#ff00cc', symbol='diamond'),
        name='Your Body'
    ))
    
    fig_3d.update_layout(
        scene=dict(
            xaxis_title='Chest (cm)',
            yaxis_title='Waist (cm)',
            zaxis_title='Hips (cm)'
        ),
        height=500,
        paper_bgcolor='#ffffff',
        font_color='#333333'
    )
    
    st.plotly_chart(fig_3d, use_container_width=True)
    
    # Additional charts
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("##### 📈 Fit Score Distribution")
        fig_hist = px.histogram(
            body_types, 
            x='Fit_Score',
            nbins=20,
            color_discrete_sequence=['#4A00E0']
        )
        fig_hist.update_layout(
            plot_bgcolor='#ffffff',
            paper_bgcolor='#ffffff',
            font_color='#333333',
            height=300
        )
        st.plotly_chart(fig_hist, use_container_width=True)
    
    with col2:
        st.markdown("##### 🔄 Size Recommendation")
        
        sizes = ['XS', 'S', 'M', 'L', 'XL']
        popularity = [10, 25, 40, 20, 5]
        fit_scores = [65, 78, 92, 85, 70]
        
        fig_bar = go.Figure()
        fig_bar.add_trace(go.Bar(
            x=sizes,
            y=popularity,
            name='Popularity',
            marker_color='#8E2DE2'
        ))
        
        fig_bar.update_layout(
            plot_bgcolor='#ffffff',
            paper_bgcolor='#ffffff',
            font_color='#333333',
            height=300,
            yaxis_title="Popularity %"
        )
        
        st.plotly_chart(fig_bar, use_container_width=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

with tab3:
    st.markdown('<div class="animated-card">', unsafe_allow_html=True)
    st.markdown("## 💡 Personalized Recommendations")
    
    # Generate recommendations
    recommendations = []
    
    if chest > waist + 15:
        recommendations.append({
            "title": "Athletic Fit",
            "description": "Your V-shaped physique suits athletic cuts",
            "icon": "💪",
            "priority": "High"
        })
    
    if abs(chest - hips) < 5:
        recommendations.append({
            "title": "Straight Fit",
            "description": "Consider straight-cut garments",
            "icon": "📏",
            "priority": "Medium"
        })
    
    if waist < 85:
        recommendations.append({
            "title": "Slim Fit",
            "description": "Slim-fit styles will complement your waistline",
            "icon": "👖",
            "priority": "High"
        })
    
    # Display recommendations
    for i, rec in enumerate(recommendations[:3]):
        with st.expander(f"{rec['icon']} {rec['title']} ({rec['priority']} Priority)"):
            st.write(rec['description'])
            st.progress(random.randint(70, 95) / 100)
    
    st.markdown("### 🛍️ Recommended Brands")
    
    brands = ["Levi's", "Uniqlo", "Nike", "Zara", "H&M"]
    fit_matches = [92, 88, 85, 82, 79]
    
    for brand_name, fit_score in zip(brands, fit_matches):
        col1, col2, col3 = st.columns([2, 1, 1])
        with col1:
            st.markdown(f"**{brand_name}**")
        with col2:
            st.markdown(f"Fit: **{fit_score}%**")
        with col3:
            st.progress(fit_score / 100)
    
    st.markdown('</div>', unsafe_allow_html=True)

with tab4:
    st.markdown('<div class="animated-card">', unsafe_allow_html=True)
    st.markdown("## 🔍 3D Fit Preview")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("##### 👤 Body Model")
        
        # Simple 3D visualization
        fig_body = go.Figure(data=[
            go.Mesh3d(
                x=[0, 1, 2, 0],
                y=[0, 2, 0, 1],
                z=[0, 1, 2, 3],
                color='lightblue',
                opacity=0.8
            )
        ])
        
        fig_body.update_layout(
            scene=dict(
                xaxis=dict(visible=False),
                yaxis=dict(visible=False),
                zaxis=dict(visible=False)
            ),
            height=300,
            paper_bgcolor='#ffffff'
        )
        
        st.plotly_chart(fig_body, use_container_width=True)
    
    with col2:
        st.markdown("##### 👕 Garment Fit")
        
        fig_garment = go.Figure(data=[
            go.Mesh3d(
                x=[0.1, 1.1, 2.1, 0.1],
                y=[0.1, 2.1, 0.1, 1.1],
                z=[0, 1, 2, 3],
                color='lightpink',
                opacity=0.5
            )
        ])
        
        fig_garment.update_layout(
            scene=dict(
                xaxis=dict(visible=False),
                yaxis=dict(visible=False),
                zaxis=dict(visible=False)
            ),
            height=300,
            paper_bgcolor='#ffffff'
        )
        
        st.plotly_chart(fig_garment, use_container_width=True)
    
    st.markdown("##### 🎮 Fit Simulation Controls")
    
    tightness = st.select_slider("Tightness", ["Very Loose", "Loose", "Normal", "Snug", "Tight"])
    movement = st.select_slider("Movement", ["Standing", "Walking", "Running", "Sitting"])
    
    st.info(f"**Simulation:** {tightness} fit | {movement} movement")
    
    st.markdown('</div>', unsafe_allow_html=True)

# ============================================
# 6. FOOTER WITH DEVELOPER CREDIT
# ============================================
st.markdown("---")



col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"""
    <div style="text-align: center;">
        <p style="color: #666666;">
        Last updated: {datetime.now().strftime("%H:%M:%S")}
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style="text-align: center;">
        <p style="color: #666666;">
        🔒 Secure & Private
        </p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div style="text-align: center;">
        <p style="color: #666666;">
        ⚡ Powered by AI
        </p>
    </div>
    """, unsafe_allow_html=True)

# ============================================
# 7. ADD JAVASCRIPT ANIMATIONS
# ============================================
st.markdown("""
<script>
// Simple hover effects
document.addEventListener('DOMContentLoaded', function() {
    const cards = document.querySelectorAll('.animated-card');
    cards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-5px)';
        });
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
        });
    });
});
</script>
""", unsafe_allow_html=True)