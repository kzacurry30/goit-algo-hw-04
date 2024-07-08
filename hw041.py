def create_salary_file(path):
    content = """Alex Korp,3000
Nikita Borisenko,2000
Sitarama Raju,1000"""
    
    with open(path, 'w', encoding='utf-8') as file:
        file.write(content)

def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            salaries = []
            for line in file:
                try:
                    _, salary = line.strip().split(',')
                    salaries.append(float(salary))
                except ValueError as e:
                    print(f"Помилка обробки рядка: {line}. {e}")


            if not salaries:
                return (0, 0)

            total = sum(salaries)
            average = total / len(salaries)
            return (total, average)

    except FileNotFoundError:
        print(f"Файл за шляхом {path} не знайдено.")
        return (0, 0)
    except Exception as e:
        print(f"Виникла помилка: {e}")
        return (0, 0)


path_to_file = 'salary_file.txt'
create_salary_file(path_to_file)


total, average = total_salary(path_to_file)
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
