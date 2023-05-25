import subprocess
import socket
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


class PingCheckerGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Ping Checker")
        self.server_ip = "127.0.0.1"
        self.server_port = 8000
        self.ping_running = False

        # Create a label and an entry box for the number of packets to send
        count_label = tk.Label(self.master, text="Number of packets to send:")
        count_label.pack()
        self.count = tk.Entry(self.master)
        self.count.pack()
        self.count.insert(0, "5")

        # Create a label for the packet loss status
        packet_loss_title = tk.Label(self.master, text="Packet Loss Status:")
        packet_loss_title.pack()
        self.packet_loss_label = tk.Label(self.master, text="")
        self.packet_loss_label.pack()

        # Create a button to start checking for packet loss
        ping_button = tk.Button(self.master, text="Ping", command=self.start_ping)
        ping_button.pack()

        # Create a button to stop checking for packet loss
        stop_button = tk.Button(self.master, text="Stop", command=self.stop_ping)
        stop_button.pack()

        # Create a figure for the ping graph
        self.ping_fig = Figure(figsize=(8, 5), dpi=100)
        self.ping_ax = self.ping_fig.add_subplot(111)
        self.ping_ax.set_xlabel("Time (s)")
        self.ping_ax.set_ylabel("Ping (ms)")
        self.ping_line, = self.ping_ax.plot([], [])  # Create an empty line plot for the ping data
        self.ping_canvas = FigureCanvasTkAgg(self.ping_fig, master=self.master)
        self.ping_canvas.get_tk_widget().pack()

    def start_ping(self):
        if not self.ping_running:
            self.ping_running = True
            self.ping_loop()

    def stop_ping(self):
        self.ping_running = False

    def ping_loop(self):
        if self.ping_running:
            # Execute the ping command and capture the output
            count = self.count.get()
            ping_output = subprocess.Popen(["ping", "-n", count, self.server_ip], stdout=subprocess.PIPE).communicate()[0]

            # Convert the output to a string
            ping_output_str = ping_output.decode("utf-8")

            # Parse the output to check for packet loss
            if "100% loss" in ping_output_str or "General failure" in ping_output_str:
                self.packet_loss_label.configure(text="Packet loss detected")
            elif "could not find host" in ping_output_str:
                self.packet_loss_label.configure(text="Host Not Found")
            else:
                self.packet_loss_label.configure(text="No packet loss detected")

            # Extract the ping times from the ping output
            ping_times = self.ping_ax.lines[0].get_ydata().tolist()
            for line in ping_output_str.splitlines():
                if "time=" in line:
                    ping_time_str = line.split("time=")[-1].split(" ")[0]
                    if "ms" in ping_time_str:
                        ping_time_str = ping_time_str[:-2]
                    ping_times.append(float(ping_time_str))

            # Update the ping graph with the new ping times
            self.ping_ax.clear()
            self.ping_ax.set_xlabel("Time (s)")
            self.ping_ax.set_ylabel("Ping (ms)")
            self.ping_ax.plot(ping_times)
            self.ping_canvas.draw()

            # Call this function again after 1 second
            self.master.after(1000, self.ping_loop)


if __name__ == "__main__":
    root = tk.Tk()
    app = PingCheckerGUI(root)
    root.mainloop()
