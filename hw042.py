def get_cats_info(path):
    cats_info = []

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    cat_id, name, age = line.strip().split(',')
                    cat_dict = {
                        "id" : cat_id,
                        "name" : name,
                        "age": int(age)
                    }
                    cats_info.append(cat_dict)
                except ValueError as e:
                    print(f"Помилка обробки рядка: {line}. {e}")
        return cats_info
    except FileNotFoundError as e:
        print(f"Файл за шляхом {path} не знайдено.")
        return []
    
    except Exception as e:
        print(f"Виникла помилка: {e}")
        return []

                
def create_cats_file(path):
    content = """60b90c1c13067a15887e1ae1,Tayson,3
60b90c2413067a15887e1ae2,Vika,1
60b90c2e13067a15887e1ae3,Barsik,2
60b90c3b13067a15887e1ae4,Simon,12
60b90c4613067a15887e1ae5,Tessi,5"""
    
    with open(path, 'w', encoding='utf-8') as file:
        file.write(content)

path_to_file = 'cats_file.txt'
create_cats_file(path_to_file)   

cats_info = get_cats_info(path_to_file)
for cat in cats_info:
    print(cats_info)

