hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

minutosTotal = ((hour * 60) + mins + dura)
horaFim = (minutosTotal / 60) % 24
minutoFim = minutosTotal % 60

print(f"O evento iniciou {hour}:{mins} e terminou {int(horaFim)}:{int(minutoFim)}")