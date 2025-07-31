"""
CSS Styles for ResiVoice Application
Contains all the custom styling for the Streamlit application
"""

def get_custom_css():
    """Returns the custom CSS styles for the ResiVoice application"""
    return """
    <style>
        body, .stApp {
            background: linear-gradient(135deg, #10141a 60%, #0a232e 100%) !important;
            color: #e0e0e0 !important;
        }
        .stApp {
            min-height: 100vh;
            background-attachment: fixed;
            box-shadow: 0 0 40px #00d4aa33;
        }
        section[data-testid="stSidebar"] {
            background: #181c20 !important;
            color: #e0e0e0 !important;
            border-right: 2px solid #00d4aa22;
        }
        h1, h2, h3, h4 {
            color: #00d4aa !important;
            text-shadow: 0 0 8px #00d4aa55;
        }
        .stButton>button {
            background: #181c20;
            color: #00d4aa;
            border: 1.5px solid #00d4aa;
            border-radius: 8px;
            box-shadow: 0 0 8px #00d4aa44;
            transition: 0.2s;
        }
        .stButton>button:hover {
            background: #00d4aa;
            color: #181c20;
            box-shadow: 0 0 16px #00d4aa99;
        }
    </style>
""" + """
    <style>
        /* Import Google Fonts */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');
        
        /* Global Styles - Dark Theme */
        .main .block-container {
            padding-top: 1rem;
            padding-bottom: 2rem;
            max-width: 1200px;
            background: #0a0a0a;
        }
        
        /* Main Header - Omnidimension Style */
        .main-header {
            font-family: 'Inter', sans-serif;
            font-size: 3.5rem;
            font-weight: 800;
            background: linear-gradient(135deg, #00d4aa 0%, #00b8d4 50%, #00d4aa 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            text-align: center;
            margin-bottom: 2rem;
            letter-spacing: -0.02em;
        }
        
        /* Page Headers */
        .page-header {
            font-family: 'Inter', sans-serif;
            font-size: 2.5rem;
            font-weight: 700;
            color: #ffffff;
            margin-bottom: 2rem;
            text-align: center;
            position: relative;
            padding-bottom: 1rem;
        }
        
        .page-header::after {
            content: '';
            position: absolute;
            bottom: 0;
            left: 50%;
            transform: translateX(-50%);
            width: 80px;
            height: 4px;
            background: linear-gradient(90deg, #00d4aa, #00b8d4);
            border-radius: 2px;
        }
        
        /* Voice Section - Omnidimension Style */
        .voice-section {
            background: linear-gradient(135deg, #1a1a1a 0%, #0f0f0f 100%);
            border: 2px solid #00d4aa;
            border-radius: 16px;
            padding: 3rem 2rem;
            text-align: center;
            color: white;
            margin: 3rem 0;
            box-shadow: 0 0 30px rgba(0, 212, 170, 0.2);
            position: relative;
            overflow: hidden;
        }
        
        .voice-section::before {
            content: '';
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: radial-gradient(circle, rgba(0, 212, 170, 0.1) 0%, transparent 70%);
            animation: float 6s ease-in-out infinite;
        }
        
        @keyframes float {
            0%, 100% { transform: translateY(0px) rotate(0deg); }
            50% { transform: translateY(-20px) rotate(180deg); }
        }
        
        .voice-section h3 {
            font-family: 'Inter', sans-serif;
            font-size: 2rem;
            font-weight: 700;
            margin-bottom: 1rem;
            position: relative;
            z-index: 1;
            color: #00d4aa;
        }
        
        .voice-section p {
            font-family: 'Inter', sans-serif;
            font-size: 1.1rem;
            margin-bottom: 1.5rem;
            position: relative;
            z-index: 1;
            color: #e0e0e0;
        }
        
        /* Voice Button - Omnidimension Style */
        .voice-button {
            background: linear-gradient(135deg, #00d4aa, #00b8d4);
            border: none;
            border-radius: 12px;
            padding: 1.2rem 2.5rem;
            color: #0a0a0a;
            font-family: 'Inter', sans-serif;
            font-size: 1.2rem;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
            position: relative;
            z-index: 1;
            box-shadow: 0 8px 25px rgba(0, 212, 170, 0.3);
        }
        
        .voice-button:hover {
            background: linear-gradient(135deg, #00b8d4, #00d4aa);
            transform: translateY(-2px);
            box-shadow: 0 12px 35px rgba(0, 212, 170, 0.4);
        }
        
        /* Cards - Dark Theme */
        .card {
            background: linear-gradient(135deg, #1a1a1a 0%, #0f0f0f 100%);
            border: 1px solid #333333;
            padding: 2rem;
            border-radius: 16px;
            margin-bottom: 1.5rem;
            box-shadow: 0 8px 32px rgba(0,0,0,0.3);
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
        }
        
        .card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 4px;
            height: 100%;
            background: linear-gradient(180deg, #00d4aa, #00b8d4);
            border-radius: 0 2px 2px 0;
        }
        
        .card:hover {
            transform: translateY(-5px);
            box-shadow: 0 15px 45px rgba(0, 212, 170, 0.2);
            border-color: #00d4aa;
        }
        
        .card h4 {
            font-family: 'Inter', sans-serif;
            font-size: 1.4rem;
            font-weight: 700;
            color: #00d4aa;
            margin-bottom: 1rem;
        }
        
        .card p {
            font-family: 'Inter', sans-serif;
            font-size: 0.95rem;
            color: #e0e0e0;
            line-height: 1.6;
            margin-bottom: 0.5rem;
        }
        
        /* Status Colors - Dark Theme */
        .status-pending { 
            color: #ffa726; 
            font-weight: 600;
            background: rgba(255, 167, 38, 0.1);
            padding: 0.2rem 0.8rem;
            border-radius: 20px;
            font-size: 0.85rem;
            border: 1px solid rgba(255, 167, 38, 0.3);
        }
        .status-processing { 
            color: #00d4aa; 
            font-weight: 600;
            background: rgba(0, 212, 170, 0.1);
            padding: 0.2rem 0.8rem;
            border-radius: 20px;
            font-size: 0.85rem;
            border: 1px solid rgba(0, 212, 170, 0.3);
        }
        .status-resolved { 
            color: #4caf50; 
            font-weight: 600;
            background: rgba(76, 175, 80, 0.1);
            padding: 0.2rem 0.8rem;
            border-radius: 20px;
            font-size: 0.85rem;
            border: 1px solid rgba(76, 175, 80, 0.3);
        }
        .status-rejected { 
            color: #f44336; 
            font-weight: 600;
            background: rgba(244, 67, 54, 0.1);
            padding: 0.2rem 0.8rem;
            border-radius: 20px;
            font-size: 0.85rem;
            border: 1px solid rgba(244, 67, 54, 0.3);
        }
        
        /* Form Styling - Dark Theme */
        .stForm {
            background: linear-gradient(135deg, #1a1a1a 0%, #0f0f0f 100%);
            border: 1px solid #333333;
            padding: 2.5rem;
            border-radius: 16px;
            box-shadow: 0 15px 45px rgba(0,0,0,0.3);
            margin: 2rem 0;
        }
        
        .stForm h3 {
            font-family: 'Inter', sans-serif;
            font-size: 1.8rem;
            font-weight: 700;
            color: #00d4aa;
            margin-bottom: 2rem;
            text-align: center;
        }
        
        /* Feedback Page Specific Styling - Dark Theme */
        .feedback-page .stForm {
            background: linear-gradient(135deg, #1a1a1a 0%, #0f0f0f 100%);
            border: 1px solid #333333;
            box-shadow: 0 15px 45px rgba(0, 0, 0, 0.3);
        }
        
        .feedback-page .stForm h3 {
            color: #00d4aa;
        }
        
        .feedback-page .stButton > button {
            background: linear-gradient(135deg, #00d4aa, #00b8d4);
            box-shadow: 0 8px 25px rgba(0, 212, 170, 0.3);
            color: #0a0a0a;
            font-weight: 700;
        }
        
        .feedback-page .stButton > button:hover {
            background: linear-gradient(135deg, #00b8d4, #00d4aa);
            box-shadow: 0 12px 35px rgba(0, 212, 170, 0.4);
        }
        
        .feedback-page .stTextInput > div > div > input {
            background: #1a1a1a;
            border: 2px solid #333333;
            color: #ffffff;
            border-radius: 8px;
        }
        
        .feedback-page .stTextInput > div > div > input:focus {
            border-color: #00d4aa;
            box-shadow: 0 0 0 3px rgba(0, 212, 170, 0.2);
            background: #0f0f0f;
        }
        
        .feedback-page .stSelectbox > div > div > div {
            background: #1a1a1a;
            border: 2px solid #333333;
            border-radius: 8px;
        }
        
        .feedback-page .stSelectbox > div > div > div:focus-within {
            border-color: #00d4aa;
            box-shadow: 0 0 0 3px rgba(0, 212, 170, 0.2);
        }
        
        .feedback-page .stTextArea > div > div > textarea {
            background: #1a1a1a;
            border: 2px solid #333333;
            color: #ffffff;
            border-radius: 8px;
        }
        
        .feedback-page .stTextArea > div > div > textarea:focus {
            border-color: #00d4aa;
            box-shadow: 0 0 0 3px rgba(0, 212, 170, 0.2);
            background: #0f0f0f;
        }
        
        .feedback-page .card {
            background: linear-gradient(135deg, #1a1a1a 0%, #0f0f0f 100%);
            border: 1px solid #333333;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
        }
        
        .feedback-page .card::before {
            background: linear-gradient(180deg, #00d4aa, #00b8d4);
        }
        
        .feedback-page .card h4 {
            color: #00d4aa;
        }
        
        .feedback-page .card p {
            color: #e0e0e0;
        }
        
        .feedback-page .stBarChart {
            background: linear-gradient(135deg, #1a1a1a 0%, #0f0f0f 100%);
            border: 1px solid #333333;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
        }
        
        .feedback-page .stMetric {
            background: linear-gradient(135deg, #1a1a1a 0%, #0f0f0f 100%);
            border: 1px solid #333333;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
        }
        
        .feedback-page .stMetric > div > div {
            color: #00d4aa;
        }
        
        .feedback-page .page-header::after {
            background: linear-gradient(90deg, #00d4aa, #00b8d4);
        }
        
        /* Input placeholder color */
        .feedback-page .stTextInput > div > div > input::placeholder {
            color: #888888;
            opacity: 0.8;
        }
        
        .feedback-page .stTextArea > div > div > textarea::placeholder {
            color: #888888;
            opacity: 0.8;
        }
        
        /* Label styling */
        .feedback-page label {
            color: #e0e0e0 !important;
            font-weight: 600;
        }
        
        /* Selectbox text color */
        .feedback-page .stSelectbox select {
            color: #ffffff;
        }
        
        /* Button Styling - Omnidimension Style */
        .stButton > button {
            background: linear-gradient(135deg, #00d4aa, #00b8d4);
            border: none;
            border-radius: 12px;
            padding: 0.8rem 2rem;
            font-family: 'Inter', sans-serif;
            font-weight: 600;
            font-size: 1rem;
            color: #0a0a0a;
            transition: all 0.3s ease;
            box-shadow: 0 8px 25px rgba(0, 212, 170, 0.3);
        }
        
        .stButton > button:hover {
            background: linear-gradient(135deg, #00b8d4, #00d4aa);
            transform: translateY(-2px);
            box-shadow: 0 12px 35px rgba(0, 212, 170, 0.4);
        }
        
        /* Input Styling - Dark Theme */
        .stTextInput > div > div > input {
            background: #1a1a1a;
            border-radius: 12px;
            border: 2px solid #333333;
            padding: 0.8rem 1rem;
            font-family: 'Inter', sans-serif;
            transition: all 0.3s ease;
            color: #ffffff;
        }
        
        .stTextInput > div > div > input:focus {
            border-color: #00d4aa;
            box-shadow: 0 0 0 3px rgba(0, 212, 170, 0.1);
            background: #0f0f0f;
        }
        
        .stSelectbox > div > div > div {
            background: #1a1a1a;
            border-radius: 12px;
            border: 2px solid #333333;
            transition: all 0.3s ease;
        }
        
        .stSelectbox > div > div > div:focus-within {
            border-color: #00d4aa;
            box-shadow: 0 0 0 3px rgba(0, 212, 170, 0.1);
        }
        
        .stTextArea > div > div > textarea {
            background: #1a1a1a;
            border-radius: 12px;
            border: 2px solid #333333;
            padding: 1rem;
            font-family: 'Inter', sans-serif;
            transition: all 0.3s ease;
            color: #ffffff;
        }
        
        .stTextArea > div > div > textarea:focus {
            border-color: #00d4aa;
            box-shadow: 0 0 0 3px rgba(0, 212, 170, 0.1);
            background: #0f0f0f;
        }
        
        /* Chart Styling - Dark Theme */
        .stBarChart {
            background: linear-gradient(135deg, #1a1a1a 0%, #0f0f0f 100%);
            border-radius: 16px;
            padding: 1.5rem;
            border: 1px solid #333333;
            box-shadow: 0 8px 32px rgba(0,0,0,0.3);
            margin: 1rem 0;
        }
        
        /* Metric Styling - Dark Theme */
        .stMetric {
            background: linear-gradient(135deg, #1a1a1a 0%, #0f0f0f 100%);
            border-radius: 16px;
            padding: 1.5rem;
            border: 1px solid #333333;
            box-shadow: 0 8px 32px rgba(0,0,0,0.3);
            text-align: center;
        }
        
        .stMetric > div > div {
            font-family: 'Inter', sans-serif;
            font-weight: 700;
            color: #00d4aa;
        }
        
        /* Sidebar Styling - Dark Theme */
        .css-1d391kg {
            background: linear-gradient(180deg, #0a0a0a 0%, #1a1a1a 100%);
        }
        
        /* Success/Error Messages - Dark Theme */
        .stSuccess {
            background: linear-gradient(135deg, #4caf50, #45a049);
            color: white;
            border-radius: 12px;
            padding: 1rem;
            font-family: 'Inter', sans-serif;
            font-weight: 600;
            box-shadow: 0 8px 25px rgba(76, 175, 80, 0.3);
        }
        
        .stError {
            background: linear-gradient(135deg, #f44336, #d32f2f);
            color: white;
            border-radius: 12px;
            padding: 1rem;
            font-family: 'Inter', sans-serif;
            font-weight: 600;
            box-shadow: 0 8px 25px rgba(244, 67, 54, 0.3);
        }
        
        /* Info Messages - Dark Theme */
        .stInfo {
            background: linear-gradient(135deg, #00d4aa, #00b8d4);
            color: #0a0a0a;
            border-radius: 12px;
            padding: 1rem;
            font-family: 'Inter', sans-serif;
            font-weight: 600;
            box-shadow: 0 8px 25px rgba(0, 212, 170, 0.3);
        }
        
        /* Warning Messages - Dark Theme */
        .stWarning {
            background: linear-gradient(135deg, #ffa726, #ff9800);
            color: #0a0a0a;
            border-radius: 12px;
            padding: 1rem;
            font-family: 'Inter', sans-serif;
            font-weight: 600;
            box-shadow: 0 8px 25px rgba(255, 167, 38, 0.3);
        }
        
        /* Navigation Button Styling - Dark Theme */
        .stButton > button {
            background: transparent !important;
            border: none !important;
            color: #e0e0e0 !important;
            font-family: 'Inter', sans-serif !important;
            font-weight: 500 !important;
            font-size: 0.9rem !important;
            text-transform: uppercase !important;
            letter-spacing: 0.5px !important;
            padding: 0.5rem 1rem !important;
            transition: all 0.3s ease !important;
            border-bottom: 2px solid transparent !important;
            border-radius: 0 !important;
            box-shadow: none !important;
        }
        
        .stButton > button:hover {
            background: transparent !important;
            border-bottom-color: #00d4aa !important;
            color: #00d4aa !important;
            transform: none !important;
            box-shadow: none !important;
        }
        
        .stButton > button:focus {
            background: transparent !important;
            border-bottom-color: #00d4aa !important;
            color: #00d4aa !important;
            box-shadow: none !important;
        }
        
        /* Global dark theme overrides */
        .stApp {
            background: #0a0a0a;
        }
        
        .main {
            background: #0a0a0a;
        }
        
        /* Dataframe styling */
        .stDataFrame {
            background: #1a1a1a;
            border: 1px solid #333333;
            border-radius: 8px;
        }
        
        /* Selectbox dropdown styling */
        .stSelectbox > div > div > div > div {
            background: #1a1a1a;
            color: #ffffff;
        }
        
        /* Checkbox styling */
        .stCheckbox > div > div {
            background: #1a1a1a;
            border: 1px solid #333333;
        }
        
        /* Form submit button special styling */
        .stFormSubmitButton > button {
            background: linear-gradient(135deg, #00d4aa, #00b8d4) !important;
            color: #0a0a0a !important;
            font-weight: 700 !important;
        }
        
        .stFormSubmitButton > button:hover {
            background: linear-gradient(135deg, #00b8d4, #00d4aa) !important;
        }
    </style>
""" 