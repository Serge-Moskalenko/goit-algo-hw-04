from colorama import Fore
from pathlib import Path
import sys

def main():
    try:
        if len(sys.argv)<2:
            user_input=""
        else:
            user_input=sys.argv[1]

        path=Path(user_input)       

        if path.exists():

            if path.is_dir():
                
                items=path.glob("**/*")
                for item in items:
                    if item.is_dir():
                        print(f"{Fore.BLUE}{item}{Fore.RESET}")
                    else:
                        print(f"{Fore.GREEN}{item}{Fore.RESET}")
            else:
                print( f"{Fore.GREEN} {path} is a file{Fore.RESET}")

        else:
            print(f"{path.absolute()} not found")
        
    except:"not found"

if __name__ == "__main__":
    main()
