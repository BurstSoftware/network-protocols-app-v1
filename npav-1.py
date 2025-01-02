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
                        "https://networkencyclopedia.com/ethernet/"),
            "USB": ("Connects peripherals to a computer, supports data transfer.", 
                   "Use libraries like `pyserial` for USB communication in Python.",
                   "https://www.usb.org/developers"),
            "Bluetooth": ("Short-range wireless communication, e.g., for headphones.", 
                         "Pair devices via system settings or use `pybluez` for custom applications.",
                         "https://www.bluetooth.com/learn-about-bluetooth/"),
            "Wi-Fi (IEEE 802.11)": ("Wireless networking for internet access.", 
                                   "Connect via OS network settings or use `wifi` Python module for scripting.",
                                   "https://www.wi-fi.org/knowledge-center")
        })

    elif selected_layer == "Data Link Layer Protocols":
        display_protocols("Data Link Layer Protocols", {
            "ARP (Address Resolution Protocol)": ("Resolves IP addresses to MAC addresses.", 
                                                "Use `arp -a` to view ARP table, or `scapy` in Python for ARP packets.",
                                                "https://wiki.wireshark.org/ARP"),
            "HDLC (High-level Data Link Control)": ("Encapsulates data for point-to-point links.", 
                                                   "Configure via router or network device interfaces.",
                                                   "https://www.cisco.com/c/en/us/support/docs/wan/high-level-data-link-control/52537-hdlc-lap-concepts.html"),
            "PPP (Point-to-Point Protocol)": ("Establishes direct connections between nodes.", 
                                            "Set up PPP connections using `pppd` on Linux systems.",
                                            "https://linux.die.net/man/8/pppd"),
            "STP (Spanning Tree Protocol)": ("Prevents loops in Ethernet networks.", 
                                           "Enable and configure STP on managed network switches.",
                                           "https://www.cisco.com/c/en/us/support/docs/lan-switching/spanning-tree-protocol/5234-5.html"),
            "VLAN (Virtual Local Area Network)": ("Creates logical LAN segments within a physical network.", 
                                                "Configure VLAN tagging on switches or use `vconfig` on Linux.",
                                                "https://www.cloudflare.com/learning/network-layer/what-is-a-vlan/")
        })

    elif selected_layer == "Network Layer Protocols":
        display_protocols("Network Layer Protocols", {
            "IP (Internet Protocol - IPv4 and IPv6)": ("Routes packets between devices on different networks.", 
                                                      "Configure static IPs using `ifconfig` or `ip` command.",
                                                      "https://www.cloudflare.com/learning/network-layer/internet-protocol/"),
            "ICMP (Internet Control Message Protocol)": ("Sends error and diagnostic messages (e.g., ping).", 
                                                       "Use `ping` command or `scapy` library in Python for ICMP packets.",
                                                       "https://networklessons.com/cisco/ccna-routing-switching-icnd1-100-105/icmp-internet-control-message-protocol"),
            "IGMP (Internet Group Management Protocol)": ("Manages multicast group memberships.", 
                                                        "Enable IGMP snooping on switches for multicast optimization.",
                                                        "https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/ipmulti_igmp/configuration/xe-16/imc-igmp-xe-16-book.html"),
            "IPsec (Internet Protocol Security)": ("Provides secure communication over IP.", 
                                                 "Set up IPsec tunnels using `strongSwan` or `OpenSwan` tools.",
                                                 "https://www.cloudflare.com/learning/network-layer/what-is-ipsec/"),
            "GRE (Generic Routing Encapsulation)": ("Encapsulates data for VPNs and tunneling.", 
                                                   "Configure GRE tunnels via router settings or Linux `ip tunnel` command.",
                                                   "https://www.cisco.com/c/en/us/support/docs/ip/generic-routing-encapsulation-gre/47494-configure-gre-tunnel.html")
        })

    elif selected_layer == "Transport Layer Protocols":
        display_protocols("Transport Layer Protocols", {
            "TCP (Transmission Control Protocol)": ("Ensures reliable data transmission.", 
                                                  "Use Python `socket` library to create TCP connections.",
                                                  "https://www.cloudflare.com/learning/ddos/glossary/tcp-ip/"),
            "UDP (User Datagram Protocol)": ("Supports fast, connectionless communication.", 
                                           "Use Python `socket` library for UDP datagrams.",
                                           "https://www.cloudflare.com/learning/ddos/glossary/user-datagram-protocol-udp/"),
            "SCTP (Stream Control Transmission Protocol)": ("Combines features of TCP and UDP for real-time data.", 
                                                          "Install and use SCTP modules or libraries for your OS.",
                                                          "https://www.techtarget.com/searchnetworking/definition/Stream-Control-Transmission-Protocol-SCTP")
        })

    elif selected_layer == "Session Layer Protocols":
        display_protocols("Session Layer Protocols", {
            "NetBIOS (Network Basic Input/Output System)": ("Supports file and printer sharing in Windows networks.", 
                                                          "Access via Windows command line using `net use` or network settings.",
                                                          "https://learn.microsoft.com/en-us/windows-server/storage/file-server/networking-basics"),
            "RPC (Remote Procedure Call)": ("Allows a program to execute code on another machine.", 
                                          "Use `xmlrpc` or `grpc` libraries in Python for RPC communication.",
                                          "https://grpc.io/docs/what-is-grpc/introduction/")
        })

    elif selected_layer == "Presentation Layer Protocols":
        display_protocols("Presentation Layer Protocols", {
            "SSL/TLS (Secure Sockets Layer/Transport Layer Security)": ("Encrypts communication for security (e.g., HTTPS).", 
                                                                      "Set up SSL certificates using `OpenSSL` or automate with `certbot`.",
                                                                      "https://www.cloudflare.com/learning/ssl/what-is-ssl/")
        })

    elif selected_layer == "Application Layer Protocols":
        display_protocols("Application Layer Protocols", {
            "HTTP/HTTPS": ("Enables web browsing and secure data transfer.", 
                          "Use `requests` library in Python for HTTP/HTTPS requests.",
                          "https://developer.mozilla.org/en-US/docs/Web/HTTP"),
            "FTP": ("Transfers files between a client and server.", 
                   "Use `ftplib` in Python or GUI tools like FileZilla.",
                   "https://docs.python.org/3/library/ftplib.html"),
            "SMTP": ("Sends emails between servers.", 
                    "Use Python `smtplib` to send emails programmatically.",
                    "https://docs.python.org/3/library/smtplib.html"),
            "POP3": ("Retrieves emails from a server.", 
                    "Access emails using `poplib` in Python.",
                    "https://docs.python.org/3/library/poplib.html"),
            "IMAP": ("Synchronizes emails across devices.", 
                    "Use Python `imaplib` for email synchronization.",
                    "https://docs.python.org/3/library/imaplib.html"),
            "DNS": ("Translates domain names to IP addresses.", 
                   "Perform DNS queries using `socket` or `dnspython` library.",
                   "https://www.cloudflare.com/learning/dns/what-is-dns/"),
            "DHCP": ("Assigns IP addresses to devices dynamically.", 
                    "Set up DHCP servers with `dhcpd` or router settings.",
                    "https://www.isc.org/dhcp/"),
            "SNMP": ("Manages devices on IP networks.", 
                    "Use `pysnmp` library to query SNMP-enabled devices.",
                    "https://pysnmp.readthedocs.io/"),
            "SSH": ("Provides secure remote access to devices.", 
                   "Automate SSH tasks using `paramiko` or `ssh` command.",
                   "https://www.ssh.com/academy/ssh/protocol"),
            "NTP": ("Synchronizes clocks on networked devices.", 
                   "Use `ntpdate` command or configure NTP clients.",
                   "https://www.ntppool.org/en/"),
            "LDAP": ("Accesses and maintains distributed directories.", 
                    "Query LDAP directories using `ldap3` Python library.",
                    "https://ldap3.readthedocs.io/"),
            "SFTP": ("Transfers files securely over SSH.", 
                    "Use Python `paramiko` or tools like WinSCP.",
                    "https://docs.paramiko.org/en/stable/api/sftp.html"),
            "BGP": ("Routes data between autonomous systems on the internet.", 
                   "Configure BGP on routers using tools like Quagga or FRRouting.",
                   "https://www.cloudflare.com/learning/security/glossary/what-is-bgp/"),
            "OSPF": ("Finds the shortest path for routing in IP networks.", 
                    "Enable OSPF on network routers via their configuration settings.",
                    "https://www.cisco.com/c/en/us/support/docs/ip/open-shortest-path-first-ospf/7039-1.html"),
            "RIP": ("Routes data using distance-vector algorithm.", 
                   "Configure RIP on routers via CLI or web interfaces.",
                   "https://www.cisco.com/c/en/us/support/docs/ip/rip/13788-3.html"),
            "SIP": ("Manages multimedia communication sessions.", 
                   "Set up SIP clients using software like Zoiper or libraries.",
                   "https://www.3cx.com/voip/sip/"),
            "RTP": ("Delivers audio and video over IP networks.", 
                   "Integrate RTP streams using multimedia frameworks like GStreamer.",
                   "https://www.gstreamer.freedesktop.org/documentation/rtp/")
        })

    elif selected_layer == "Other Protocols":
        display_protocols("Other Protocols", {
            "VPN (Virtual Private Network) protocols": ("Enable secure access to private networks over the internet.", 
                                                      "Set up VPNs using OpenVPN or built-in OS tools.",
                                                      "https://openvpn.net/community-resources/"),
            "PPTP": ("Implements VPNs, now considered less secure.", 
                    "Configure PPTP in Windows network settings or routers.",
                    "https://learn.microsoft.com/en-us/windows/win32/rras/pptp-protocol"),
            "L2TP": ("Combines with IPsec for secure VPNs.", 
                    "Set up L2TP with IPsec using `strongSwan` or similar tools.",
                    "https://strongswan.org/documentation.html"),
            "WireGuard": ("Modern VPN protocol focused on simplicity and speed.", 
                         "Set up WireGuard using the `wg` command-line tool or configuration files.",
                         "https://www.wireguard.com/quickstart/"),
            "MPLS": ("Optimizes routing by using labels instead of IP addresses.", 
                    "Configure MPLS on enterprise routers to enhance data transport.",
                    "https://www.cloudflare.com/learning/network-layer/what-is-mpls/"),
            "Zerotier": ("Creates virtual networks for devices across the internet.", 
                        "Install ZeroTier client and join a virtual network via its management interface.",
                        "https://docs.zerotier.com/getting-started/")
        })

if __name__ == "__main__":
    main()
