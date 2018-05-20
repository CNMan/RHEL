## 配置字体
```
wget https://github.com/CNMan/RHEL/raw/master/fontconfig/99-language-selector-zh.conf
mv 99-language-selector-zh.conf /usr/share/fontconfig/conf.avail/
ln -s /usr/share/fontconfig/conf.avail/99-language-selector-zh.conf /etc/fonts/conf.d/
fc-cache -fv
```

## 参考资料
* https://www.freedesktop.org/software/fontconfig/fontconfig-user.html
* https://packages.ubuntu.com/search?keywords=fontconfig-config
* https://packages.ubuntu.com/search?keywords=language-selector-common
* http://www.jinbuguo.com/gui/fonts.conf.html
* http://www.jinbuguo.com/gui/linux_fontconfig.html
* http://www.jinbuguo.com/gui/fonts.conf.xml
* https://wiki.archlinux.org/index.php/Font_Configuration/Chinese_Font_Configurations_(简体中文)
* https://wiki.ubuntu-tw.org/index.php?title=HowtoCustomFontswithFontconfig
* https://my.oschina.net/klauszl/blog/262632
* https://websemantics.uk/articles/font-size-conversion/

```
conf.d/README

Each file in this directory is a fontconfig configuration file.  Fontconfig
scans this directory, loading all files of the form [0-9][0-9]*.conf.
These files are normally installed in /usr/share/fontconfig/conf.avail
and then symlinked here, allowing them to be easily installed and then
enabled/disabled by adjusting the symlinks.

The files are loaded in numeric order, the structure of the configuration
has led to the following conventions in usage:

 Files begining with:	Contain:
 
 00 through 09		Font directories
 10 through 19		system rendering defaults (AA, etc)
 20 through 29		font rendering options
 30 through 39		family substitution
 40 through 49		generic identification, map family->generic
 50 through 59		alternate config file loading
 60 through 69		generic aliases, map generic->family
 70 through 79		select font (adjust which fonts are available)
 80 through 89		match target="scan" (modify scanned patterns)
 90 through 99		font synthesis
```

## Fonts from Windows
```
wget 'https://codeload.github.com/CNMan/WindowsFonts/zip/master' -O WindowsFonts.zip
sha1sum:
d5b59edb053ba89c665926e38b8a47d056783505  WindowsFonts.zip
```

## 花園明朝
```
日本完整涵盖CJK Ext.A、Ext.B、Ext.C、Ext.D、Ext.E、Ext.F的字体
wget 'http://gigenet.dl.osdn.jp/hanazono-font/68253/hanazono-20170904.zip'
sha1sum:
e9cd9ee769be986d7b468c0461b185a9d5647e14  hanazono-20170904.zip
```

## 中华书局宋体
```
国产完整涵盖CJK Ext.A、Ext.B、Ext.C、Ext.D、Ext.E、Ext.F的字体
http://www.ancientbooks.cn/helpcore?font
```

## Noto Serif CJK SC/Noto Sans CJK SC/Noto Sans Mono CJK SC
```
wget 'https://noto-website-2.storage.googleapis.com/pkgs/NotoSansCJKsc-hinted.zip'
wget 'https://noto-website-2.storage.googleapis.com/pkgs/NotoSerifCJKsc-hinted.zip'
全部Noto系列
wget 'https://noto-website-2.storage.googleapis.com/pkgs/Noto-hinted.zip'
文件列表可以参考Noto-hinted.zip.filelist
sha1sum:
e38b784f26cfc08ab81348d63e0c05e15560d791  NotoSansCJKsc-hinted.zip
9369a3524417ecb2b5cbab1b21f8b07ac73ec89c  NotoSerifCJKsc-hinted.zip
7a9828c10a1de39bbce91006a52f74b9a4878981  Noto-hinted.zip
```

## Source Han Serif SC/Source Han Sans SC/Source Han Sans HW SC
```
wget 'https://raw.githubusercontent.com/adobe-fonts/source-han-sans/release/OTF/SourceHanSansHWSC.zip'
wget 'https://raw.githubusercontent.com/adobe-fonts/source-han-sans/release/OTF/SourceHanSansSC.zip'
wget 'https://raw.githubusercontent.com/adobe-fonts/source-han-serif/release/OTF/SourceHanSerifSC_EL-M.zip'
wget 'https://raw.githubusercontent.com/adobe-fonts/source-han-serif/release/OTF/SourceHanSerifSC_SB-H.zip'
sha1sum:
d7f878878a0eb0e75ff1c0e8dad8e3401e4f29f9  SourceHanSansHWSC.zip
a8288083891d407211603d16f48a67b087feb80c  SourceHanSansSC.zip
976ad131a971b7971511390e8ab4bc0a0d2884a0  SourceHanSerifSC_EL-M.zip
a4a6a26b43dd72b7206d5132fdbc1b7b1604ed22  SourceHanSerifSC_SB-H.zip
```

## 其他字体
```
https://releases.pagure.org/liberation-fonts/liberation-fonts-ttf-2.00.1.tar.gz #RHEL7 自带的是1.07.2
https://assets.ubuntu.com/v1/fad7939b-ubuntu-font-family-0.83.zip
```
