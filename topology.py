from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import RemoteController, OVSSwitch
from mininet.cli import CLI

class CustomTopo(Topo):
    def build(self):
        s1 = self.addSwitch('s1')
        h1 = self.addHost('h1', ip='10.0.0.1')
        h2 = self.addHost('h2', ip='10.0.0.2')
        self.addLink(h1, s1)
        self.addLink(h2, s1)

if __name__ == '__main__':
    topo = CustomTopo()
    net = Mininet(topo=topo, controller=RemoteController, switch=OVSSwitch)
    net.start()
    CLI(net)
    net.stop()
