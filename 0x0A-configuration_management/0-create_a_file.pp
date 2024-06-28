# Create a file with Puppet
file {
    'school':
    ensure      => file,
    path        => '/tmp/school',
    content     => 'I love Puppet',
    group       => 'www_data',
    owner       => 'www_data',
    permissions => '0744',
}
