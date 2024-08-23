# Fix High requests issue

exec {'increase_nginx_open_files':
  provider => shell,
  command  => 'sudo sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 4096\"/" /etc/default/nginx',
}

exec {'restart_nginx':
  provider => shell,
  command  => 'sudo service nginx restart',
  require  => Exec['increase_nginx_open_files'],
}
