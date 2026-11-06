import shutil

total, utilise, libre = shutil.disk_usage("/")

go = 1024 ** 3

print(f"Total  : {total / go:.2f} Go")
print(f"Utilisé: {utilise / go:.2f} Go ({utilise / total * 100:.1f} %)")
print(f"Libre  : {libre / go:.2f} Go")   
