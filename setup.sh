mkdir -p ~/.streamlit/
echo "\
[serber]\n\
port=$PORT\n\
enableCORS=false\n\
\n\
" > ~/.streamlit/config.toml
