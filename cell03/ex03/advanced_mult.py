import sys

def main():
    
    if len(sys.argv) > 1:
    
        print("none$")
        return

    
    i = 0
    while i <= 10:
        
        print(f"Table de {i}: ", end="")
        j = 0
        while j <= 10:
    
            print(i * j, end=" " if j < 10 else "\n")
            j += 1
        i += 1

if __name__ == "__main__":
    main()
