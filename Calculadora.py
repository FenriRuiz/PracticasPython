def resolverEcuacion(ecuacion):
    operador = ""
    resOp = 0
    subEc = ""
    iteraciones = ecuacion.count("(")
    op = ["+","-","*","/"]
    
    for i in range(0, iteraciones):
        flag1=0
        flag2=0
        flag3=0
        flag4=0
        for i in ecuacion:
            flag2=flag2+1
            if i == ")":
                flag1=flag2         
                while flag1>0:
                    flag1=flag1-1
                    if ecuacion[flag1] == "(":
                        subEc=ecuacion[flag1:flag2]
                        break
                break
        for i in subEc:
            if i == ")":
                flag4=flag3
                while flag4>0:
                    flag4=flag4-1
                    if subEc[flag4] in op:
                        if subEc[flag4-1] in op:
                            flag4=flag4-1
                            operador=subEc[flag4]
                                      
                        derecha = int(subEc[flag4+1:flag3])
                        izquierda = int(subEc[1:flag4])
                        operador=subEc[flag4]
                        flag4=0
                        
                        if operador == "+":
                            resOp=izquierda+derecha
                        if operador == "-":
                            resOp=izquierda-derecha
                        if operador == "*":
                            resOp=izquierda*derecha                        
                        if operador == "/":
                            resOp=izquierda//derecha
            flag3=flag3+1
        ecuacion=ecuacion.replace(subEc,str(resOp))
    return ecuacion