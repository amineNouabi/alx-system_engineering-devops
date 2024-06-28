# Create a file with Puppet

file {
	'/tmp/school':
	content => "I love Puppet";
	ensure => file,
	group => 'www_data',
	owner => 'www_data',
	permissions => '0744',
}
