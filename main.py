from system_info import system1
import os

def main():
   try:
      print('[1] - System Info ')
      option = int(input('Select? '))

      if option == 1:
         system1()
      else:
          print("Select a valid option")
   except KeyboardInterrupt:
      print("You close the program. :(")

if __name__ == "__main__":
    main()