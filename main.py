listgood = [ ]
listmid = [ ]
listbad = [ ]
N = int(input("Cik ir skolēnu? "))
for x in range(N):
  x = int(input("Ievadi visu prieksmetu vidējo atzīmi: "))
  if x > 8:
    listgood.append(x)
  if 3 < x < 9:
    listmid.append(x)
  if x < 4:
    listbad.append(x)
print("Teicamnieku ir:")
print(len(listgood))
print("Viduvēji mācās: ")
print(len(listmid))
print("Nesekmīgo skolēnu ir: ")
print(len(listbad))