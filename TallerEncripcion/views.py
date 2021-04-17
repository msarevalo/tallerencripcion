from django.http import HttpResponse
import datetime
from cv2 import cv2
import numpy as np
from django.template import Template, Context
from django.template import loader
from PIL import Image as im

def menu(request):
    
    plantilla=open("plantillas/menu.html")
    plt=Template(plantilla.read())
    plantilla.close
    ctx=Context({})

    probando=plt.render(ctx)
    return HttpResponse(probando)

def modularform(request):

    plantilla=open("plantillas/punto1.html")
    plt=Template(plantilla.read())
    plantilla.close
    ctx=Context({})

    probando=plt.render(ctx)
    return HttpResponse(probando)

def punto1(request):

    corrimiento=int(str(request.GET['solicitud']))
    palabra=str(request.GET['cadena'])
    prueba=modular(corrimiento, palabra)
    
    plantilla=open("plantillas/punto1.html")
    plt=Template(plantilla.read())
    plantilla.close
    ctx=Context({'original':palabra,'corrimiento':corrimiento, 'respuesta':prueba})

    probando=plt.render(ctx)
    return HttpResponse(probando)

def modular(corrimiento, palabra):
    abc=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']
    encriptada=[]

    for i in palabra:
        letra = abc.index(i)
        encripcion = (letra+corrimiento)%(len(abc))
        resultado= abc[encripcion]
        encriptada.append(resultado)
    
    return encriptada

def automataform(request):
    plantilla=open("plantillas/punto2.html")
    plt=Template(plantilla.read())
    plantilla.close
    ctx=Context({})

    probando=plt.render(ctx)
    return HttpResponse(probando)

def punto2(request):
    secreta=str(request.GET['secreta'])
    iteraciones=int(str(request.GET['iteraciones']))
    celula=int(str(request.GET['celula']))
    palabra=str(request.GET['cadena'])
    prueba=automata2(secreta,iteraciones,celula,palabra)

    plantilla=open("plantillas/punto2.html")
    plt=Template(plantilla.read())
    plantilla.close

    ctx=Context({'original':palabra,'iteraciones':iteraciones, 'celula':celula, 'secreta':secreta, 'respuesta':prueba})

    probando=plt.render(ctx)
    return HttpResponse(probando)

def automata2(secreta,iteraciones,celula,palabra):
    abc=['#','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4']
    inbinario=""
    secbinario=""

    for i in palabra:
        letra = abc.index(i)
        prueba=bin(letra)
        prueba=prueba[2:]
        while len(prueba)<5:
            prueba="0"+prueba
        inbinario=inbinario+prueba

    for i in secreta:
        letra = abc.index(i)
        prueba=bin(letra)
        prueba=prueba[2:]
        while len(prueba)<5:
            prueba="0"+prueba
        secbinario=secbinario+prueba
    
    iteracion=(len(inbinario)-1)+iteraciones
    contador=1
    llave=""
    p=[]

    while contador<=iteracion:
        q=""
        for i in range(len(secbinario)):
            if i==0:
                s1=secbinario[len(secbinario)-1]
            else:
                s1=secbinario[i-1]
            
            s2=secbinario[i]

            if i==len(secbinario)-1:
                s3=secbinario[0]
            else:
                s3=secbinario[i+1]

            concatenado=str(s1)+str(s2)+str(s3)
            if concatenado=="111":
                resultado=0
            elif concatenado=="110":
                resultado=0
            elif concatenado=="101":
                resultado=0
            elif concatenado=="100":
                resultado=1
            elif concatenado=="011":
                resultado=1
            elif concatenado=="010":
                resultado=1
            elif concatenado=="001":
                resultado=1
            elif concatenado=="000":
                resultado=0
            
            if contador>=iteraciones:
                if i==celula:
                    llave=llave+str(resultado)
            q=q+str(resultado)
        p.append(q)
        secbinario=q
        contador=contador+1

    encriptado=""
    for i in range(len(inbinario)):
        if llave[i]==inbinario[i]:
            encriptado=encriptado+"0"
        else:
            encriptado=encriptado+"1"
    
    salida=""
    letrae=""
    for i in range(len(encriptado)):
        letrae=letrae+encriptado[i]
        if (i+1)%5==0:
            letraencriptada=int(str(letrae),2)
            resultado=abc[letraencriptada]
            salida=salida+str(resultado)
            letrae=""

    return salida

def imagenesform(request):
    plantilla=open("plantillas/punto3.html")
    plt=Template(plantilla.read())
    plantilla.close
    ctx=Context({})

    probando=plt.render(ctx)
    return HttpResponse(probando)

def punto3(request):
    nombre=str(request.GET['nombre'])
    l1=int(str(request.GET['l1']))
    l2=int(str(request.GET['l2']))
    l3=int(str(request.GET['l3']))
    prueba=imagenes(nombre, l1, l2,l3)
    plantilla=open("plantillas/punto3.html")
    plt=Template(plantilla.read())
    plantilla.close
    ctx=Context({'original':nombre,'respuesta':prueba})

    probando=plt.render(ctx)
    return HttpResponse(probando)

def imagenes(nombre, l1, l2, l3):
    ruta="imagenes/"+nombre
    img = cv2.imread(ruta, cv2.IMREAD_GRAYSCALE)
    
    l1=l1
    l2=l2
    l3=l3
    cifrado=[]
    ini1=ini2=inj1=inj2=s1=s2=s3=s4=0

    for i in range(len(img)):
        pixel=[]
        if i==0:
            ini1=len(img)-2
            ini2=len(img)-1
        elif i==1:
            ini1=len(img)-1
            ini2=i-1
        else:
            ini1=i-2
            ini2=i-1
        for j in range(len(img[i])):
            if j==0:
                inj1=len(img[i])-1
                inj2=j+1
            elif j==len(img[i])-1:
                inj1=j-1
                inj2=0
            else:
                inj1=j-1
                inj2=j+1
            s1=img[ini1][j]
            s2=img[ini2][inj1]
            s3=img[ini2][j]
            s4=img[ini2][inj2]
            encriptado=(s1+(s2*l1)+(s3*l2)+(s4*l3))%256
            pixel.append(encriptado)
        cifrado.append(pixel)
    cifrado=np.array(cifrado).astype(np.uint8)
    #cifrado=np.reshape(cifrado, (len(img[0]), len(img)))
    #cifrado.shape
    salida = im.fromarray(cifrado)
    fecha_actual=datetime.datetime.now()
    fecha_actual= str(format(fecha_actual.day))+str(format(fecha_actual.month))+str(format(fecha_actual.year))+str(format(fecha_actual.hour))+str(format(fecha_actual.minute))+ str(format(fecha_actual.second))
    fecha_actual = str(fecha_actual) + ".png"
    salida.save('imagenes_encriptadas/'+str(fecha_actual))
    return fecha_actual