# Removes limits for the user holberton

exec {'remove_limits':
  command => 'sed -i "/^holberton/d" /etc/security/limits.conf',
}
