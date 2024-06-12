var1 = "Rpnd Yjaxd Réhpg, fjt th jcd st adh igth báh vgpcsth rpexipcth st ap Wxhidgxp rdc Patypcsgd Bpvcd n rdc Cpedatóc, th ipbqxéc jcd st adh igth báh rdchxstgpqath wxhidgxpsdgth apixcdh, rdc Rpnd Rgxhed Hpajhixd n rdc Ixid Axkxd, udgbpcsd ta tytbeapg igxjckxgpid sta etgídsd raáhxrd edg tmrtatcrxp, etgídsd ktgspstgpbtcit «ájgtd» st aph atigph apixcph.Hx wph advgpsd aatvpg wphip pfjí, ij gtrdbetchp htgá ap st hpqtg fjt ap rdcigphtñp epgp hjetgpg thit gtid th Ratdepigp. N Yjaxd Réhpg th idsd thid, ixtct ipa hxvcxuxrprxóc, egtrxhpbtcit rdbd wxhidgxpsdg st hí bxhbd, cpggpsdg st hjh egdexph wpopñph vjtggtgph n st hj edaíixrp."


TAM_MAX_CLAVE = 26
 

def obtenerModo():

    while True:

        print('¿Deseas encriptar o desencriptar un mensaje?')

        modo = input().lower()

       	if modo in 'encriptar e desencriptar d'.split():

            return modo

        else:

            print('Ingresa "encriptar" o "e" o "desencriptar" o "d"')



def obtenerMensaje():

     print('Ingresa tu mensaje:')

     return input()



def obtenerClave():

     clave = 0

     while True:

         print('Ingresa el número de clave (1-%s)' % (TAM_MAX_CLAVE))

         clave = int(input())

         if (clave >= 1 and clave <= TAM_MAX_CLAVE):

             return clave



def obtenerMensajeTraducido(modo, mensaje, clave):

    if modo[0] == 'd':

         clave= -clave

    traduccion = ''



    for simbolo in mensaje:

        if simbolo.isalpha():

            num = ord(simbolo)

            num += clave

            if simbolo.isupper():

                if num > ord('Z'):

                    num -= 26

            elif num < ord('A'):

                    num += 26

            elif simbolo.islower():

                if num > ord('z'):

                    num -= 26

                elif num < ord('a'):

                    num += 26


            traduccion += chr(num)
        else:
            traduccion += simbolo
    return traduccion

modo = obtenerModo()

mensaje = obtenerMensaje()

clave = obtenerClave()



print('Tu texto traducido es:')

print(obtenerMensajeTraducido(modo, mensaje, clave))
