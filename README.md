JSON API умного дома
====================

Для курсовой работы по созданию датчика отопления был реализован
небольшой бэкэнд на shell-скриптах, позволяющий обрабатывать и
отдавать JSON API для внешних клиентов.

Требования
----------

Для работы необходимы:

  - jq — cli-утилита для обработки JSON
  - sh, awk
  - python
  - bluetoothctl, rfcomm

Quick start
-----------

```bash
$ git clone http://github.com/ifmo-smarthome/backend-heating /srv/www/smarthome
$ sudo rfcomm bind 1 20:15:12:08:26:46 # стандартный MAC-адрес HC-06
$ sudo chown :www-data /dev/rfcomm1 && sudo chmod 660 /dev/rfcomm1
$ touch /srv/www/smarthome/{mode,min_temperature,temperature}
$ chmod 666 /srv/www/smarthome/{mode,min_temperature,temperature}
$ sudo sh -c "nohup ./daemon.sh > /dev/null 2>&1 &"
$ cat > /etc/apache2/sites-available/smarthome.conf <<EOF
<VirtualHost *:8080>
  ServerName smart.test.ru
  DocumentRoot /srv/www/smarthome
  <Directory /srv/www/smarthome>
    Options +ExecCGI
    AddHandler cgi-script .cgi
    Require all granted
    DirectoryIndex index.cgi
    Header set Access-Control-Allow-Origin "*"
  </Directory>
</VirtualHost>
EOF
$ ln -sf /etc/apache2/sites-available/smarthome.conf /etc/apache2/sites-enabled/
$ service apache2 restart
```
