import pyfiglet
import sys

def main():
    # Check for command-line arguments
    if len(sys.argv) == 1:
        font = pyfiglet.Figlet(font='random')
    elif len(sys.argv) == 3 and (sys.argv[1] == '-f' or sys.argv[1] == '--font'):
        try:
            font = pyfiglet.Figlet(font=sys.argv[2])
        except pyfiglet.FontNotFound:
            print(f"Error: Font '{sys.argv[2]}' not found.")
            sys.exit(1)
    else:
        print("Usage: python figlet.py [-f FONT] TEXT")
        sys.exit(1)
    
    # Prompt the user for input text
    text = input("Enter text: ")
    
    # Output the text in the desired font
    print(font.renderText(text))

if __name__ == "__main__":
    main()
