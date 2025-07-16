from transformers import pipeline

text = input("Lütfen analiz etmek istediğiniz cümleyi giriniz: ")

classifier = pipeline("sentiment-analysis")

result = classifier(text)[0]

print(f"Cümle: {text}")
print(f"Duygu: {result['label']}")
print(f"Skor: {result['score']:.3f}")