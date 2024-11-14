import streamlit as st
import time
import math

# Configure the page
st.set_page_config(
    page_title="Or-feu Music Experience",
    page_icon="🎵",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS with animations and enhanced styling
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Raleway:wght@300;400;700&display=swap');
    
    .stApp {
        background: linear-gradient(45deg, #000428, #004e92);
        font-family: 'Raleway', sans-serif;
    }
    
    /* Animated gradient background */
    @keyframes gradient {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    .main-container {
        background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
        background-size: 400% 400%;
        animation: gradient 15s ease infinite;
        padding: 2rem;
        border-radius: 20px;
        margin: 2rem 0;
    }
    
    .song-title {
        font-size: 4rem;
        font-weight: 700;
        background: linear-gradient(120deg, #ffffff, #a8edea);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin: 2rem 0;
        animation: fadeIn 2s ease;
    }
    
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .player-container {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 2rem;
        margin: 2rem 0;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
        border: 1px solid rgba(255, 255, 255, 0.18);
        animation: slideUp 1s ease;
    }
    
    @keyframes slideUp {
        from { opacity: 0; transform: translateY(50px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .nav-button {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 1rem 2rem;
        border-radius: 50px;
        color: white;
        font-size: 1.2rem;
        transition: all 0.3s ease;
        margin: 0.5rem;
        cursor: pointer;
    }
    
    .nav-button:hover {
        background: rgba(255, 255, 255, 0.2);
        transform: translateY(-2px);
    }
    
    .visualization {
        height: 100px;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 5px;
    }
    
    .bar {
        width: 4px;
        background: rgba(255, 255, 255, 0.8);
        border-radius: 2px;
        transition: height 0.2s ease;
    }
    
    .description {
        color: rgba(255, 255, 255, 0.9);
        font-size: 1.2rem;
        line-height: 1.6;
        text-align: center;
        margin: 2rem 0;
    }
    
    /* Custom scrollbar */
    ::-webkit-scrollbar {
        width: 10px;
    }
    
    ::-webkit-scrollbar-track {
        background: rgba(255, 255, 255, 0.1);
    }
    
    ::-webkit-scrollbar-thumb {
        background: rgba(255, 255, 255, 0.3);
        border-radius: 5px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: rgba(255, 255, 255, 0.5);
    }
    </style>
""", unsafe_allow_html=True)

# Song data with descriptions
songs = {
    "Différent": {
        "url": "https://www.dropbox.com/scl/fi/9d55ik3t507i7gi5fpkbv/Or-feu-diff-rent-_1_.mp3?rlkey=k7pqpnj1udgtv6efd50vkkfn9&dl=1",
        "description": "A journey through sound that challenges perspectives and pushes boundaries. Let the waves of melody carry you to unexplored territories."
    },
    "FIS": {
        "url": "https://www.dropbox.com/scl/fi/f2zslh6rmgq5m9mfeqldf/Or-feu-FIS-deux.mp3?rlkey=pfm0rcefaejllsc5md30awdf3&dl=1",
        "description": "An ethereal blend of rhythms and harmonies that dance between reality and dreams. Experience the fusion of classical and contemporary."
    },
    "La Lune": {
        "url": "https://www.dropbox.com/scl/fi/jhud4knqzyo92bt6opg1e/Or-feu-La-lune-master.mp3?rlkey=54irgk8ybrrbjokpuzdktfrrs&dl=1",
        "description": "Inspired by the mysterious allure of the moon, this piece weaves a tapestry of nocturnal sounds and lunar inspirations."
    }
}

def create_visualization():
    """Create an animated audio visualization"""
    cols = st.columns(32)
    for i in range(32):
        with cols[i]:
            height = 20 + math.sin(time.time() * 5 + i * 0.5) * 15
            st.markdown(f"""
                <div class="bar" style="height: {height}px"></div>
            """, unsafe_allow_html=True)

def main():
    # Navigation buttons at the top
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
            <div style="text-align: center;">
                <button class="nav-button" onclick="window.location.href='#different'">Différent</button>
            </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
            <div style="text-align: center;">
                <button class="nav-button" onclick="window.location.href='#fis'">FIS</button>
            </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
            <div style="text-align: center;">
                <button class="nav-button" onclick="window.location.href='#lune'">La Lune</button>
            </div>
        """, unsafe_allow_html=True)

    # Main content
    selection = st.radio("Select Track", list(songs.keys()), label_visibility="collapsed")
    
    st.markdown(f"""
        <div class="main-container">
            <h1 class="song-title">{selection}</h1>
            
            <div class="player-container">
                <div class="visualization">
    """, unsafe_allow_html=True)
    
    # Audio visualization
    create_visualization()
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Audio player
    st.audio(songs[selection]["url"])
    
    # Song description
    st.markdown(f"""
        <p class="description">{songs[selection]["description"]}</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Additional visual elements
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.markdown("""
            <div style="text-align: center; margin-top: 3rem;">
                <div style="
                    width: 100%;
                    height: 2px;
                    background: linear-gradient(90deg, 
                        rgba(255,255,255,0) 0%,
                        rgba(255,255,255,0.5) 50%,
                        rgba(255,255,255,0) 100%
                    );
                    margin: 2rem 0;
                "></div>
            </div>
        """, unsafe_allow_html=True)

    # Footer
    st.markdown("""
        <footer style="
            text-align: center;
            padding: 2rem;
            color: rgba(255,255,255,0.7);
            font-size: 0.9rem;
        ">
            <p>© 2024 Or-feu Music. Created with love and passion.</p>
        </footer>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
