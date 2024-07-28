hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

minutosTotal = ((hour * 3600) + (mins * 60) + (dura * 60))
horaFim = (minutosTotal / 3600) % 24
minutoFim = (minutosTotal / 60) % 60

print(f"O evento iniciou {hour}:{mins} e terminou {int(horaFim)}:{int(minutoFim)}")

# Nesse momento você percebe que precisa voltar a estudar matemática por que ficou
# 2 horas para fazer um exercício básico e no final você mesmo enxerga que existia uma solução
# mais básica que iria demorar 2 minutos pra fazer e você foi pelo caminho mais dificil 👍.
# Esse sou eu btw.