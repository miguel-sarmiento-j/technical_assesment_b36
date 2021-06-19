from libraries.client.config import CONST_SERVER_IP, CONST_SERVER_PORT
from classes.clientClass import clientManager

client=clientManager(CONST_SERVER_IP, CONST_SERVER_PORT)

def main():
    while client.attend():
        continue

if __name__ == "__main__":
    main()