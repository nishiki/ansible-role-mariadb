require 'serverspec'

set :backend, :exec

puts
puts '================================'
puts %x(ansible --version)
puts '================================'

%w[
  mariadb-server
  python-mysqldb
].each do |name|
  describe package(name) do
    it { should be_installed }
  end
end

describe file('/etc/mysql/mariadb.cnf') do
  it { should be_file }
  it { should be_mode 644 }
  it { should be_owned_by 'root' }
  it { should be_grouped_into 'root' }
  it { should contain 'server-id = 5' }
end

describe service('mysql') do
  it { should be_enabled }
  it { should be_running.under('systemd') }
end

describe port(3306) do
  it { should be_listening }
end

describe command('mysql -u root -e "show databases"') do
  its(:exit_status) { should eq 0 }
  its(:stdout) { should contain 'test' }
end

describe command('mysql -u root -e "select user, host from mysql.user"') do
  its(:exit_status) { should eq 0 }
  its(:stdout) { should contain(/toto.*%/) }
end

describe command('mysql -u root -e "show grants for toto@\'%\'"') do
  its(:exit_status) { should eq 0 }
  its(:stdout) do
    should contain "GRANT ALL PRIVILEGES ON `test`.* TO 'toto'@'%'"
  end
end

describe command('mysql -u root -e "show variables where variable_name = \'log_bin\'"') do
  its(:exit_status) { should eq 0 }
  its(:stdout) { should contain 'ON' }
end
