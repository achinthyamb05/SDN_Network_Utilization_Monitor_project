# NETWORK UTILIZATION MONITOR
## Student Information
- Achinthya MB
- PES1UG24CS019

## Project Overview 
- Objective: The project implements an SDN-based network monitoring solution using the Ryu controller and Mininet to achieve real-time traffic visibility.

- Logic Implementation: The controller manages the network by handling Packet-In events for host connectivity and periodically "pulling" traffic data from switches using OpenFlow 1.3 PortStatsRequests.
  
- Topology Design: A custom topology was built with a Remote Controller, one Open vSwitch, and two hosts, ensuring a clear separation between the Control Plane and Data Plane.
  
- Functional Correctness: Successful communication was validated through pingall (reachability) and throughput was analyzed in real-time by calculating Kbps from byte-count differences.

- Performance Tools: Network behavior and the OpenFlow handshake were verified using Wireshark for packet inspection and iperf for stress-testing bandwidth.

- SDN Benefits: This project demonstrates the core SDN advantage of programmability, allowing a centralized software "brain" to monitor and report link utilization without manual switch configuration.

  
