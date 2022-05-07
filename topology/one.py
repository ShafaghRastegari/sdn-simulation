from mininet.topo import Topo

class MyFirstTopo(Topo):
    "Simple topology example."
    def __init__(self, n=3):

        "Create custom topo."
        # Initialize topology

        Topo.__init__(self)

        # Add hosts and switches
        c1 = self.addSwitch('c1')
        hosts = []
        edges = []
        aggregations = []
        hosts_counter = 0
        edges_counter = 0
        aggregations_counter = 0
        for _ in range(n):
            aggregations.append(self.addSwitch('a{}'.format(aggregations_counter+1),dpid='00000000000000a{}'.format(aggregations_counter+1)))
            self.addLink(aggregations[aggregations_counter], c1)
            for _ in range(n):
                edges.append(self.addSwitch('e{}'.format(edges_counter+1),dpid='00000000000000e{}'.format(edges_counter+1)))
                self.addLink(edges[edges_counter], aggregations[aggregations_counter])
                for _ in range(n):
                    hosts.append(self.addHost('h{}'.format(hosts_counter+1)))
                    self.addLink(hosts[hosts_counter], edges[edges_counter])
                    hosts_counter+=1
                edges_counter+=1
            aggregations_counter+=1


topos = {'myfirsttopo': (lambda: MyFirstTopo())}