import streamlit as st 
from duygu_analizi import analiz_yap

st.title("Duygu Analizi Uygulaması")
text = st.text_area("Lütfen analiz edilmesini istediğiniz cümleyi giriniz:", height=150)



if st.button("Analiz Et"):
    if text.strip() != "":
        result = analiz_yap(text)
        st.write(f"**Cümle** {result['text']}")
        st.write(f"**Duygu** {result['label']}")
        st.write(f"**Skor** {result['score']:.3f}")
    else:
        st.warning("Henüz bir cümle girmediniz! Lütfen önce cümle girişi yapın.")



