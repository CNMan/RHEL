```
yum clean all --verbose
rm -rf /var/cache/dnf/*
rm -rf /var/cache/yum/*
yum makecache
yum update
yum list all | grep -v 'Last metadata expiration check' > yumlistall.txt
```
