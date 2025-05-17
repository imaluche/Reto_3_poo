class producto:
 def __init__(self, nombre, precio): #lo mas elemental
    self.nombre = nombre
    self.precio = precio
 def pedido(ls:list,le:list,lb:list,lp:list,lps:list):
   def añadir_producto(ltest,lend): #secuencia para elegir la comida
    for i in range (len(ltest)):
      print(str(i+1)+ ". "+ str((ltest[i]).nombre))
    d = int(input("indique el numero que desea pedir: "))
    lend.append(ltest[d-1])
    return d
   lf = []
   flag = True
   print(f"bienvenido")
   while flag == True:
        print(f"que desea pedir? (1 para sopas, 2 para ensaladas, 3 para bebidas, 4 para plato central, 5 para postres)")
        opcion = int(input("opcion: "))
        if opcion == 1: 
           print("que sopa desea pedir?")
           añadir_producto(ls,lf)
        if opcion == 2: 
           print("que ensalada desea pedir?")
           q = añadir_producto(le,lf)
           c = (input("desea vinagreta? (si/no)"))
           if c == "si":
              le[q-1].vinagreta(b=True)
        if opcion == 3:
           print("que bebida desea pedir?")
           q = añadir_producto(lb,lf)
           c = (input("desea hielo? (si/no)"))
           if c == "si":
              lb[q-1].hielo(b = True)
           if lb[q-1].jugo == True:
               c= (input("desea azucar? (si/no)"))
               if c == "si":
                  lb[q-1].azucar(b = True)
        if opcion == 4:
           print("que plato central desea pedir?")
           añadir_producto(lp,lf)
        if opcion == 5:
           print("que postre desea pedir?")
           añadir_producto(lps,lf)
        f=input("desea pedir algo mas? (si/no)")
        if f == "no":
           flag = False
           return lf
class sopas(producto): #las sopas son un producto
    def __init__(self, nombre, precio):
        super().__init__(nombre, precio)
        self.tipo = "sopa"
class ensaladas(producto): #las ensaladas son un producto
    def __init__(self, nombre, precio, p:bool=False): #indiciador de poder llevar vinagreta
        super().__init__(nombre, precio)
        self.tipo = "ensalada"
        self.p = p
    def vinagreta(self, b:bool = False):
       if (self.p == False):
          print("esa ensalada no lleva vinagreta")
       if (b == False):
         print("sin vinagreta")
       if (b == True) and (self.p == True):
         print("con vinagreta")
         self.precio += 50
class bebidas(producto): #las bebidas son un producto
    def __init__(self, nombre, precio, jugo:bool = False):
        self.jugo = jugo
        super().__init__(nombre, precio)
        self.tipo = "bebida"
        if self.jugo == True:
           def azucar(self, b:bool = False):
            if b == False:
                print("sin azucar")
            else:
                self.precio = self.precio+50
    def hielo(self, b:bool = False):
       if b == False:
         print("sin hielo")
       else:
         self.precio = self.precio+50
class platocentral(producto): #los platos centrales son un producto
    def __init__(self, nombre, precio):
        super().__init__(nombre, precio)
        self.tipo = "plato central"
class postres(producto): #los postres son un producto
    def __init__(self, nombre, precio):
        super().__init__(nombre, precio)
        self.tipo = "postre"

class cuenta():
    def __init__(self,l:list):
        self.elementos= l
    def total(self):
       t=0
       print(f"Gracias por su visita, sus compras fuerzon las siguientes:")
       for i in (self.elementos):
          print(i.nombre)
       for i in self.elementos:
          t = t + i.precio
       print(f"su total es: {t}")
       prop=input("desea dejar propina? (si/no)")
       if prop == "si":
            propina = int(input("indique el porcentaje de propina que desea dejar: "))
            t = t + (t*propina/100)
            print(f"su total con propina es: {t}, gracias por su visita")          
       else:
          print(f"su total es: {t}, gracias por su visita")
if __name__ == "__main__": 
   menu = producto("menu", 0)
   s1 = sopas("ajiaco", 6000)
   s2 = sopas ("mondongo", 5000)
   s3 = sopas ("sopa de mariscos", 7000)
   lsopas = [s1, s2, s3]
   e1 = ensaladas("ensalda cesar", 2000, p = True)
   e2 = ensaladas("guacamole", 1500)
   e3 = ensaladas("ensalada de la casa", 1000, p = True)
   lensaladas = [e1, e2, e3]
   b1 = bebidas("limonada", 5000, jugo = True)
   b2 = bebidas("cocacola", 4000)
   b3 = bebidas("agua", 2000)
   lbebidas = [b1, b2, b3]
   p1 = platocentral("bandeja paisa", 20000)
   p2 = platocentral("arroz con pollo", 18000)
   p3 = platocentral("churrasco", 25000)
   p4 = platocentral("sobrebarriga", 22000)
   lplatos = [p1, p2, p3, p4]
   pt1 = postres("milhoja", 5000)
   pr2 = postres( "copa de helado", 4000)
   pt3 = postres("torta de cumpleaños", 10000)
   lpostres = [pt1, pr2, pt3]
   r = producto.pedido(lsopas,lensaladas,lbebidas,lplatos,lpostres)
   cuenta1 = cuenta(r)
   cuenta1.total()   
   
   
