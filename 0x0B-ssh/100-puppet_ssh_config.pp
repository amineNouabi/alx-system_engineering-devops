# ssh setup for the server
file { 'Declare identity file':
  ensure  => file,
  path    => '/root/.ssh/config',
  content => "Host 273190-web-01\n  HostName 273190-web-01\n  IdentityFile ~/.ssh/school\n  IdentitiesOnly yes\n",
}

file { 'Turn off password authentication':
  ensure  => file,
  path    => '/etc/ssh/sshd_config',
  content => "PasswordAuthentication no\n",
}
