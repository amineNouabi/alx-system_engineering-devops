# Configure an ngix web server with Puppet

exec {'update system':
  command => '/usr/bin/apt update',
}

package {'nginx':
  ensure  => installed,
  require => Exec['update system'],
}

file {'/var/www/html/index.html':
  content => 'Hello World!',
}

exec {'redirect_me':
  command  => 'sed -i "/^\tlocation \/ {/i\ \tlocation \/redirect_me {\n\t\treturn 301 https:\/\/www.youtube.com\/watch?v=QH2-TGUlwu4;\n\t}" /etc/nginx/sites-available/default',
  provider => shell,
}

file {'/var/www/html/404.html':
  content => 'Ceci n\'est pas une page',
}

exec {'custom_header':
  command  => 'sed -i "/^\tlocation \/ {/i\ \tadd_header X-Served-By $HOSTNAME;" /etc/nginx/sites-available/default',
  provider => shell,
}

service {'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}
