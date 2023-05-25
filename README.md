# Networking
Packet Loss Detection in Python

This code is a basic Packet Loss Detection Tool in Python which used Client-Server Model.

# UseCase
Packet loss occurs when one or more packets of data travelling across a computer network fail to reach their destination.
This is usually caused by equipment failure or some other issue but it can also happen because of someone with malicious intent listening to the packets or also know as Packet Sniffing Attack
Therefore this type of script can be used to monitor a secure connection between a Client & Server Machine.
Once the system detects Packet Loss it can then send a request to the server to discontinue its existing session and start a new session which can help prevent not only packet sniffing but also allocate resources with less traffic or in short traffic management. Thus increasing the whole user experience.

#*Current Limitations with Silver Lining*
Although this model is now best suited for client server mode only, it can also be used to monitor personal traffic to other sites.
Usually when a packet sniffing attack is done the hacker has to place himself between server and the client but the flow of packets is very unpredictable to where it can jump next. Therefore the hacker has a best option to place himself between the Internet Service Provider and the Client where the jumps of the packets can be predicted which in most cases has to be done physically/geographically.
Thus sending packets to any server can solve this issue because the flow of packets remain same till the ISP, which interrupted can trigger Packet Loss Detected Warning

YOU CAN DO THIS BY CHANGING THE “self.server_ip” VARIABLE TO ANY URL OR IP ADDRESS 
Eg:-  self.server_ip = "www.google.com"

# *Instructions To Install*

Prerequisites:
Python - Download the latest version of python from https://www.python.org/downloads/ 

Install the modules given below using the pip installer in terminal
*Copy-Paste 1 by 1*

“pip install subprocess”
“pip install socket”
“pip install tkinter”
“pip install matplotlib”
 
# Running the Server Side Script
While testing I’ve done it on the same system so I have used the address as 127.0.0.1 to listen for as it’s self calling.

If you are hosting the server script on different machine you need to provide address and port number accordingly 

How to run the script:
1. Using python terminal change the directory of the terminal to folder containing the server side script 
2. Run the script using - “python.exe server.py”
3. 3. The script will automatically start listening on the instructed port with the given address

# Running the Main Script

Make sure that the address given on the server side is same as the address in main.py 
Orelse change the variable “self.server_ip” to the desired IP address

How to run the script:
1. Once you have installed the tkinter module the script will run in application format i.e open in new window with GUI.
2. Using another terminal, if the server side script is running on same device u need to use new terminal without closing the server side, if the server is not      listening then this application wont get any response
3. You can open separate terminal and run it using - “python.exe main.py”
   If using VS Code you can also use *Code Runner Extension* to run the script.
4. Input the desired number of packets to be sent, by default it will be 5 but incase if you want to increase or decrease depending on your system
   & network throughput you can change it too.
5. Once the Start button is clicked the application will check for packet loss and also plot a graph of the ping output. The Status window will show if there       is any packet loss present or not.











