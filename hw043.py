import sys
from pathlib import Path
from colorama import Fore, init, Style

def visualize_directory(directory_path, prefix=" "):
    try:
        entries = list(Path(directory_path).iterdir())
    except FileNotFoundError:
        print(Fore.RED + "Помилка: Вказаний шлях не знайдено" + Style.RESET_ALL)
        return
    except NotADirectoryError:
        print(Fore.RED + "Помилка: Вказаний шлях не веде до директорії" + Style.RESET_ALL)
        return

    for entry in entries:
        if entry.is_dir():
            print(prefix + Fore.BLUE + entry.name + '/' + Style.RESET_ALL)
            visualize_directory(entry, prefix + "    ")
        else:
            print(prefix + Fore.GREEN + entry.name + Style.RESET_ALL)

def main():
    init(autoreset=True)

    if len(sys.argv) != 2:
        print(Fore.RED + "Використання: python visualize_directory.py <шлях до директорії>" + Style.RESET_ALL)
        return

    directory_path = sys.argv[1]
    if not Path(directory_path).exists():
        print(Fore.RED + "Помилка: Вказаний шлях не існує" + Style.RESET_ALL)
        return

    if not Path(directory_path).is_dir():
        print(Fore.RED + "Помилка: Вказаний шлях не веде до директорії" + Style.RESET_ALL)
        return

    print(Fore.YELLOW + f"Структура директорії для: {directory_path}" + Style.RESET_ALL)
    visualize_directory(directory_path)

if __name__ == "__main__":
    main()
