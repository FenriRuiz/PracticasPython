def descargarPagina(pagina):
	#https://stackoverflow.com/questions/34192093/python-socket-get
    cliente = socket(AF_INET, SOCK_STREAM)
    #Modificar UCLM_SERVER por el nombre del servidor y 5000, por el puerto del servidor
    cliente.connect((UCLM_SERVER, 5000))
    #"GET / IdPagina HTTP/1.1
    # Host: nombre del host
    #
    #"
    request="GET /"+str(pagina)+" HTTP/1.1\nHost: atclab.esi.uclm.es\n\n"
    cliente.send(request.encode())

    cliente.recv(1024)
    msg = cliente.recv(4096)	
    mensaje = msg.decode()
    #Para mostrar en mensaje en su totalidad eliminar [115:]
    print(mensaje[115:])

    return str(mensaje[115:120])