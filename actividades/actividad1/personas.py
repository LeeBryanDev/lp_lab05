# personas.py

fo = open('personas.txt', 'r', encoding='utf-8')

personas = []

for linea in fo:
    linea = linea.strip()
    if linea != '':
        campos = linea.split(';')
        persona = {
            'id': campos[0],
            'nombre': campos[1],
            'apellido': campos[2],
            'fecha_nacimiento': campos[3]
        }
        personas.append(persona)

fo.close()

for persona in personas:
    print('Persona:')
    for clave, valor in persona.items():
        print('  ' + clave + ': ' + valor)
    print()
