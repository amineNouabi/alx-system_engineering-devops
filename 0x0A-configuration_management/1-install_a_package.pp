# Install Flask version 2.1.0 package using pip3
package { 'Flask':
  command  => 'pip3 install Flask==2.1.0',
  provider => 'shell',
}
