class lampada :
    def __init__(self):
        self.__ligada = False
        print('A lampada instalada (está desligada).')


    def ligar_desligar(self):
        self.__ligada = not self.__ligada

        if self.__ligada:
            print('>> Lampada ligada.')
        else:
            print('>> Lampada desligada.')

    def vrf_est(self):
        return self.__ligada


minha_lampada = lampada()
vrf_est = minha_lampada.vrf_est()

minha_lampada.ligar_desligar()
vrf_est = minha_lampada.vrf_est()

minha_lampada.ligar_desligar()
vrf_est =minha_lampada.vrf_est()

