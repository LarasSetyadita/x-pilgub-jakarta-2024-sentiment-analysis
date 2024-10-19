import streamlit as st
import plost
import pandas as pd

#####################
## import css file ##
#####################

with open('./css/style.css') as f :
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


##########
## Data ##
##########

data = {
    'company': ['Positif', 'Negatif', 'Netral'],
    'jumlah kata': [100, 150, 200],
    'polaritas': [0.1, -0.2, 0.3]
}
data = pd.DataFrame(data)

#################
## page method ##
#################

def bar_chart():
    st.write('barchart')

def donut_chart(selected_theta, data1):
    plost.donut_chart(
        data=data1,
        theta=selected_theta,
        color='company',
        legend='bottom',
        use_container_width=True
    )

#################
## main method ##
#################

def main():
    st.image('./images/pilkada-header-logo.jpg')
    st.title('Analisis Sentiment Pemilihan Gubernur Jakarta 2024')
    st.subheader('Crawlind data didapatkan dari aplikasi X')

    # deskripsi
    st.write('Analisis sentimen ini bertujuan untuk memahami opini publik '
                  'terkait keyword "jakarta menyala" yang berkaitan dengan '
                  'pemilihan gubernur Jakarta 2024. Data dikumpulkan melalui '
                  'crawling dari Twitter, di mana keyword tersebut mungkin '
                  'mencerminkan aspirasi, kritik, atau harapan masyarakat '
                  'terhadap calon gubernur Jakarta. Analisis ini dilakukan '
                  'dengan menggunakan teknik machine learning untuk '
                  'mengkategorikan tweet menjadi sentimen positif, '
                  'negatif, atau netral.')

    # form
    with st.form('form_sentiment'):
        text_input = st.text_area("Let's Try", placeholder="Ketikkan kata atau kalimat")
        submit_button = st.form_submit_button('Analisis')

    if submit_button:
        st.info('Positif')

    col1, col2 = st.columns(2)
    with col1:
        st.sidebar.subheader('Donut chart parameter')
        donut_theta = st.sidebar.selectbox('Select data', ('jumlah kata', 'polaritas'))
        donut_chart(donut_theta, data)
    # with col2:
    #     st.sidebar.subheader('Donut chart parameter')
    #     donut_theta = st.sidebar.selectbox('Select data', ('jumlah kata', 'polaritas'))
    #     donut_chart(donut_theta, data)

    st.markdown('### Metrics')
    col1, col2, col3 = st.columns(3)
    col1.metric("Temperature", "70 °F", "1.2 °F")
    col2.metric("Wind", "9 mph", "-8%")
    col3.metric("Humidity", "86%", "4%")



if __name__ == '__main__':
     main()



