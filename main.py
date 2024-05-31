# version: 1.1
# Author: TheRedmc-Off
# Description: File explorer and downloader from a GitHub repository
# Latest release date: 31/05/2024

import requests
from termcolor import colored
import os
import getpass

blue = '\033[34m'
white = '\033[37m'

banner = f"""{blue}
 ██████╗ ██╗████████╗   ██████╗ ██╗     
██╔════╝ ██║╚══██╔══╝   ██╔══██╗██║     
██║  ███╗██║   ██║█████╗██║  ██║██║     
██║   ██║██║   ██║╚════╝██║  ██║██║     
╚██████╔╝██║   ██║      ██████╔╝███████╗
 ╚═════╝ ╚═╝   ╚═╝      ╚═════╝ ╚══════╝
  {white}- Github repository file downloader
"""

os.system('cls')
print(banner)

try:
    ask_url = input("Enter the username and repository name separated by a space: ")
    print()
    username, repo = ask_url.split()
    url = f"https://api.github.com/repos/{username}/{repo}/git/trees/main?recursive=1"

    response = requests.get(url)
except ValueError:
    print("Error: Invalid input")
    exit()

def print_tree(items, current_path):
    dirs = {}
    files = {}
    dir_counter = 0
    file_counter = 0
    special_dirs = ['.github', '.git', '.config', '.vim', '.idea']

    for item in items:
        path_parts = item['path'].split('/')
        if '/'.join(path_parts[:-1]) == current_path:
            if item['type'] == 'tree':  # "tree" = dir
                dirs[chr(65 + dir_counter) if dir_counter < 26 else 'Z' + chr(65 + dir_counter - 26)] = path_parts[-1]
                dir_counter += 1
            elif item['type'] == 'blob':  # "blob" = file
                files[file_counter + 1] = path_parts[-1]
                file_counter += 1

    for key, value in dirs.items():
        if value in special_dirs:
            print(colored(f"[{key}] {value}", 'blue'))
        else:
            print(colored(f"[{key}] {value}", 'green'))

    for key, value in files.items():
        if value.endswith(('.com', '.exe', '.msi', '.apk')):
            print(colored(f"[{key}] {value}", 'yellow'))
        elif value.endswith('.dll'):
            print(colored(f"[{key}] {value}", 'red'))
        elif value.endswith(('.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', '.odt', '.ods', '.odp')):
            print(colored(f"[{key}] {value}", 'blue'))
        elif value.endswith(('.py', '.cs', '.cpp', '.js', '.java', '.php', '.rb', '.go', '.swift', '.kt', '.rs', '.ts', '.html', '.css')):
            print(colored(f"[{key}] {value}", 'cyan'))
        else:
            print(colored(f"[{key}] {value}", 'magenta'))
    return dirs, files

if response.status_code == 200:
    data = response.json()
    current_path = ''
    while True:
        dirs, files = print_tree(data['tree'], current_path)
        choice = input("\nSelect a directory to enter, a file to download, 'up' to go to parent directory and 'q' to quit: ")
        if choice == 'q':
            break
        elif choice == 'up':
            current_path = '/'.join(current_path.split('/')[:-1])
            os.system('cls')
        elif choice in dirs:
            current_path = '/'.join([current_path, dirs[choice]]).strip('/')
        elif int(choice) in files:
            file_url = f"https://github.com/{username}/{repo}/blob/main/{current_path}/{files[int(choice)]}"
            file_url = file_url.replace('blob', 'raw')
            file_response = requests.get(file_url)
            if file_response.status_code == 200:
                downloads_folder = f"C:\\Users\\{getpass.getuser()}\\Downloads"
                print(f'Downloading file: "{files[int(choice)]}"')
                with open(os.path.join(downloads_folder, files[int(choice)]), 'wb') as f:
                    f.write(file_response.content)
                os.system('cls')
                print(f'File "{files[int(choice)]}" downloaded to "{downloads_folder}"')
            else:
                print(f"Error downloading file: {file_response.status_code}")

else:
    print("Error:", response.status_code)