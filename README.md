# Flowers website

Website to add/remove pictures and display them.

Self-host this on a Linux server.

Install:

```bash
sudo apt-get install nginx perl libdata-uuid-perl libcgi-pm-perl
```

Copy the nginx config from `nginx.conf` to `/etc/nginx/nginx.conf`.

Create admin password

```bash
sudo htpasswd -c /var/www/flowers/.htpasswd <user>
```
