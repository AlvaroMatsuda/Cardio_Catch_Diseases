mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"kazu.mts@gmail.com\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml
streamlit run cardio_catch_app.py
