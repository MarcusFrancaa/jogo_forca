def randompalavra(inputopcaousuario):
    import random
    resp=inputopcaousuario

    if resp==1:
        from palavras_forca import animais
        resp=str(random.choice(animais))
        return resp

    elif resp==2:
        from palavras_forca import carros
        resp=str(random.choice(carros))
        return resp

    elif resp==3:
        from palavras_forca import comidas
        resp=str(random.choice(comidas))
        return resp

    elif resp==4:
        from palavras_forca import cidades
        resp=str(random.choice(cidades))
        return resp




