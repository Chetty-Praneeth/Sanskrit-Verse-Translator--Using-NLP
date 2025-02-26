from googletrans import Translator

translator = Translator()

def translate(text, dest):
    # If the destination is Hindi, translate directly
    if dest == "hi":
        return translator.translate(text, src='auto', dest='hi').text

    # If the destination is English, translate directly from Sanskrit
    if dest == "en":
        translation = translator.translate(text, src='auto', dest='hi')
        hi_to_en_translation = translator.translate(translation.text, src='auto', dest='en')
        translated_text =  hi_to_en_translation.text

    # For other languages, do a two-step translation via English
    intermediate_text = translator.translate(text, src='auto', dest='hi')

    hi_to_en_translation = translator.translate(intermediate_text.text, src='auto', dest='en')

    en_to_dest_translation = translator.translate(hi_to_en_translation.text, src='en', dest=dest)

    translated_text = en_to_dest_translation.text

    return translated_text