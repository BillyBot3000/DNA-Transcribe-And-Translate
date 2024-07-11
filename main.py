# Define Variables
codonList = []
startList = []
newList = []
aminoList = []
used = False
sequence = ""
codon = ""
aminoTable = ""
stop = ""
x = 0
y = 0
dict = {65:85, 84:65, 67:71, 71:67}

#translation stuff
aminoAcids1 = ["UUU","UUC","UUA","UUG","CUU","CUC",
               "CUA","CUG","AUU","AUC","AUA","AUG",
               "GUU","GUC","GUA","GUG","UCU","UCC",
               "UCA","UCG","CCU","CCC","CCA","CCG",
               "ACU","ACC","ACA","ACG","GCU","GCC",
               "GCA","GCG","UAU","UAC","UAA","UAG",
               "CAU","CAC","CAA","CAG","AAU","AAC",
               "AAA","AAG","GAU","GAC","GAA","GAG",
               "UGU","UGC","UGA","UGG","CGU","CGC",
               "CGA","CGG","AGU","AGC","AGA","AGG",
               "GGU","GGC","GGA","GGG"]

aminoAcids2 =["Phenylalanine","Phenylalanine","Leucine","Leucine","Leucine","Leucine",
              "Leucine","Leucine","Isoleucine","Isoleucine","Isoleucine","Methionine (START)",
              "Valine","Valine","Valine","Valine","Serine","Serine",
              "Serine","Serine","Proline","Proline","Proline","Proline",
              "Threonine","Threonine","Threonine","Threonine","Alanine","Alanine",
              "Alanine","Alanine","Tyrosine","Tyrosine","STOP","STOP",
              "Histidine","Histidine","Glutamine","Glutamine","Asparagine","Asparagine",
              "Lysine","Lysine","Asparatic Acid","Asparatic Acid","Glutamic Acid","Glutamic Acid",
              "Cystenine","Cystenine","STOP","Tryptophan","Arginine","Arginine",
              "Arginine","Arginine","Serine","Serine","Arginine","Arginine",
              "Glycine","Glycine","Glycine","Glycine"]

str1 = ""
str2 = ""

#print stuff
print("DNA Transcriber and Translater Version 2 made by William Langdon")

#start program
while(True):
  
  #format sequence
  print("")
  sequence = input("Enter A Sequence:")
  sequence = sequence.upper()
  sequence = sequence.replace(" ","")
  
  #transcribe sequence
  sequence = sequence.translate(dict)
  for i in range(len(sequence)):
    startList.append(sequence[i])
  for i in range(3):
    startList.append(" ")
  for i in range(len(startList) - 3):
    stop = startList[i - 3] + startList[i - 2] + startList[i - 1] 
    possible = startList[i] + startList[i + 1] + startList[i + 2]
    #find start codon
    if(possible == "AUG"):
      used = True
    #find stop codon
    if(x%3 == 0 and x > 2 and (stop == "UAA" or stop == "UAG" or stop == "UGA")):
      used = False
      x = 0
    #append new list
    if(used == True):
      x += 1
      newList.append(startList[i])
  #make codon list
  for i in range(len(newList)//3):
    codon = ""
    codon = newList[i * 3] + newList[i * 3 + 1] + newList[i * 3 + 2]
    codonList.append(codon)

  codon = ""
  for i in range(len(codonList)):
    aminoList.append(aminoAcids2[aminoAcids1.index(codonList[i])])
  #print final result
  print("\n")
  for i in range(len(codonList)):
    if (i+1-y < 10):
      print("0"+str(i+1-y),"|",codonList[i],"|",aminoList[i])
    else:
      print(i+1-y,"|",codonList[i],"|",aminoList[i])
    if(aminoList[i] == "STOP"):
      print("----------END OF PROTEIN----------")
      y = i + 1
      
