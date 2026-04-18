nota = float(input('Digite a nota: '))
if nota >= 7:
  print('Apv')
elif nota >= 5 and nota < 7:
  print('Avf')
elif nota <= 3:
  print('Rpv')

avf = nota - 10
print(avf)
