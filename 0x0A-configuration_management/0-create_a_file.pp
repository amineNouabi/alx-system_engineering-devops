# Create a file with Puppet
file {
    'school':
    path        => '/tmp/school',
    ensure      => file,
    content     => 'I love Puppet',
    group       => 'www_data',
    owner       => 'www_data',
    permissions => '0744',
}
