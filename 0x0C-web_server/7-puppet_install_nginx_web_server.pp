# Configure an ngix web server with Puppet
# with /redirect_me to the specified YouTube video


exec {'update system':
  command => '/usr/bin/apt update',
}

package {'nginx':
  ensure  => installed,
  require => Exec['update system'],
}

file {'/var/www/html/index.html':
  ensure  => file,
  content => 'Hello World!',
}

exec {'redirect_me':
  command  => 'sed -i "/^\tlocation \/ {/i\ \tlocation \/redirect_me {\n\t\treturn 301 https:\/\/www.youtube.com\/watch?v=QH2-TGUlwu4;\n\t}" /etc/nginx/sites-available/default',
  provider => shell,
}

file {'/var/www/html/404.html':
  ensure  => file,
  content => 'Ceci n\'est pas une page',
}

service {'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}
