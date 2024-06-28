# Create a file with Puppet
file {
    'school':
    ensure      => file,
    path        => '/tmp/school',
    content     => 'I love Puppet',
    group       => 'www-data',
    owner       => 'www-data',
    permissions => '0744',
}
