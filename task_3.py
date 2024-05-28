from pathlib import Path
import sys

def main():
    try:
        if len(sys.argv)<2:
            user_input=""
        else:
            user_input=sys.argv[1]

        path=Path(user_input)
        print(path)        

        if path.exists():

            if path.is_dir():
                items=path.iterdir()
                for item in items:
                    print(item)
            else:
                print(f"{path} is a file")

        else:
            print(f"{path.absolute()} not found")
        
    except:"not found"

if __name__ == "__main__":
    main()
