

def extract_unique_code(text):
    # Extracts the unique_code from the sent /start command.
    return text.split()[1] if len(text.split()) > 1 else None


print(extract_unique_code('3M™ FS Головка BH3M-NB-BSP с регулируемым байпасом без кронштейна,соединения резьбы BSP внутр 3/8 дюйма (материал - пластик)'))
