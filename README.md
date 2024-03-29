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
docker exec -it keycloak_container /opt/keycloak/bin
```

Inside the container, configure credentials and create a new realm:

```bash
./kcadm.sh config credentials --server http://localhost:8080/auth --realm master --user admin --password admin
./kcadm.sh create realms -s realm=newrealm -s enabled=true
```

Create a client for ERPNext:

```bash
./kcadm.sh create clients -r Humanitarians -s clientId=erpnext -s enabled=true -s publicClient=false -s 'redirectUris=["http://localhost:8081/*"]' -s protocol=openid-connect -s directAccessGrantsEnabled=true -s serviceAccountsEnabled=true -s authorizationServicesEnabled=true -s secret=d0b8122f-8dfb-46b7-b68a-f5cc4e25d000
```

### Set Up ERPNext Credentials

After setting up ERPNext using the previous steps, you can configure the initial credentials:

1. Open a web browser and navigate to [http://localhost:8081/](http://localhost:8081/).

2. You will be directed to the ERPNext login page.

3. Use the following credentials to log in:

* Username: Administrator
* Password: admin

4. Once logged in, you can change the password for the "Administrator" account and configure additional users and permissions as needed.

### Generate API Secret for ERPNext API Requests and Social Logins

docker exec -it frappe_docker-backend-1 bench execute frappe.core.doctype.user.user.generate_keys --args ['user_name']