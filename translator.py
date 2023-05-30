from deep_translator import GoogleTranslator
def tarjimon(text):
    tarjima=GoogleTranslator(source='auto',target='uz').translate(text)
    return tarjima
def tarjimon1(text):
    tarjima=GoogleTranslator(source='auto',target='en').translate(text)
    return tarjima