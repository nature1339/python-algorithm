s = str(input())

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

answer = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

for i in s:
    check_idx = 0   
    for spell in range(len(alphabet)):
      if i == alphabet[spell]:
          check_idx = spell
    answer[check_idx] += 1      
    # answer[alphabet.index(i)] += 1

for i in answer:
    print (i ," " ,end ="")


