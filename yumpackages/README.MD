```
yum clean all --verbose
rm -rf /var/cache/dnf/*
rm -rf /var/cache/yum/*
yum makecache
yum update --refresh -y
yum list all | grep -v 'Last metadata expiration check' > yumlistall.txt
```
