import os, re
import testinfra.utils.ansible_runner

def test_packages(host):
  for package_name in ['mariadb-server', 'python-mysqldb']:
    package = host.package(package_name)
    assert package.is_installed

def test_config_file(host):
  config = host.file('/etc/mysql/my.cnf')
  assert config.exists
  assert config.is_file
  assert config.user == 'root'
  assert config.group == 'root'
  assert config.mode == 0o644
  assert config.contains('server-id = 5')

def test_data_directory(host):
  config = host.file('/opt/mariadb')
  assert config.exists
  assert config.is_directory
  assert config.user == 'mysql'
  assert config.group == 'root'
  assert config.mode == 0o750

def test_service(host):
  service = host.service('mysql')
  assert service.is_running
  assert service.is_enabled

def test_socket(host):
  socket = host.socket('tcp://127.0.0.1:3306')
  assert socket.is_listening

def test_user_exists(host):
  result = host.check_output('mysql -uroot -psecret -e "show grants for toto@\'%\'"')
  assert re.search('toto.*%', result)

def test_root_user(host):
  result = host.check_output('mysql -uroot -psecret -e "select count(*) from mysql.user where user=\'root\'"')
  assert '1' in result

def test_grant_access(host):
  result = host.check_output('mysql -uroot -psecret -e "show grants for toto@\'%\'"')
  assert "GRANT ALL PRIVILEGES ON `test`.* TO 'toto'@'%'" in result

def test_logbin_enabled(host):
  result = host.check_output('mysql -uroot -psecret -e "show variables where variable_name = \'log_bin\'"')
  assert 'ON' in result
