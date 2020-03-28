# Ansible role: MariaDB

[![Version](https://img.shields.io/badge/latest_version-2.0.0-green.svg)](https://git.yaegashi.fr/nishiki/ansible-role-mariadb/releases)
[![Build Status](https://travis-ci.org/nishiki/ansible-role-mariadb.svg?branch=master)](https://travis-ci.org/nishiki/ansible-role-mariadb)
[![License](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](https://git.yaegashi.fr/nishiki/ansible-role-mariadb/src/branch/master/LICENSE)

Install and configure MariaDB

## Requirements

* Ansible >= 2.8
* Debian Stretch and Buster

## Role variables

| Name                            | Type  | Required |Default | Comment                                |
|---------------------------------|-------|----------|--------|----------------------------------------|
| mariadb_use_official_repository | bool  | no       | true   | use the official repository            |
| mariadb_branch                  | str   | no       | 10.3   | the branch version to install          |
| mariadb_user                    | str   | no       | root   | login to connect on mariadb            |
| mariadb_password                | str   | no       | secret | password to connect on mariadb         |
| mariadb_master                  | bool  | no       | false  | the server is master                   |
| mariadb_autorestart             | bool  | no       | false  | restart mariadb when the config change |
| mariadb_users                   | array | no       |        | the users to manage                    |
| mariadb_databases               | array | no       |        | the databases to manage                |
| mariadb_config                  | hash  | no       |        | extra options for configuration        |

### mariadb_users

| Name       | Type  | Required |Default  | Comment                                                   |
|------------|-------|----------|---------|-----------------------------------------------------------|
| name       | str   | yes      |         | the username                                              |
| host       | str   | yes      |         | the mysql user host                                       |
| password   | str   | yes      |         | the user password                                         |
| privileges | array | no       |         | the privileges with this form `database.*:SELECT,UPDATE`) |
| state      | str   | no       | present | if state is `absent` the user is deleted                  |

Example:

```
- name: johndoe
  host: '%'
  password: supersecret
  privileges:
    - 'database.*:SELECT,UPDATE'
  state: present
```

### mariadb_databases

| Name       | Type  | Required |Default  | Comment                                                   |
|------------|-------|----------|---------|-----------------------------------------------------------|
| name       | str   | yes      |         | the dabase name                                           |
| state      | str   | no       | present | if state is `absent` the database is deleted              |

Example:

```
- name: superprogram
  state: present
```

### mariadb_config

Example:

```
  mysqld:
    server-id: 1
    bind-address: 0.0.0.0
```

## How to use

```
- hosts: server
  vars:
    mariadb_password: supersecret
    mariadb_users:
      - name: johndoe
        host: '%'
        password: usersecret
        privileges:
          - 'myappli.*:ALL'
    mariadb_databases:
      - myappli
    mariadb_config:  
      server-id: 1
      bind-address: 0.0.0.0
  roles:
    - mariadb
```

## Development

### Test with molecule and docker

* install [docker](https://docs.docker.com/engine/installation/)
* install `python3` and `python3-pip`
* install molecule and dependencies `pip3 install molecule 'molecule[docker]' docker ansible-lint testinfra yamllint`
* run `molecule test`

## License

```
Copyright (c) 2019 Adrien Waksberg

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```
