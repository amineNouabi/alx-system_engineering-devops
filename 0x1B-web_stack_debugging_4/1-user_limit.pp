# Removes limits for the user holberton

exec {'replace-5':
  provider => shell,
  command  => 'sudo sed -i "s/nofile 5/nofile 70000/" /etc/security/limits.conf',
}

exec {'replace-4':
  provider => shell,
  command  => 'sudo sed -i "s/nofile 4/nofile 70000/" /etc/security/limits.conf',
  require  => Exec['replace-5'],
}
