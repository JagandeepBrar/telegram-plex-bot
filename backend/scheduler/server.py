from threading import Thread
from backend import constants
from backend.scheduler import jobs
from backend.scheduler.tasks import notify
import socket
import logging

server_socket = None

def initialize():
    global server_socket
    # Create the server socket, assign the host and port
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((constants.SOCKET_HOST, int(constants.SOCKET_PORT)))
    server_socket.listen(5)
    startServer()

def startServer():
    # Starts the server on a seperate thread since it is an infinite loop waiting for connections
    server_thread = Thread(target=serverListen)
    server_thread.start()
    logging.getLogger(__name__).info("Server socket thread is running")

def stopServer():
    if(server_socket is not None):
        server_socket.close()
        logging.getLogger(__name__).info("Server socket has been closed")

def serverListen():
    while True:
        # Waits for a client to connect, starts a thread for the client
        (client_socket, address) = server_socket.accept()
        client_thread = Thread(target=alertScheduler, args=(client_socket,address))
        client_thread.start()

def alertScheduler(client_socket, address):
    # Receives the data from the client (metadata_id) and sends it to the notifyImmediately job
    metadata_id = client_socket.recv(constants.SOCKET_MAX_MSG_LENGTH)
    jobs.addSingleJob(notify.notifyImmediately, 0, metadata_id)