
data = ["aaaa","aaa"]
i = 0
var = 0
r =len(data)

while True:
    
    if i == (r-1) and var == 0:
        break
    
    if i == (r-1):
        i = 0
        var = 0
    
    if (data[i] < data[i+1]) == False:
        x = data[i]
        data[i] = data[i+1]
        data[i+1] = x
        var+=1
        
        if data[i] == data[i+1]:
            var-=1
    
    i+=1
      
print(data)