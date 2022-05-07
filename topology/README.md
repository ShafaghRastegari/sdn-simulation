Here we create and run custom topology

In this project we create a simple tree topology. End-hosts connect to top-of-rack switches, called edge switches and form the leaves of the tree; one or more core switches form the root of the tree; and one or more aggregation switches form the intermediate nodes of the tree.

In our project there is only one core switch connected to 𝑛 aggregation switches; each aggregation switch is connected to 𝑛 edge switches; each edges switches is connected to 𝑛 hosts.

You can see simple tree topology where n=2:

![simple tree topology](/images/simple-tree-topology.png)

## Usage
After you meet the reqirement and take steps in the root folder rather than step 3 to run a simple topology use this command
- note that onos-ip here is the ip that onos is running on it in your computer
```sh
mn --custom /topo/one.py --topo myfirsttopo --controller remote,ip=onos-ip,switch=ovs,protocols=OpenFlow13
```

## Example
> Result for n=2

![two topology](/images/two.png)

Use `pingall` command to check the connectivity

![pingall two](/images/pingall-two.png)

> Result for n=3

![three topology](/images/three.png)

Use `pingall` command to check the connectivity

![pingall three](/images/pingall-three.png)