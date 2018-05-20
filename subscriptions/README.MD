[Production Support Terms of Service](https://access.redhat.com/support/offerings/production/sla)

[All Red Hat Store products](https://www.redhat.com/en/store/all-products)

[Buy Red Hat Enterprise Linux Developer Suite (SKU:RH2262474)](https://www.redhat.com/en/store/red-hat-enterprise-linux-developer-suite#?sku=RH2262474) US$99/Self-support(1 year)

开发者也可以根据[Red Hat Developer Program Benefits](https://developers.redhat.com/articles/red-hat-developer-program-benefits/)指引[注册](https://developers.redhat.com/register)免费订阅

[Developer Program Terms & Conditions](https://developers.redhat.com/terms-and-conditions/)

同个账号登录[Red Hat Customer Portal](https://access.redhat.com/)即Red Hat 客户门户网站[查看](https://access.redhat.com/management/subscriptions?type=all)，发现会给一个SKU为RH00798的Red Hat Developer Subscription免费订阅

![Imgur](https://i.imgur.com/haClscj.png)

```
# subscription-manager list --available --all
+-------------------------------------------+
    Available Subscriptions
+-------------------------------------------+
Subscription Name:   Red Hat Developer Subscription
Provides:
                     dotNET on RHEL (for RHEL Server)
                     dotNET on RHEL Beta (for RHEL Server)
                     MRG Realtime
                     Oracle Java (for RHEL Server)
                     Oracle Java (for RHEL Server) - Extended Update Support
                     Red Hat Ansible Engine
                     Red Hat Beta
                     Red Hat Container Development Kit
                     Red Hat Container Images
                     Red Hat Container Images Beta
                     Red Hat Developer Tools (for RHEL Server)
                     Red Hat Developer Tools Beta (for RHEL Server)
                     Red Hat Developer Toolset (for RHEL Server)
                     Red Hat Enterprise Linux Atomic Host
                     Red Hat Enterprise Linux Atomic Host Beta
                     Red Hat Enterprise Linux for ARM 64
                     Red Hat Enterprise Linux for ARM 64 Beta
                     Red Hat Enterprise Linux for Real Time
                     Red Hat Enterprise Linux for SAP
                     Red Hat Enterprise Linux for SAP Hana
                     Red Hat Enterprise Linux High Availability - Update Services for SAP Solutions
                     Red Hat Enterprise Linux High Availability (for RHEL Server)
                     Red Hat Enterprise Linux High Availability (for RHEL Server) - Extended Update Support
                     Red Hat Enterprise Linux High Performance Networking (for RHEL Compute Node)
                     Red Hat Enterprise Linux High Performance Networking (for RHEL Server)
                     Red Hat Enterprise Linux High Performance Networking (for RHEL Server) - Extended Update Support
                     Red Hat Enterprise Linux Load Balancer (for RHEL Server)
                     Red Hat Enterprise Linux Load Balancer (for RHEL Server) - Extended Update Support
                     Red Hat Enterprise Linux Resilient Storage (for RHEL Server)
                     Red Hat Enterprise Linux Resilient Storage (for RHEL Server) - Extended Update Support
                     Red Hat Enterprise Linux Scalable File System (for RHEL Server)
                     Red Hat Enterprise Linux Scalable File System (for RHEL Server) - Extended Update Support
                     Red Hat Enterprise Linux Server
                     Red Hat Enterprise Linux Server - Extended Update Support
                     Red Hat Enterprise Linux Server - Update Services for SAP Solutions
                     Red Hat EUCJP Support (for RHEL Server) - Extended Update Support
                     Red Hat S-JIS Support (for RHEL Server) - Extended Update Support
                     Red Hat Software Collections (for RHEL Server)
                     Red Hat Software Collections Beta (for RHEL Server)
                     RHEL for SAP - Extended Update Support
                     RHEL for SAP - Update Services for SAP Solutions
                     RHEL for SAP (for IBM Power LE) - Update Services for SAP Solutions
                     RHEL for SAP HANA - Extended Update Support
                     RHEL for SAP HANA - Update Services for SAP Solutions
SKU:                 RH00798
Contract:            
Pool ID:             xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
Provides Management: No
Available:           16
Suggested:           1
Service Level:       Self-Support
Service Type:        
Subscription Type:   Standard
Ends:                04/29/2019
System Type:         Physical
```

```
# subscription-manager list --consumed
+-------------------------------------------+
   Consumed Subscriptions
+-------------------------------------------+
Subscription Name:   Red Hat Developer Subscription
Provides:
                     dotNET on RHEL (for RHEL Server)
                     dotNET on RHEL Beta (for RHEL Server)
                     MRG Realtime
                     Oracle Java (for RHEL Server)
                     Oracle Java (for RHEL Server) - Extended Update Support
                     Red Hat Ansible Engine
                     Red Hat Beta
                     Red Hat Container Development Kit
                     Red Hat Container Images
                     Red Hat Container Images Beta
                     Red Hat Developer Tools (for RHEL Server)
                     Red Hat Developer Tools Beta (for RHEL Server)
                     Red Hat Developer Toolset (for RHEL Server)
                     Red Hat Enterprise Linux Atomic Host
                     Red Hat Enterprise Linux Atomic Host Beta
                     Red Hat Enterprise Linux for ARM 64
                     Red Hat Enterprise Linux for ARM 64 Beta
                     Red Hat Enterprise Linux for Real Time
                     Red Hat Enterprise Linux for SAP
                     Red Hat Enterprise Linux for SAP Hana
                     Red Hat Enterprise Linux High Availability - Update Services for SAP Solutions
                     Red Hat Enterprise Linux High Availability (for RHEL Server)
                     Red Hat Enterprise Linux High Availability (for RHEL Server) - Extended Update Support
                     Red Hat Enterprise Linux High Performance Networking (for RHEL Compute Node)
                     Red Hat Enterprise Linux High Performance Networking (for RHEL Server)
                     Red Hat Enterprise Linux High Performance Networking (for RHEL Server) - Extended Update Support
                     Red Hat Enterprise Linux Load Balancer (for RHEL Server)
                     Red Hat Enterprise Linux Load Balancer (for RHEL Server) - Extended Update Support
                     Red Hat Enterprise Linux Resilient Storage (for RHEL Server)
                     Red Hat Enterprise Linux Resilient Storage (for RHEL Server) - Extended Update Support
                     Red Hat Enterprise Linux Scalable File System (for RHEL Server)
                     Red Hat Enterprise Linux Scalable File System (for RHEL Server) - Extended Update Support
                     Red Hat Enterprise Linux Server
                     Red Hat Enterprise Linux Server - Extended Update Support
                     Red Hat Enterprise Linux Server - Update Services for SAP Solutions
                     Red Hat EUCJP Support (for RHEL Server) - Extended Update Support
                     Red Hat S-JIS Support (for RHEL Server) - Extended Update Support
                     Red Hat Software Collections (for RHEL Server)
                     Red Hat Software Collections Beta (for RHEL Server)
                     RHEL for SAP - Extended Update Support
                     RHEL for SAP - Update Services for SAP Solutions
                     RHEL for SAP (for IBM Power LE) - Update Services for SAP Solutions
                     RHEL for SAP HANA - Extended Update Support
                     RHEL for SAP HANA - Update Services for SAP Solutions
SKU:                 RH00798
Contract:            
Account:             
Serial:              xxxxxxxxxxxxxxxxxxx
Pool ID:             xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
Provides Management: No
Active:              True
Quantity Used:       1
Service Level:       Self-Support
Service Type:        
Status Details:      Subscription is current
Subscription Type:   Standard
Starts:              04/29/2018
Ends:                04/29/2019
System Type:         Physical
```