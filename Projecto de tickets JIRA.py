class Tickets:
    def __init__(self, status):
        self.status = " "

    def blocked (self):
        print ("El ticke esta bloqueado.")

    def ready_for_acceptance (self):
        print("El ticket fue aceptado")

    def progress (self):
        print("El ticket está en progreso")

    def status_final (self):
        print("")
    
    def info(self):
        status1 = input("Elige el estatus: ")
        if status1 == "blocked":
            Tickets.blocked(self)
        elif status1 == "ready_for_acceptance":
            Tickets.ready_for_acceptance(self)
        elif status1 == "progress":
            Tickets.progress(self)
        else:
            Tickets.status_final(self)

Tickets1 = Tickets('blocked')
Tickets1.info()

