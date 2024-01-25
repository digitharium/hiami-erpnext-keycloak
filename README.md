# Template Repository

[![License: BSD3](https://img.shields.io/badge/License-BSD3-blue.svg)](https://opensource.org/license/bsd-3-clause/)

[![Trigger Jenkins Pipe](https://github.com/digitharium/hiami-erpnext-keycloak/actions/workflows/main.yml/badge.svg)](https://github.com/digitharium/hiami-erpnext-keycloak/actions/workflows/main.yml)

## Introduction

This repository is a template for all the repositories that will be used at the hackathon 2024 part of the symposium.

## Contributors

* Pieter-Bas Ijdens [pbijdens](github.com/pbijdens)
* Romain Kieffer [romainkieffer](github.com/romainkieffer)
* Grégory Wawszyniak Dumont [gregWDumont](https://github.com/gregWDumont)

## Instructions

This section will highlight the instructions needed for this repository

### Docker install

Download and install the Docker client from the official [Docker website](https://www.docker.com/).

### Start Keycloak Container

```bash
docker run -p --name keycloack_container 8080:8080 -e KEYCLOAK_ADMIN=admin -e KEYCLOAK_ADMIN_PASSWORD=admin quay.io/keycloak/keycloak:23.0.4 start-dev
```

### Clone the frappe_docker Repository and Set Up ERPNext

```bash
git clone https://github.com/frappe/frappe_docker
cd frappe_docker
docker-compose -f pwd.yml up -d
```

### Set Up ERPNext URI

```bash
echo "127.0.0.1 erpnext.local" | sudo tee -a /etc/hosts
```

### Configure Keycloak

Enter the Keycloak container shell:

```bash
docker exec -it keycloak_container /bin/bash
```

Inside the container, configure credentials and create a new realm:

```bash
./kcadm.sh config credentials --server http://localhost:8080/auth --realm master --user admin --password admin
./kcadm.sh create realms -s realm=newrealm -s enabled=true
```

Create a client for ERPNext:

```bash
./kcadm.sh create clients \
-r newrealm \
-s clientId=erpnext \
-s enabled=true \
-s publicClient=false \
-s 'redirectUris=["http://erpnext.local/api/method/frappe.integrations.oauth2.authorize"]' \
-s protocol=openid-connect \
-s directAccessGrantsEnabled=true \
-s serviceAccountsEnabled=true \
-s authorizationServicesEnabled=true 
```
