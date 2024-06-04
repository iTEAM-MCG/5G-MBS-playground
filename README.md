# Welcome to the 5G-MAG's 5G-MBS playground

Here you will find an easy way to try the current 5G-MBS MVP being developed by the [iTEAM Mobile Communications Group](https://github.com/iTEAM-MCG) as part of the [5G-MAG](https://github.com/5G-MAG), following the 3GPP Release 17 specifications.

This implementation is being developed on top of the [Open5GS](https://github.com/open5gs/open5gs) 5G Core. The repository containing the source code can be found [here](https://github.com/5G-MAG/open5gs/tree/upv-mbs).

This playground uses Docker Compose to deploy a 5G-MBS capable 5G Core using Docker images present in a container repository.

## 5G-MBS architecture using Open5GS

![5G-MBS architecture using Open5GS](images/5G-MBS_5G_Core.png)

> [!NOTE]
> Ports `TCP 27017`, `SCTP 38412` and `UDP 2152` are being exposed to the host running this Docker Compose deployment

These ports are being used for the following:
- `TCP 27017` to add subscribers to the MongoDB database
- `SCTP 38412` from the AMF for the NGAP `N2 interface`, used for the control plane connection with the external gNB
- `UDP 2152` from the MB-UPF for the GTPU `N3mb interface`, used for the data plane connection with the external gNB

TODO: Explain the services being exposed by the containers and how to change the `docker-host.external-ip: 172.33.33.33` in the mb-upf section of the docker-compose.yaml file.

> [!NOTE]
> Modify the `.env` file present on this repository to change the values being deployed on `docker-compose.yaml`

Add your host's IP address to the `DOCKER_HOST_IP` variable in the `.env` file for the MB-UPF to be able to reach Internet.

## Basic usage

To download the Docker images from the repository and start everything:

```bash
docker compose up -d
```

To stop everything:

```bash
docker compose down
```

## Find more information

- [docs/Overview](docs/Overview.md) to see the current status and features of the project.
- [docs/Detailed Instructions](docs/Detailed-Instructions.md) to see how to manage the containers.
- `configs` to check/modify the Network Function configuration files of the deployment.
- `examples` to see examples of the supported requests to the implemented APIs.
