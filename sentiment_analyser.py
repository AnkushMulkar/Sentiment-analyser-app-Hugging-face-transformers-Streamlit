import streamlit as st
from transformers import pipeline

st.title('Sentiment Analyser App')
st.subheader("Deployed by [Ankush Mulkar](https://www.linkedin.com/in/ankushmulkar/)")
st.write('This app uses the Hugging Face Transformers [sentiment analyser](https://huggingface.co/course/chapter1/3?fw=tf) library to clasify the sentiment of your input as postive or negative. The web app is built using [Streamlit](https://docs.streamlit.io/en/stable/getting_started.html).')

st.write('*Note: it will take few seconds to run the app.*')
form = st.form(key='sentiment-form')
user_input = form.text_area('Enter your text to see the sentiment')
submit = form.form_submit_button('Submit')

if submit:
    classifier = pipeline("sentiment-analysis")
    result = classifier(user_input)[0]
    label = result['label']
    score = result['score']

    if label == 'POSITIVE':
        st.success(f'{label} sentiment (score: {score})')
    else:
        st.error(f'{label} sentiment (score: {score})')
