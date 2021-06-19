from libraries.server.config import CONST_SERVER_IP, CONST_SERVER_PORT
from classes.serverClass import ServerManager

server=ServerManager(CONST_SERVER_IP, CONST_SERVER_PORT)

def main():
    while True:
        server.attend()

if __name__ == "__main__":
    main()