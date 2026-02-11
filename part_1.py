sample_bay = ["Basalt", "Silica", "Iron", "Dust"]
new_findings=[]
print(sample_bay[0])
x = len(sample_bay) 
print(sample_bay[x - 1])
print(x)
for salts in sample_bay:
    print(f"transmitting data for:", salts)
while len(new_findings)<3:
    y=input("type of salt?")
    new_findings.append(y)
print(new_findings)
sample_bay.remove("Dust")
print(sample_bay)
  

    
