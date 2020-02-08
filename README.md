# Ansible role: MariaDB

[![Version](https://img.shields.io/badge/latest_version-2.0.0-green.svg)](https://git.yaegashi.fr/nishiki/ansible-role-mariadb/releases)
[![Build Status](https://travis-ci.org/nishiki/ansible-role-mariadb.svg?branch=master)](https://travis-ci.org/nishiki/ansible-role-mariadb)
[![License](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](https://git.yaegashi.fr/nishiki/ansible-role-mariadb/src/branch/master/LICENSE)

Install and configure MariaDB

## Requirements

* Ansible >= 2.8
* Debian Stretch and Buster

## Role variables

* `mariadb_use_official_repository` - use the official repository (default: `yes`)
* `mariadb_branch` - the branch version to install (default: `10.3`)
* `mariadb_user` - login to connect on mariadb (default: `root`)
* `mariadb_password` - password to connect on mariadb (default: `secret`)
* `mariadb_master` - the server is master (default: `no`)
* `mariadb_autorestart` - restart mariadb when the config change (default: `no`)
* `mariadb_users` - array with the users to manage

```
- name: johndoe
  password: supersecret
  privileges:
    - 'database.*:SELECT,UPDATE'
  state: present
```

* `mariadb_databases` -  array with the databases to manage

```
- name: superprogram
  state: present
```

* `mariadb_config` -  hash with mariadb configuration

```
  mysqld:
    server-id: 1
    bind-address: 0.0.0.0
```

## How to use

```
- hosts: server
  roles:
    - mariadb
```

## Development

### Test syntax with yamllint

* install `python` and `python-pip`
* install yamllint `pip install yamllint`
* run `yamllint .`

### Test syntax with ansible-lint

* install `python` and `python-pip`
* install yamllint `pip install ansible-lint`
* run `ansible-lint .`

### Tests with docker

* install [docker](https://docs.docker.com/engine/installation/)
* install ruby
* install bundler `gem install bundler`
* install dependencies `bundle install`
* run the tests `kitchen test`

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
