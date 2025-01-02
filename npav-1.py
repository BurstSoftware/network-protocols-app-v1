import streamlit as st

def display_protocols(layer_name, protocols):
    """
    Display the details of protocols for a given layer.
    """
    st.header(layer_name)
    for protocol, (description, steps) in protocols.items():
        st.subheader(protocol)
        st.markdown(f"**Description:** {description}")
        st.markdown(f"**Steps/Examples:** {steps}")
        st.markdown("---")

def main():
    st.title("Networking Protocols Explorer")
    st.markdown("""
        This app categorizes and provides information about various networking protocols across the OSI model layers.
        Select a layer or category to explore the associated protocols, along with steps or code examples to utilize them.
    """)

    # Sidebar navigation
    layers = [
        "Physical Layer Protocols",
        "Data Link Layer Protocols",
        "Network Layer Protocols",
        "Transport Layer Protocols",
        "Session Layer Protocols",
        "Presentation Layer Protocols",
        "Application Layer Protocols",
        "Other Protocols",
    ]
    selected_layer = st.sidebar.selectbox("Select a Layer or Category", layers)

    # Display protocols based on selected layer
    if selected_layer == "Physical Layer Protocols":
        display_protocols("Physical Layer Protocols", {
            "Ethernet": ("Used in wired LANs for high-speed data transfer.", "Configure network interfaces using `ifconfig` or `ip` command on Linux."),
            "USB": ("Connects peripherals to a computer, supports data transfer.", "Use libraries like `pyserial` for USB communication in Python."),
            "Bluetooth": ("Short-range wireless communication, e.g., for headphones.", "Pair devices via system settings or use `pybluez` for custom applications."),
            "Wi-Fi (IEEE 802.11)": ("Wireless networking for internet access.", "Connect via OS network settings or use `wifi` Python module for scripting.")
        })

    elif selected_layer == "Data Link Layer Protocols":
        display_protocols("Data Link Layer Protocols", {
            "ARP (Address Resolution Protocol)": ("Resolves IP addresses to MAC addresses.", "Use `arp -a` to view ARP table, or `scapy` in Python for ARP packets."),
            "HDLC (High-level Data Link Control)": ("Encapsulates data for point-to-point links.", "Configure via router or network device interfaces."),
            "PPP (Point-to-Point Protocol)": ("Establishes direct connections between nodes.", "Set up PPP connections using `pppd` on Linux systems."),
            "STP (Spanning Tree Protocol)": ("Prevents loops in Ethernet networks.", "Enable and configure STP on managed network switches."),
            "VLAN (Virtual Local Area Network)": ("Creates logical LAN segments within a physical network.", "Configure VLAN tagging on switches or use `vconfig` on Linux.")
        })

    elif selected_layer == "Network Layer Protocols":
        display_protocols("Network Layer Protocols", {
            "IP (Internet Protocol - IPv4 and IPv6)": ("Routes packets between devices on different networks.", "Configure static IPs using `ifconfig` or `ip` command."),
            "ICMP (Internet Control Message Protocol)": ("Sends error and diagnostic messages (e.g., ping).", "Use `ping` command or `scapy` library in Python for ICMP packets."),
            "IGMP (Internet Group Management Protocol)": ("Manages multicast group memberships.", "Enable IGMP snooping on switches for multicast optimization."),
            "IPsec (Internet Protocol Security)": ("Provides secure communication over IP.", "Set up IPsec tunnels using `strongSwan` or `OpenSwan` tools."),
            "GRE (Generic Routing Encapsulation)": ("Encapsulates data for VPNs and tunneling.", "Configure GRE tunnels via router settings or Linux `ip tunnel` command.")
        })

    elif selected_layer == "Transport Layer Protocols":
        display_protocols("Transport Layer Protocols", {
            "TCP (Transmission Control Protocol)": ("Ensures reliable data transmission.", "Use Python `socket` library to create TCP connections."),
            "UDP (User Datagram Protocol)": ("Supports fast, connectionless communication.", "Use Python `socket` library for UDP datagrams."),
            "SCTP (Stream Control Transmission Protocol)": ("Combines features of TCP and UDP for real-time data.", "Install and use SCTP modules or libraries for your OS.")
        })

    elif selected_layer == "Session Layer Protocols":
        display_protocols("Session Layer Protocols", {
            "NetBIOS (Network Basic Input/Output System)": ("Supports file and printer sharing in Windows networks.", "Access via Windows command line using `net use` or network settings."),
            "RPC (Remote Procedure Call)": ("Allows a program to execute code on another machine.", "Use `xmlrpc` or `grpc` libraries in Python for RPC communication.")
        })

    elif selected_layer == "Presentation Layer Protocols":
        display_protocols("Presentation Layer Protocols", {
            "SSL/TLS (Secure Sockets Layer/Transport Layer Security)": ("Encrypts communication for security (e.g., HTTPS).", "Set up SSL certificates using `OpenSSL` or automate with `certbot`.")
        })

    elif selected_layer == "Application Layer Protocols":
        display_protocols("Application Layer Protocols", {
            "HTTP/HTTPS (Hypertext Transfer Protocol/Secure)": ("Enables web browsing and secure data transfer.", "Use `requests` library in Python for HTTP/HTTPS requests."),
            "FTP (File Transfer Protocol)": ("Transfers files between a client and server.", "Use `ftplib` in Python or GUI tools like FileZilla."),
            "SMTP (Simple Mail Transfer Protocol)": ("Sends emails between servers.", "Use Python `smtplib` to send emails programmatically."),
            "POP3 (Post Office Protocol version 3)": ("Retrieves emails from a server.", "Access emails using `poplib` in Python."),
            "IMAP (Internet Message Access Protocol)": ("Synchronizes emails across devices.", "Use Python `imaplib` for email synchronization."),
            "DNS (Domain Name System)": ("Translates domain names to IP addresses.", "Perform DNS queries using `socket` or `dnspython` library."),
            "DHCP (Dynamic Host Configuration Protocol)": ("Assigns IP addresses to devices dynamically.", "Set up DHCP servers with `dhcpd` or router settings."),
            "SNMP (Simple Network Management Protocol)": ("Manages devices on IP networks.", "Use `pysnmp` library to query SNMP-enabled devices."),
            "Telnet": ("Provides remote access to devices (insecure).", "Use `telnet` command or Python `telnetlib` for automation."),
            "SSH (Secure Shell)": ("Provides secure remote access to devices.", "Automate SSH tasks using `paramiko` or `ssh` command."),
            "NTP (Network Time Protocol)": ("Synchronizes clocks on networked devices.", "Use `ntpdate` command or configure NTP clients."),
            "LDAP (Lightweight Directory Access Protocol)": ("Accesses and maintains distributed directories.", "Query LDAP directories using `ldap3` Python library."),
            "SFTP (Secure File Transfer Protocol)": ("Transfers files securely over SSH.", "Use Python `paramiko` or tools like WinSCP."),
            "TFTP (Trivial File Transfer Protocol)": ("Transfers files with minimal functionality.", "Set up TFTP servers using `tftpd` on Linux."),
            "BGP (Border Gateway Protocol)": ("Routes data between autonomous systems on the internet.", "Configure BGP on routers using tools like Quagga or FRRouting."),
            "OSPF (Open Shortest Path First)": ("Finds the shortest path for routing in IP networks.", "Enable OSPF on network routers via their configuration settings."),
            "RIP (Routing Information Protocol)": ("Routes data using distance-vector algorithm.", "Configure RIP on routers via CLI or web interfaces."),
            "SIP (Session Initiation Protocol)": ("Manages multimedia communication sessions.", "Set up SIP clients using software like Zoiper or libraries."),
            "RTP (Real-time Transport Protocol)": ("Delivers audio and video over IP networks.", "Integrate RTP streams using multimedia frameworks like GStreamer.")
        })

    elif selected_layer == "Other Protocols":
        display_protocols("Other Protocols", {
            "VPN (Virtual Private Network) protocols": ("Enable secure access to private networks over the internet.", "Set up VPNs using OpenVPN or built-in OS tools."),
            "PPTP (Point-to-Point Tunneling Protocol)": ("Implements VPNs, now considered less secure.", "Configure PPTP in Windows network settings or routers."),
            "L2TP (Layer 2 Tunneling Protocol)": ("Combines with IPsec for secure VPNs.", "Set up L2TP with IPsec using `strongSwan` or similar tools."),
            "WireGuard": ("Modern VPN protocol focused on simplicity and speed.", "Set up WireGuard using the `wg` command-line tool or configuration files."),
            "MPLS (Multiprotocol Label Switching)": ("Optimizes routing by using labels instead of IP addresses.", "Configure MPLS on enterprise routers to enhance data transport."),
            "Zerotier": ("Creates virtual networks for devices across the internet.", "Install ZeroTier client and join a virtual network via its management interface.")
        })

if __name__ == "__main__":
    main()
