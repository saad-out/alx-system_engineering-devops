# Replace a line in file
file_line {'Turn_off_passwd_auth':
path  => 'ssh_config',
line  => '\tPasswordAuthentication no\n\tIdentityFile ~/.ssh/school',
after => 'GSSAPIAuthentication yes'
}
