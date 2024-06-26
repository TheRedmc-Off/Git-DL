# Git-DL

## Description

This program is a file browser where you can enter folders, exit them, download files and save them.
You only need the username and the repository name to browse it.

## Usage case

You can use this tool to download files from a repository, but it was mainly built to make malware downloadable more easily.
You can find them at: https://github.com/TheRedmc-Off/Malware-Playground

## Installation

To install Git-DL, you can follow these steps:

1. Clone the repository to your local machine.
2. Open a terminal or command prompt and navigate to the cloned repository directory.
3. Run the following command to install the required dependencies:

    ```bash
    pip install requests getpass termcolor
    ```

4. Once the dependencies are installed, you can start the program by running the following command:

    ```bash
    python main.py
    ```

5. The program will prompt you to enter the username and the GitHub repository you want to browse and download files from.
6. Enter these informations and press Enter.
7. The program will display a list of files and directories in the repository.
8. Use the commands on the screen to navigate through the list and press letters or numbers depending on the selected file or directory.
9. If you select a directory, the program will display its contents.
10. If you select a file, the program will download it and save it to your downloads folder.

That's it! You can now use Git-DL to browse and download files from any GitHub repository.