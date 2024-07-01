# ssh setup for the server
file { 'Declare identity file':
  path    => '/root/.ssh/config',
  ensure  => file,
  content => "Host 273190-web-01\n  HostName 273190-web-01\n  IdentityFile ~/.ssh/school\n  IdentitiesOnly yes\n",
}

file { 'Turn off password authentication':
  path    => '/etc/ssh/sshd_config',
  ensure  => file,
  content => "PasswordAuthentication no\n",
}
