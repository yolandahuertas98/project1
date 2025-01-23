import re

def normalize_material(value):
    match value.upper():
        case 'ALUMINIO' | 'ALU' | 'AL':
            return 'ALUMINIO'
        case 'HIERRO' | 'SPC' | 'SS400' | 'S275JR' | 'SPH' | 'ACERO' | 'ACERO AL CARBONO':
            return 'HIERRO'
        case 'GALVA' | 'SECC' | 'GALVANIZADO' | 'ACERO GALVANIZADO' :
            return 'GALVANIZADO'
        case 'INOX' | 'INOXIDABLE' | 'SUS' | 'ACERO INOXIDABLE' | '304' | 'INOX 316' | 'INOX 304':
            return 'INOXIDABLE'
        case _:
            return value
        
def clean_convert_thickness(value):
    try:
        # Eliminar 'mm' y espacios
        #value = value.replace('mm', '').strip()
        # Elimina todo lo que no coincida con lo  que esta dentro de la expresion regular y si elimina todo devuelve vacio ''
        value = re.sub('[^0-9,.]', '', str(value))
        # Reemplazar coma por punto
        value = value.replace(',', '.')
        # Convertir a float y formatear a un decimal
        return f"{float(value):.1f}"
    
    except ValueError:
        return value

def clean_convert_units(value):
    try:
         value = re.sub('[^0-9,.]', '', str(value))
         value  = value.replace(',', '.')
         return int(float(value))
    
    except ValueError:
     return value
