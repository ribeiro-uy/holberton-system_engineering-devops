# Script increases the limit of requests allowed nginx server
exec { 'limit_requests_increase':
command => 'sed -i "s/15/30000/g" /etc/default/nginx; sudo service nginx restart',
path    => ['/usr/bin', '/sbin', '/bin', '/usr/sbin']
}
