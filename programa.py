class Programa:
    def inicio(self, he, st, ar, fo, stp, sf, ind):
        self.header=he
        self.modelostep=st
        self.archivo=ar
        self.footer=fo
        self.nuevostep=stp
        self.step=sf
        self.index=ind
    def nuevoarchivo(self):
        idviejo = 'verXX'
        idnuevo = 'step01'
        token = 'XXpassarpython'
        abrirleerstep = open(self.modelostep,'r')
        leerstep = abrirleerstep.read()
        abrirleerstep.close()
        cambioid = leerstep.replace(idviejo, idnuevo)
        escribirprimero = open(self.nuevostep,'w')
        escribirprimero.write(cambioid)
        escribirprimero.close()
        abrirleertxt = open(self.archivo,'r')
        leertxt = abrirleertxt.read()
        abrirleertxt.close()
        abrirleermodificado = open(self.nuevostep,'r')
        leermodificado = abrirleermodificado.read()
        abrirleermodificado.close()
        cambiostep = leermodificado.replace(token, leertxt)
        escribirsegundo= open(self.step,'w')
        escribirsegundo.write(cambiostep)
        escribirsegundo.close()
    def archivohtml(self):
        abrirheader = open(self.header, 'r')
        header = abrirheader.read()
        abrirheader.close()
        abrirstep = open(self.step, 'r')
        step = abrirstep.read()
        abrirstep.close()
        abrirfooter = open(self.footer, 'r')
        footer = abrirfooter.read()
        abrirfooter.close()
        narchivo = [header,step,footer]
        archivodef= open(self.index,'w')
        for elemento in narchivo:
            archivodef.write(elemento + '\n')
        archivodef.close()

nuevoprograma = Programa()
nuevoprograma.inicio('header.html','modelostep.html','step01.txt','footer.html','previostep.html','step.html','index.html')
nuevoprograma.nuevoarchivo()
nuevoprograma.archivohtml()
