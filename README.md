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

### Start Keycloak Container

```bash
docker run -d --name my_keycloak_container -p 8080:8080
-e KEYCLOAK_ADMIN=admin -e KEYCLOAK_ADMIN_PASSWORD=admin
quay.io/keycloak/keycloak:23.0.4 start-dev
```

### Clone the frappe_docker repository and set up ERPNext

```bash
git clone https://github.com/frappe/frappe_docker
cd frappe_docker
docker-compose -f pwd.yml up -d
```
