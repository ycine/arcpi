#NARZEDZIE DO ZMIANY NAZW PLIKOW W DANEJ LOKALIZACJI


import os

#Function to rename multiple files


def main():
    i = 0

    for filename in os.listdir(r"C:\Users\Marcin Wiaderkowicz\Desktop\Nowy folder"):
        dst = "Windows10_wall" + str(i) + ".jpg"
        src = 'C:\\Users\\Marcin Wiaderkowicz\\Desktop\\Nowy folder\\' + filename
        dst = 'C:\\Users\\Marcin Wiaderkowicz\\Desktop\\Nowy folder\\' + dst
        print(src)
        # rename() function will
        # rename all the files
        os.rename(src, dst)
        i += 1


# Driver Code
if __name__ == '__main__':
    # Calling main() function
    main()


