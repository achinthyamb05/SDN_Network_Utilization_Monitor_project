# NETWORK UTILIZATION MONITOR
## Student Information
- Achinthya MB
- PES1UG24CS019

## Problem Statement
To implement an SDN-based network monitoring solution using the Ryu controller and Mininet that demonstrates real-time traffic visibility through OpenFlow 1.3 flow rule design and packet-in event handling.

## Project Overview 
- Objective: The project implements an SDN-based network monitoring solution using the Ryu controller and Mininet to achieve real-time traffic visibility.

- Logic Implementation: The controller manages the network by handling Packet-In events for host connectivity and periodically "pulling" traffic data from switches using OpenFlow 1.3 PortStatsRequests.
  
- Topology Design: A custom topology was built with a Remote Controller, one Open vSwitch, and two hosts, ensuring a clear separation between the Control Plane and Data Plane.
  
- Functional Correctness: Successful communication was validated through pingall (reachability) and throughput was analyzed in real-time by calculating Kbps from byte-count differences.

- Performance Tools: Network behavior and the OpenFlow handshake were verified using Wireshark for packet inspection and iperf for stress-testing bandwidth.
- SDN Benefits: This project demonstrates the core SDN advantage of programmability, allowing a centralized software "brain" to monitor and report link utilization without manual switch configuration.


## Setup and Execution Steps
1. System Preparation
   
Ensure your Ubuntu VM is updated and has the necessary dependencies installed:

sudo apt update && sudo apt upgrade -y

sudo apt install git python3-pip mininet openvswitch-switch -y

2. Controller Setup
   
   Install the Ryu SDN Framework if not already present:

 - pip3 install ryu

3. Running the Project
   
Step A: Start the Ryu Controller

Launch the monitoring script in a dedicated terminal. This starts the "Brain" of the network and initiates the 5-second polling thread:

- ryu-manager monitor_controller.py

Step B: Start the Mininet Topology

Open a second terminal and run your custom topology script. This creates the virtual hosts, switch, and connects them to the remote controller:

- sudo python3 topology.py

Step C: Verify Functionality

Once the Mininet CLI (mininet>) appears, test connectivity and generate traffic to see the utilization reports:

Connectivity Test: 

- mininet> pingall

Traffic Generation: 

- mininet> iperf h1 h2

Making host 1 listen: 

- mininet> h1 iperf -s &

Making h2 send bulk of data every 10 seconds:

- mininet> h2 iperf -c 10.0.0.1 -t 10

4. Cleanup

If the network fails to start or says "Address already in use," clean the Mininet cache:

- sudo mn -c



  
