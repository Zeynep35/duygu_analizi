from transformers import pipeline


classifier = pipeline(
    "sentiment-analysis",
    model = "distilbert/distilbert-base-uncased-finetuned-sst-2-english")

def analiz_yap(text):
    result = classifier(text)[0]

    return {
        "text" : text,
        "label": result['label'],
        "score" : result['score']
    }
