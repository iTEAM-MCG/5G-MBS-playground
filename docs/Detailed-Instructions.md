# Detailed Instructions

## Inspect all the traffic being sent in the network

You can use tcpdump/Wireshark to sniff all the messages being sent between the Network Functions by inspecting the `br-ogs` network bridge. This bridge is created by the Docker Compose network and is used to connect all the Network Functions.

```bash
$ tcpdump -i br-ogs
```

## Connect to the AF container to start sending requests to the Network Functions

The AF container is not Open5GS related, in fact, it is not even an AF, it is just a container called AF being used to send curl requests to the Open5GS APIs.

```bash
# Connect to the AF container
docker exec -it af bash
```

Use curl inside the container to send requests to the other Network Functions:

```bash
# Inside the AF container, example of the AF sending the MB-SMF the TMGI allocate request
curl --http2-prior-knowledge \
  --request POST \
  --header "Content-Type: application/json" \
  --data '{ "tmgiNumber": 1 }' \
  mb-smf.open5gs.org:80/nmbsmf-tmgi/v1/tmgi
```

## Configure the MB-UPF multicast

TODO: Explain all the smcroute mess
