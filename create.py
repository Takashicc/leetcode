import os
import re
import shutil


# TODO Refactor
class Color:
    GREEN = '\033[92m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    END = '\033[0m'

    @staticmethod
    def green(text: str) -> str:
        return f'{Color.GREEN}{text}{Color.END}'

    @staticmethod
    def red(text: str) -> str:
        return f'{Color.RED}{text}{Color.END}'

    @staticmethod
    def bold(text: str) -> str:
        return f'{Color.BOLD}{text}{Color.END}'


def red_print(text: str) -> None:
    print(Color.bold(Color.red(text)))


def green_print(text: str) -> None:
    print(Color.bold(Color.green(text)))


def main():
    try:
        while True:
            try:
                num = int(input("Number? (e.g., 242): "))
            except ValueError:
                red_print("Cannot parse to number. Please try again.")
                continue
            break

        while True:
            title = "_".join(
                re.sub(
                    " +",
                    " ",
                    input("Title? (e.g., valid_anagram): ").strip().lower()
                ).split(" ")
            )
            if len(title) == 0:
                red_print("Empty character are not allowed. Please try again.")
                continue
            break

        folder_path = os.path.join(os.path.dirname(__file__), f'{num}_{title}')
        file_path = os.path.join(folder_path, "main.py")
        green_print("Are you sure to create a new folder and a file?")
        green_print(f"Filepath: {file_path}")

        user_input = ''
        while not re.search(r'^[yYnN].*$', user_input):
            user_input = input('Are you sure to create? (y/n): ')

        if re.search(r'^[nN].*$', user_input):
            red_print("Abort...")
            return

        if os.path.exists(folder_path):
            print(f"Folder exists! Try again.\n{folder_path}")
            return

        os.mkdir(folder_path)
        src_file_path = os.path.join(os.path.dirname(__file__), "template.py")
        dst_file_path = file_path
        shutil.copyfile(src_file_path, dst_file_path)
        green_print("File created!")
        green_print(f"Filepath: {dst_file_path}")

    except KeyboardInterrupt:
        red_print("\nAbort...")


if __name__ == '__main__':
    main()
