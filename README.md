# Duygu Analizi Projesi 

Bu proje, kullanıcıdan alınan metni analiz ederek olumlu, olumsuz veya nötr duygu içerip içermediğini belirler.  
Hugging Face üzerindeki önceden eğitilmiş transformer modeli kullanılmıştır.

---

##  Kullanım

1. Gerekli kütüphaneleri yükleyin:

```bash

pip install -r requirements.txt

2. Python dosyasını çalıştırın:

python sentiment_analysis.py

3. Bu projede aşağıdaki model kullanılmıştır:

Model: distilbert-base-uncased-finetuned-sst-2-english
Kaynak: https://huggingface.co/distilbert/distilbert-base-uncased-finetuned-sst-2-english

Bu model, Stanford Sentiment Treebank (SST-2) veri kümesi üzerinde ince ayar yapılmış bir DistilBERT modelidir.
Metinleri olumlu (POSITIVE) veya olumsuz (NEGATIVE) olarak sınıflandırır.

4. Örnek Çıktı

Cümle: I love this movie!
Duygu: POSITIVE
Skor: 0.998


5. Dosya Yapısı

duygu-analizi/
├── app.py                  
├── sentiment_analysis.py   
├── requirements.txt        
├── README.md               
└── .gitignore              

Katkı

Geliştirmek veya katkıda bulunmak istersen pull request gönderebilirsin.
Her türlü geri bildirime açığım!

