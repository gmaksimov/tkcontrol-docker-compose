Tkcontrol Docker Compose
=========

Quick start with tkcontrol using docker-compose

Getting started
---------------

Download [Docker Desktop](https://www.docker.com/products/docker-desktop) for Mac or Windows. [Docker Compose](https://docs.docker.com/compose) will be automatically installed. On Linux, make sure you have the latest version of [Compose](https://docs.docker.com/compose/install/). 

## Install

Download folder with latest docker images.

Load images on the host with docker:
```
docker load < imagename.tar.gz
```

## Run

```
git clone https://github.com/gmaksimov/tkcontrol-docker-compose.git
cd tkcontrol-docker-compose

docker-compose up -d

```

After that you can access tkcontrol using http://localhost

## Connect clients

After connection clients you would see them on the web interface

### Using docker (only for testing)

```
docker-compose -f docker-compose.yml -f docker-compose.clients.yml up
```

### Manually install salt-minion on client machine

Manually install [salt-minion](https://docs.saltstack.com/en/master/topics/installation/index.html) on client machine.

Add address of saltstack machine to /etc/salt/minion.conf

```
master: saltstack
```
*Note: Ensure that this address is resolvable or use ip address*

## Upgrade

Download folder with latest docker images.

Load images on the host with docker:
```
docker load < imagename.tar.gz
```

Update config files:
```
git pull
```

Recreate containers:
```
docker-compose up --force-recreate -d
```
