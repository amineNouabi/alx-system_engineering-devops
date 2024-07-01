# ssh setup for the server
file { '/etc/ssh/sshd_config':
  ensure => present,
  content => template('ssh/sshd_config.erb'),
  owner => 'root',
  group => 'root',
  mode => '0644',
}
