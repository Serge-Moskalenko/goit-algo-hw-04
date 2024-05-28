from pathlib import Path

path=Path("./cats_info.txt")

def get_cats_info(path):
    try:
        main_list=[]
        with open(path,"r",encoding="utf-8") as fh:
            for item in fh.readlines():
                items=item.split(",")
                list = [item.replace('\n', '') for item in items]
                object={"id":list[0],"name":list[1],"age":list[2]}
                main_list.append(object)
                
        return main_list
    except:
        return "not found"

print(get_cats_info(path))