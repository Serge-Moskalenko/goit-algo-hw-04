from pathlib import Path
path=Path("./salary_file.txt")


def total_salary(path):
   total=0
   count=0

   with open(path,"r", encoding="utf-8") as fh:
        for item in fh.readlines():
            count+=1
            items=item.split(",")
            list = [item.strip() for item in items]
            total+=int(list[1])

   average=total/count

   print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")


      
total_salary(path)

# with open("salary_file.txt","r") as fh:
#     print(fh.read())


