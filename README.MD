# RHEL

## [生命周期](https://access.redhat.com/support/policy/updates/errata)
|Version|General availability|Full support ends|Maintenance Support 1 ends|Maintenance Support or Maintenance Support 2 ends|Extended life cycle support (ELS) add-on ends|Extended life phase ends|Last minor release|
|------|------|------|------|------|------|------|------|
|10|20250520|20300531|Not Applicable|20350531|20380531|Ongoing|10.10|
|9|20220518|20270531|Not Applicable|20320531|20350531|Ongoing|9.10|
|8|20190507|20240531|Not Applicable|20290531|20320531|Ongoing|8.10|
|7|20140610|20190806|20200806|20240630|20280630|Ongoing|7.9|
|6|20101110|20160510|20170510|20201130|20240630|Ongoing|6.10|
|5|20070315|20130108|20140131|20170331|20201130|Ongoing|5.11|
|4|20050214|20090331|20110216|20120229|20170331|Ongoing|4.9|
|3|20031023|20060720|20070630|20101031|20140130|20140130||

## 官方文档
RHEL7:https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7

RHEL8:https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8

RHEL9:https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9

RHEL10:https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/10

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
subscription-manager release --set=8.10 #锁定特定版本
subscription-manager release --show #显示锁定的特定版本
subscription-manager release --unset #取消锁定特定版本
subscription-manager repos --disable="*"
subscription-manager repos --enable="rhel-8-for-x86_64-baseos-rpms" #Red Hat Enterprise Linux 8 for x86_64 - BaseOS (RPMs)
subscription-manager repos --enable="rhel-8-for-x86_64-appstream-rpms" #Red Hat Enterprise Linux 8 for x86_64 - AppStream (RPMs)
subscription-manager repos --enable="rhel-8-for-x86_64-supplementary-rpms" #Red Hat Enterprise Linux 8 for x86_64 - Supplementary (RPMs)
subscription-manager repos --enable="codeready-builder-for-rhel-8-x86_64-rpms" #Red Hat CodeReady Linux Builder for RHEL 8 x86_64 (RPMs)
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
yum install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm
yum install ntfs-3g ntfs-3g-libs
```

## 安装RPM Fusion源及VLC Media Player、exFAT驱动
```
yum install https://download1.rpmfusion.org/free/el/rpmfusion-free-release-8.noarch.rpm
yum install https://download1.rpmfusion.org/nonfree/el/rpmfusion-nonfree-release-8.noarch.rpm
yum install vlc exfat-utils fuse-exfat
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
注册试用并下载SecureCRT + SecureFX 9.3 Bundle：https://www.vandyke.com/download/index.html
```
yum install pcre2-utf16 xcb-util-image xcb-util-keysyms xcb-util-renderutil xcb-util-wm
sha1sum scrt-sfx-9.3.2-2978.rhel8-64.x86_64.rpm #确认是147E230325DB436FC8576ED866A48D8C02204125
yum install scrt-sfx-9.3.2-2978.rhel8-64.x86_64.rpm
mkdir -p /home/username/.vandyke/SecureCRT/Config/
cp SecureCRT.lic /home/username/.vandyke/SecureCRT/Config/
cp SecureFX.lic /home/username/.vandyke/SecureCRT/Config/
```

## 安装VMware Workstation
参考[Install Workstation Pro on a Linux Host](https://docs.vmware.com/en/VMware-Workstation-Pro/17/com.vmware.ws.using.doc/GUID-1F5B1F14-A586-4A56-83FA-2E7D8333D5CA.html)
```
yum group install "Development Tools"
yum install elfutils-libelf-devel pcsc-lite-libs
ln -s /usr/lib64/libnsl.so.2 /usr/lib64/libnsl.so.1
sha1sum VMware-Workstation-Full-17.0.2-21581411.x86_64.bundle #确认是3c75575db021720b9746e7a0fc58513151001826
sh VMware-Workstation-Full-17.0.2-21581411.x86_64.bundle --console --ignore-errors --set-setting vmware-workstation serialNumber MC60H-DWHD5-H80U9-6V85M-8280D
```

```
sha1sum VMware-Workstation-Full-17.5.2-23775571.x86_64.bundle #确认是23593d98a396c55f42c6e1967be47108d6767a03
sh VMware-Workstation-Full-17.5.2-23775571.x86_64.bundle --console --ignore-errors --set-setting vmware-workstation serialNumber MC60H-DWHD5-H80U9-6V85M-8280D
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
systemctl restart NetworkManager.service
```

## 清除更新缓存
```
yum clean all
rm -rf /var/cache/yum/
rm -rf /var/cache/dnf/
```

## 安装[Cisco Secure Client(including AnyConnect)](https://software.cisco.com/download/home/286330811/type/282364313)
```
md5sum cisco-secure-client-linux64-5.1.3.62-predeploy-rpm-k9.tar.gz #确认是778539e3eff05876869632a091a04bd2
tar zxvf cisco-secure-client-linux64-5.1.3.62-predeploy-rpm-k9.tar.gz
yum install cisco-secure-client-vpn-5.1.3.62-1.x86_64.rpm
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
/home/username/.mozilla/firefox/xxxxxxx.default-default/logins.json
/home/username/.mozilla/firefox/xxxxxxx.default-default/key3.db
/home/username/.mozilla/firefox/xxxxxxx.default-default/key4.db
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
# 7z x besttrace4linux.zip besttraceipip
# chmod +x besttraceipip
# chmod +s besttraceipip
$ ./besttraceipip 8.8.8.8
```

## [WPS Office for Linux](https://www.wps.com/office/linux/)

```
wget https://wdl1.pcfg.cache.wpscdn.com/wpsdl/wpsoffice/download/linux/11719/wps-office-11.1.0.11719.XA-1.x86_64.rpm
sha1sum wps-office-11.1.0.11719.XA-1.x86_64.rpm #b75660011e58bc85be3b4b18add24380b13f47df
yum install wps-office-11.1.0.11719.XA-1.x86_64.rpm
```

## LCDF Typetools
```
RHEL 7/8 没有这个工具的rpm包了
wget https://ftp5.gwdg.de/pub/opensuse/repositories/home:/mrdocs/RedHat_RHEL-6/x86_64/lcdf-typetools-2.105-2.1.x86_64.rpm
yum install lcdf-typetools-2.105-2.1.x86_64.rpm
```

## DVD 离线源
参考：[Need to set up yum repository for locally-mounted DVD on Red Hat Enterprise Linux 8](https://access.redhat.com/solutions/3776721)
```
mkdir /mnt/rhel8iso
mkdir /mnt/rhel8suppiso
mount -o loop rhel-8.10-x86_64-dvd.iso /mnt/rhel8iso/
mount -o loop supp-supplementary-8.10-rhel-8-x86_64-dvd.iso /mnt/rhel8suppiso/
touch /etc/yum.repos.d/rhel8iso.repo
chmod 644 /etc/yum.repos.d/rhel8iso.repo
nano /etc/yum.repos.d/rhel8iso.repo
	[InstallMedia-BaseOS]
	name=Red Hat Enterprise Linux 8 - BaseOS
	baseurl=file:///mnt/rhel8iso/BaseOS
	enabled=1
	gpgcheck=1
	gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-redhat-release
	priority=1

	[InstallMedia-AppStream]
	name=Red Hat Enterprise Linux 8 - AppStream
	baseurl=file:///mnt/rhel8iso/AppStream
	enabled=1
	gpgcheck=1
	gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-redhat-release
	priority=1

	[InstallMedia-Supplementary]
	name=Red Hat Enterprise Linux 8 - Supplementary
	baseurl=file:///mnt/rhel8suppiso
	enabled=1
	gpgcheck=1
	gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-redhat-release
	priority=1
yum clean all
subscription-manager clean
yum --noplugins list
yum --noplugins update
```

自动挂载
```
nano /etc/fstab
	rhel-8.10-x86_64-dvd.iso	/mnt/rhel8iso	udf,iso9660	user,auto,loop,nofail	0 0
	supp-supplementary-8.10-rhel-8-x86_64-dvd.iso	/mnt/rhel8suppiso	udf,iso9660	user,auto,loop,nofail	0 0
```

## 设置SSH key files permission
```
chmod 700 ~/.ssh
chmod 600 ~/.ssh/authorized_keys
chmod 600 ~/.ssh/config
chmod 600 ~/.ssh/id_ecdsa
chmod 600 ~/.ssh/id_ecdsa.pub
chmod 600 ~/.ssh/id_ed25519
chmod 600 ~/.ssh/id_ed25519.pub
chmod 600 ~/.ssh/id_rsa
chmod 600 ~/.ssh/id_rsa.pub
```

## 安装中文输入法，重启，再在语言设置里添加生效
```
yum install ibus-libpinyin	#拼音输入法
yum install ibus-table-chinese-wubi-haifeng	#海峰五笔
yum install ibus-table-chinese-wubi-jidian	#极点五笔
```

## 安装并更改主题
```
yum install gnome-tweaks sassc inkscape optipng glib2-devel gtk2-engines gtk-murrine-engine
```

以下命令用普通用户运行即可
```
git clone https://github.com/vinceliuice/Mojave-gtk-theme.git
git clone https://github.com/vinceliuice/McMojave-circle.git
cd Mojave-gtk-theme/
./install.sh
cd ../McMojave-circle/
./install.sh
```

## 写入USB镜像
```
umount /dev/sdc1
umount /dev/sdc2
dd if=rhel-8.10-x86_64-dvd.iso of=/dev/sdc bs=1M conv=fsync
```

```
13575+0 records in
13575+0 records out
14234419200 bytes (14 GB, 13 GiB) copied, 2993.75 s, 4.8 MB/s
```
