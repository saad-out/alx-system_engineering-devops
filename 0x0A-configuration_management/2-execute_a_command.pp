# Execute command
exec {'killmenow':
timeout => 0,
command => '/bin/pkill -f "killmenow"',
}
