
import random

#Consejos:
def gen_advice():
    advice = ["¿Sabias que, apagar las luces y desconectar algunos electrodomésticos cuando no estén en uso pueden reducir el consumo de energía un 20%?",
            "Recuerda cerrar el grifo cuando te cepilles los dientes, ¡esto puede ahorrar hasta 4 galones de agua al día!", 
            "Cambia las bolsas plásticas por bolsas biodegradables o reutilizables para tus compras, ¡así reducirás mucho tu consumo de plástico!", 
            "Siempre ten en cuenta las tres R, 'Reduce', 'Reutiliza', y 'Recicla'; Reduce la cantidad de residuos que generes, Reutiliza lo que puedas, y recicla lo que no puedes utilizar. ", ]
    return random.choice(advice)



