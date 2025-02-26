from googletrans import Translator

translator = Translator()

def translate(text,dest):
    if dest == "hi":
        # Translating the Sanskrit text to Hindi
        translation = translator.translate(text, src='auto', dest='hi')
        translated_text =  translation.text
    elif dest == "en":
        #if the destination is english then conert it from sanskrit to hindi and then to english
        # Translate the Sanskrit text to Hindi
        translation = translator.translate(text, src='auto', dest='hi')
        # Translate the Hindi text to English
        hi_to_en_translation = translator.translate(translation.text, src='auto', dest='en')
        translated_text =  hi_to_en_translation.text
    else:
        #For translation other than Hindi
        # Translate the Sanskrit text to Hindi
        translation = translator.translate(text, src='auto', dest='hi')
        # Translate the Hindi text to English
        hi_to_en_translation = translator.translate(translation.text, src='auto', dest='en')
        # Translate the English text to dest
        en_to_dest_translation = translator.translate(hi_to_en_translation.text, src='en', dest=dest)
        translated_text = en_to_dest_translation.text
    return translated_text