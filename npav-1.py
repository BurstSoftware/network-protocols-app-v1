import streamlit as st

def display_protocols(layer_name, protocols):
    """
    Display the details of protocols for a given layer.
    """
    st.header(layer_name)
    for protocol, (description, steps, resource) in protocols.items():
        st.subheader(protocol)
        st.markdown(f"**Description:** {description}")
        st.markdown(f"**Steps/Examples:** {steps}")
        st.markdown(f"**Learn More:** [Documentation & Resources]({resource})")
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
            "Ethernet": ("Used in wired LANs for high-speed data transfer.", 
                        "Configure network interfaces using `ifconfig` or `ip` command on Linux.",
                        "https://standards.ieee.org/ieee/802.3/7028/"),
            "USB": ("Connects peripherals to a computer, supports data transfer.", 
                   "Use libraries like `pyserial` for USB communication in Python.",
                   "https://www.usb.org/documents"),
            "Bluetooth": ("Short-range wireless communication, e.g., for headphones.", 
                         "Pair devices via system settings or use `pybluez` for custom applications.",
                         "https://www.bluetooth.com/specifications/specs/"),
            "Wi-Fi (IEEE 802.11)": ("Wireless networking for internet access.", 
                                   "Connect via OS network settings or use `wifi` Python module for scripting.",
                                   "https://www.wi-fi.org/discover-wi-fi/specifications")
        })

    elif selected_layer == "Data Link Layer Protocols":
        display_protocols("Data Link Layer Protocols", {
            "ARP (Address Resolution Protocol)": ("Resolves IP addresses to MAC addresses.", 
                                                "Use `arp -a` to view ARP table, or `scapy` in Python for ARP packets.",
                                                "https://datatracker.ietf.org/doc/html/rfc826"),
            "HDLC (High-level Data Link Control)": ("Encapsulates data for point-to-point links.", 
                                                   "Configure via router or network device interfaces.",
                                                   "https://standards.iso.org/ittf/PubliclyAvailableStandards/"),
            "PPP (Point-to-Point Protocol)": ("Establishes direct connections between nodes.", 
                                            "Set up PPP connections using `pppd` on Linux systems.",
                                            "https://datatracker.ietf.org/doc/html/rfc1661"),
            "STP (Spanning Tree Protocol)": ("Prevents loops in Ethernet networks.", 
                                           "Enable and configure STP on managed network switches.",
                                           "https://standards.ieee.org/ieee/802.1D/6866/"),
            "VLAN (Virtual Local Area Network)": ("Creates logical LAN segments within a physical network.", 
                                                "Configure VLAN tagging on switches or use `vconfig` on Linux.",
                                                "https://standards.ieee.org/ieee/802.1Q/7098/")
        })

    elif selected_layer == "Network Layer Protocols":
        display_protocols("Network Layer Protocols", {
            "IP (Internet Protocol - IPv4 and IPv6)": ("Routes packets between devices on different networks.", 
                                                      "Configure static IPs using `ifconfig` or `ip` command.",
                                                      "https://datatracker.ietf.org/doc/html/rfc791"),
            "ICMP (Internet Control Message Protocol)": ("Sends error and diagnostic messages (e.g., ping).", 
                                                       "Use `ping` command or `scapy` library in Python for ICMP packets.",
                                                       "https://datatracker.ietf.org/doc/html/rfc792"),
            "IGMP (Internet Group Management Protocol)": ("Manages multicast group memberships.", 
                                                        "Enable IGMP snooping on switches for multicast optimization.",
                                                        "https://datatracker.ietf.org/doc/html/rfc2236"),
            "IPsec (Internet Protocol Security)": ("Provides secure communication over IP.", 
                                                 "Set up IPsec tunnels using `strongSwan` or `OpenSwan` tools.",
                                                 "https://datatracker.ietf.org/doc/html/rfc4301"),
            "GRE (Generic Routing Encapsulation)": ("Encapsulates data for VPNs and tunneling.", 
                                                   "Configure GRE tunnels via router settings or Linux `ip tunnel` command.",
                                                   "https://datatracker.ietf.org/doc/html/rfc2784")
        })

    elif selected_layer == "Transport Layer Protocols":
        display_protocols("Transport Layer Protocols", {
            "TCP (Transmission Control Protocol)": ("Ensures reliable data transmission.", 
                                                  "Use Python `socket` library to create TCP connections.",
                                                  "https://datatracker.ietf.org/doc/html/rfc793"),
            "UDP (User Datagram Protocol)": ("Supports fast, connectionless communication.", 
                                           "Use Python `socket` library for UDP datagrams.",
                                           "https://datatracker.ietf.org/doc/html/rfc768"),
            "SCTP (Stream Control Transmission Protocol)": ("Combines features of TCP and UDP for real-time data.", 
                                                          "Install and use SCTP modules or libraries for your OS.",
                                                          "https://datatracker.ietf.org/doc/html/rfc4960")
        })

    elif selected_layer == "Session Layer Protocols":
        display_protocols("Session Layer Protocols", {
            "NetBIOS (Network Basic Input/Output System)": ("Supports file and printer sharing in Windows networks.", 
                                                          "Access via Windows command line using `net use` or network settings.",
                                                          "https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2003/cc738412(v=ws.10)"),
            "RPC (Remote Procedure Call)": ("Allows a program to execute code on another machine.", 
                                          "Use `xmlrpc` or `grpc` libraries in Python for RPC communication.",
                                          "https://grpc.io/docs/")
        })

    elif selected_layer == "Presentation Layer Protocols":
        display_protocols("Presentation Layer Protocols", {
            "SSL/TLS (Secure Sockets Layer/Transport Layer Security)": ("Encrypts communication for security (e.g., HTTPS).", 
                                                                      "Set up SSL certificates using `OpenSSL` or automate with `certbot`.",
                                                                      "https://datatracker.ietf.org/doc/html/rfc8446")
        })

    elif selected_layer == "Application Layer Protocols":
        display_protocols("Application Layer Protocols", {
            "HTTP/HTTPS": ("Enables web browsing and secure data transfer.", 
                          "Use `requests` library in Python for HTTP/HTTPS requests.",
                          "https://datatracker.ietf.org/doc/html/rfc2616"),
            "FTP": ("Transfers files between a client and server.", 
                   "Use `ftplib` in Python or GUI tools like FileZilla.",
                   "https://datatracker.ietf.org/doc/html/rfc959"),
            "SMTP": ("Sends emails between servers.", 
                    "Use Python `smtplib` to send emails programmatically.",
                    "https://datatracker.ietf.org/doc/html/rfc5321"),
            "POP3": ("Retrieves emails from a server.", 
                    "Access emails using `poplib` in Python.",
                    "https://datatracker.ietf.org/doc/html/rfc1939"),
            "IMAP": ("Synchronizes emails across devices.", 
                    "Use Python `imaplib` for email synchronization.",
                    "https://datatracker.ietf.org/doc/html/rfc3501"),
            "DNS": ("Translates domain names to IP addresses.", 
                   "Perform DNS queries using `socket` or `dnspython` library.",
                   "https://datatracker.ietf.org/doc/html/rfc1035"),
            "DHCP": ("Assigns IP addresses to devices dynamically.", 
                    "Set up DHCP servers with `dhcpd` or router settings.",
                    "https://datatracker.ietf.org/doc/html/rfc2131"),
            "SNMP": ("Manages devices on IP networks.", 
                    "Use `pysnmp` library to query SNMP-enabled devices.",
                    "https://datatracker.ietf.org/doc/html/rfc1157"),
            "SSH": ("Provides secure remote access to devices.", 
                   "Automate SSH tasks using `paramiko` or `ssh` command.",
                   "https://datatracker.ietf.org/doc/html/rfc4251"),
            "NTP": ("Synchronizes clocks on networked devices.", 
                   "Use `ntpdate` command or configure NTP clients.",
                   "https://datatracker.ietf.org/doc/html/rfc5905"),
            "LDAP": ("Accesses and maintains distributed directories.", 
                    "Query LDAP directories using `ldap3` Python library.",
                    "https://datatracker.ietf.org/doc/html/rfc4511"),
            "SFTP": ("Transfers files securely over SSH.", 
                    "Use Python `paramiko` or tools like WinSCP.",
                    "https://datatracker.ietf.org/doc/html/rfc913"),
            "BGP": ("Routes data between autonomous systems on the internet.", 
                   "Configure BGP on routers using tools like Quagga or FRRouting.",
                   "https://datatracker.ietf.org/doc/html/rfc4271"),
            "OSPF": ("Finds the shortest path for routing in IP networks.", 
                    "Enable OSPF on network routers via their configuration settings.",
                    "https://datatracker.ietf.org/doc/html/rfc2328"),
            "RIP": ("Routes data using distance-vector algorithm.", 
                   "Configure RIP on routers via CLI or web interfaces.",
                   "https://datatracker.ietf.org/doc/html/rfc2453"),
            "SIP": ("Manages multimedia communication sessions.", 
                   "Set up SIP clients using software like Zoiper or libraries.",
                   "https://datatracker.ietf.org/doc/html/rfc3261"),
            "RTP": ("Delivers audio and video over IP networks.", 
                   "Integrate RTP streams using multimedia frameworks like GStreamer.",
                   "https://datatracker.ietf.org/doc/html/rfc3550")
        })

    elif selected_layer == "Other Protocols":
        display_protocols("Other Protocols", {
            "VPN (Virtual Private Network) protocols": ("Enable secure access to private networks over the internet.", 
                                                      "Set up VPNs using OpenVPN or built-in OS tools.",
                                                      "https://openvpn.net/community-resources/"),
            "PPTP": ("Implements VPNs, now considered less secure.", 
                    "Configure PPTP in Windows network settings or routers.",
                    "https://datatracker.ietf.org/doc/html/rfc2637"),
            "L2TP": ("Combines with IPsec for secure VPNs.", 
                    "Set up L2TP with IPsec using `strongSwan` or similar tools.",
                    "https://datatracker.ietf.org/doc/html/rfc2661"),
            "WireGuard": ("Modern VPN protocol focused on simplicity and speed.", 
                         "Set up WireGuard using the `wg` command-line tool or configuration files.",
                         "https://www.wireguard.com/papers/"),
            "MPLS": ("Optimizes routing by using labels instead of IP addresses.", 
                    "Configure MPLS on enterprise routers to enhance data transport.",
                    "https://datatracker.ietf.org/doc/html/rfc3031"),
            "Zerotier": ("Creates virtual networks for devices across the internet.", 
                        "Install ZeroTier client and join a virtual network via its management interface.",
                        "https://docs.zerotier.com/")
        })

if __name__ == "__main__":
    main()
