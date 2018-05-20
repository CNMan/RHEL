# RHEL

## 官方文档
RHEL7:https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/?version=7

RHEL8:https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/?version=8

## 官方论坛
https://access.redhat.com/discussions

## Bug反馈
https://bugzilla.redhat.com/

## 注册订阅
```
subscription-manager register --username RHN_Username --password RHN_Password
subscription-manager list --available --all #效果等同于Red Hat Subscription Manager中的All Available Subscriptions页面（包括下面要用到的Pool IDs）
subscription-manager attach --pool=PoolIDs
subscription-manager list #效果等同于Red Hat Subscription Manager中的My Installed Products页面
subscription-manager list --consumed #效果等同于Red Hat Subscription Manager中的My Subscriptions页面
subscription-manager release --list #列出可用版本
subscription-manager release --set=7.7 #锁定特定版本
subscription-manager release --show #显示锁定的特定版本
subscription-manager release --unset #取消锁定特定版本
subscription-manager repos --disable="*"
subscription-manager repos --enable="rhel-7-server-rpms" #Red Hat Enterprise Linux 7 Server (RPMs)
subscription-manager repos --enable="rhel-7-server-supplementary-rpms" #Red Hat Enterprise Linux 7 Server - Supplementary (RPMs)
subscription-manager repos --enable="rhel-7-server-optional-rpms" #Red Hat Enterprise Linux 7 Server - Optional (RPMs)
subscription-manager repos --enable="rhel-7-server-extras-rpms" #Red Hat Enterprise Linux 7 Server - Extras (RPMs)
subscription-manager repos --enable="rhel-server-rhscl-7-rpms" #Red Hat Software Collections RPMs for Red Hat Enterprise Linux 7 Server
subscription-manager repos --enable="rhel-7-server-devtools-rpms" #Red Hat Developer Tools RPMs for Red Hat Enterprise Linux 7 Server
```

## 清除订阅
```
subscription-manager remove --all
subscription-manager unregister
subscription-manager clean
```

## 关闭SELinux及防火墙
```
sestatus -v #查看SELinux状态
sed -i 's/SELINUX=enforcing/SELINUX=disabled/g' /etc/selinux/config
systemctl status firewalld #查看防火墙状态
systemctl disable firewalld #关闭防火墙
```

## 开启时钟同步
```
timedatectl set-ntp yes
```

## 安装EPEL源及NTFS驱动
```
yum install https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
yum install ntfs-3g
```

## 安装RPM Fusion源及VLC Media Player
```
yum install https://download1.rpmfusion.org/free/el/rpmfusion-free-release-7.noarch.rpm
yum install https://download1.rpmfusion.org/nonfree/el/rpmfusion-nonfree-release-7.noarch.rpm
yum install vlc npapi-vlc
```
解决中文字幕乱码：http://forum.ubuntu.org.cn/viewtopic.php?t=201887

## 安装Google Chrome和Google Earth
https://www.google.com/linuxrepositories/index.html
```
yum install https://dl.google.com/linux/direct/google-chrome-stable_current_x86_64.rpm
yum install https://dl.google.com/dl/earth/client/current/google-earth-pro-stable-current.x86_64.rpm
```

## 安装Adobe源及Adobe Flash Player
```
yum install http://linuxdownload.adobe.com/adobe-release/adobe-release-x86_64-1.0-1.noarch.rpm
yum install flash-plugin #Adobe Flash Player NPAPI
yum install flash-player-ppapi #Adobe Flash Player PPAPI
```

## 安装SecureCRT和SecureFX
```
yum install scrt-sfx-8.5.4-1942.rhel7-64.x86_64.rpm
mkdir -p /home/username/.vandyke/SecureCRT/Config/
cp SecureCRT.lic /home/username/.vandyke/SecureCRT/Config/
cp SecureFX.lic /home/username/.vandyke/SecureCRT/Config/
```

## 安装VMware Workstation
参考[Install Workstation Pro on a Linux Host](https://docs.vmware.com/en/VMware-Workstation-Pro/14.0/com.vmware.ws.using.doc/GUID-1F5B1F14-A586-4A56-83FA-2E7D8333D5CA.html)
```
yum group install "Development tools"
yum install kernel-devel pcsc-lite-libs
curl -IsL https://www.vmware.com/go/getworkstation-linux | grep Location #获取最新的VMware Workstation for Linux下载链接
wget https://download3.vmware.com/software/wkst/file/VMware-Workstation-Full-15.5.0-14665864.x86_64.bundle
sha1sum VMware-Workstation-Full-15.5.0-14665864.x86_64.bundle #确认是4418d4b3f88aca15c2c4d7b2d26c76641910ae17
sh VMware-Workstation-Full-15.5.0-14665864.x86_64.bundle --console --ignore-errors --set-setting vmware-workstation serialNumber GU7HH-24W15-M88AP-MYMXC-ZZATA
```

## 配置无线连接
```
nano /etc/sysconfig/network-scripts/ifcfg-WIFI_SSID
	NAME=WIFI_SSID
	ONBOOT=yes
	IPADDR=192.168.0.102
	PREFIX=24
	GATEWAY=192.168.0.1
	DNS1=192.168.0.100
```

```
nano /etc/sysconfig/network-scripts/keys-WIFI_SSID
	WPA_PSK=WIFI_Password
```

```
service network restart
```

## 清除更新缓存
```
yum clean all
rm -rf /var/cache/yum/
```

## 安装Cisco AnyConnect Secure Mobility Client
```
yum install pangox-compat pangox-compat-devel
md5sum anyconnect-linux64-4.8.01090-predeploy-k9.tar.gz #确认是aeaeff30b489195f469f106cbcea537f
tar zxvf anyconnect-linux64-4.8.01090-predeploy-k9.tar.gz
cd anyconnect-linux64-4.8.01090/vpn/
./vpn_install.sh
```

## 修改启动菜单分辨率
```
nano /etc/default/grub
	GRUB_TERMINAL_OUTPUT="gfxterm"
	GRUB_CMDLINE_LINUX="crashkernel=auto rd.lvm.lv=rhel/root rd.lvm.lv=rhel/swap rhgb quiet vga=0x323" //先设vga=ask并重启查看支持的分辨率
	GRUB_GFXMODE=1366x768
grub2-mkconfig -o /boot/grub2/grub.cfg
reboot
```

## 安装gedit的插件
```
yum install gedit-plugin*
```

## 安装LibreOffice
```
yum group install "Office Suite and Productivity"
```

## 修正终端退格键显示^H而不是删除
```
nano .bash_profile
添加 stty erase ^H
```
## 清理终端命令历史记录
```
cat /dev/null > ~/.bash_history && history -c && exit
```

## 终端代理
```
nano .bashrc
	http(s)代理
	export http_proxy=192.168.0.100:8123
	export https_proxy=192.168.0.100:8123
	socks5代理(curl支持，wget不支持)
	export http_proxy=socks5://192.168.0.100:1080
	export https_proxy=socks5://192.168.0.100:1080
```

## 备份firefox密码
```
/home/username/.mozilla/firefox/xxxxxxx.default/logins.json
/home/username/.mozilla/firefox/xxxxxxx.default/key3.db
```

## 安装命令行BT下载软件Transmission
```
yum install transmission-cli
```

根据运行提示在`/etc/sysctl.conf`中加入两行
```
net.core.rmem_max = 4194304
net.core.wmem_max = 1048576
```

## `yum update`后关机依然提示`Install pending software updates`
```
rm -f /var/lib/PackageKit/prepared-update
```

## 禁用、启用自动更新
```
systemctl stop packagekit
systemctl mask packagekit
```

```
systemctl start packagekit
systemctl unmask packagekit
```

## 流量统计
```
yum install vnstat
systemctl enable vnstat
systemctl start vnstat
```

## 查看版本
```
cat /etc/redhat-release
uname -a
cat /proc/version
```

## 自定义欢迎消息
```
nano /etc/profile.d/login-info.sh
```

```
#! /usr/bin/env bash

# Basic info
RELEASE=`cat /etc/redhat-release | sed 's/Red Hat Enterprise Linux/RHEL/g' | tr -d '\n'`
KERNELVERSION=`uname -r | tr -d '\n'`
HOSTNAME=`uname -n`
IPADDRESS=`ip route get 1 | awk '{print $NF;exit}' | tr -d '\n'`
ROOT=`df -Ph | grep root | awk '{print $4}' | tr -d '\n'`

# System load
MEMORY1=`free -t -m | grep Total | awk '{print $3" MB";}'`
MEMORY2=`free -t -m | grep "Mem" | awk '{print $2" MB";}'`
LOAD1=`cat /proc/loadavg | awk {'print $1'}`
LOAD5=`cat /proc/loadavg | awk {'print $2'}`
LOAD15=`cat /proc/loadavg | awk {'print $3'}`

echo "
      _    _ _____ _     _____ ________  ___ _____ 
     | |  | |  ___| |   /  __ \  _  |  \/  ||  ___|
     | |  | | |__ | |   | /  \/ | | | .  . || |__  
     | |/\| |  __|| |   | |   | | | | |\/| ||  __| 
     \  /\  / |___| |___| \__/\ \_/ / |  | || |___ 
      \/  \/\____/\_____/\____/\___/\_|  |_/\____/ 
=========================================================
 - Release.............: $RELEASE
 - Kernel Version......: $KERNELVERSION
 - Hostname............: $HOSTNAME
 - IP Address..........: $IPADDRESS
 - Disk Space..........: $ROOT remaining
=========================================================
 - CPU usage...........: $LOAD1, $LOAD5, $LOAD15 (1, 5, 15 min)
 - Memory used.........: $MEMORY1 / $MEMORY2
 - Swap in use.........: `free -m | tail -n 1 | awk '{print $3}'` MB
=========================================================
"
```

## VIM 中文帮助
* https://github.com/yianwillis/vimcdoc
* http://yianwillis.github.io/vimcdoc/

## IPIP.NET linux客户端
```
# wget https://cdn.ipip.net/17mon/besttrace4linux.zip
# 7z x besttrace4linux.zip besttrace
# chmod +x besttrace
# chmod +s besttrace
$ ./besttrace 8.8.8.8
```

## [WPS](http://community.wps.cn/download/) For Linux

```
wget https://wdl1.cache.wps.cn/wps/download/ep/Linux2019/8392/wps-office-11.1.0.8392-1.x86_64.rpm
sha1sum wps-office-11.1.0.8392-1.x86_64.rpm #860e8ddb8c177cb243ca57ab50138b7bb56232b9
yum install wps-office-11.1.0.8392-1.x86_64.rpm
```

## LCDF Typetools
```
RHEL 7 没有这个工具的rpm包了
wget https://ftp5.gwdg.de/pub/opensuse/repositories/home:/mrdocs/RedHat_RHEL-6/x86_64/lcdf-typetools-2.105-2.1.x86_64.rpm
yum install lcdf-typetools-2.105-2.1.x86_64.rpm
```

## DVD 离线源
参考：[Need to set up yum repository for locally-mounted DVD on Red Hat Enterprise Linux 7](https://access.redhat.com/solutions/1355683)
```
mkdir /mnt/rhel7iso
mount -o loop rhel-server-7.7-x86_64-dvd.iso /mnt/rhel7iso/
cp /mnt/rhel7iso/media.repo /etc/yum.repos.d/rhel7dvd.repo
chmod 644 /etc/yum.repos.d/rhel7dvd.repo
nano /etc/yum.repos.d/rhel7dvd.repo
修改gpgcheck=0为gpgcheck=1；另加入三行：
	enabled=1
	baseurl=file:///mnt/rhel7iso/
	gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-redhat-release
yum clean all
subscription-manager clean
yum --noplugins list
yum --noplugins update
```

自动挂载
```
nano /etc/fstab
	rhel-server-7.7-x86_64-dvd.iso    /mnt/rhel7iso   udf,iso9660     user,auto,loop  0 0
```
