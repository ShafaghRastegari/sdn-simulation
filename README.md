# sdn-simulation
A simple project with mininet and onos
## Usage
Suppose you already have installed docker, docker-compose and other common requirements, follow these steps.
1. Run docker-compose file to run mininet and onos
```sh
docker-compose docker-compose.yaml up
```
2. Go to mininet terminal
```sh
docker exec -it mininet /bin/bash
```
3. Run simple topology in mininet terminal with remote controller which here is onos
- note that onos-ip here is the ip that onos is running on it in your computer
```sh
mn --controller remote,ip=onos-ip --topo=tree,depth=2
```
4. Open a browser and go to `http://localhost:8181` to see your topology

## Result
If everything is correct you can see these results

![onos](/images/onos.png)

Use `pingall` command to check the connectivity

![pingall](/images/pingall.png)

### Custom topology

You can find some custom topology in topology folder