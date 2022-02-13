##

在阅读了[这篇文章](https://iyideng.vip/black-technology/cgfw/vpn-ss-ssr-v2ray-trojan-wireguard-bypass-gfw.html)之后了解到Trojan-Go当前似乎是一个不错的工具，于是继续阅读了[更详细的介绍](https://iyideng.vip/black-technology/cgfw/trojan-go.html)去了解更详细的信息，知道了首先需要准备一个国外的VPS和域名。

在购买VPS的时候从[trojan-go一键脚本](https://v2xtls.org/trojan-go%e4%b8%80%e9%94%ae%e8%84%9a%e6%9c%ac/)了解到不少厂商，从[CN2 GIA VPS商家推荐](https://v2xtls.org/cn2-gia-vps%e5%92%8c%e5%95%86%e5%ae%b6%e6%8e%a8%e8%8d%90/)选了一家便宜的[AkkoCloud](https://www.akkocloud.com/)。并在[Namesilo](https://iyideng.vip/note/namesilo-domain-registrar.html)购买了域名。

在[](https://iyideng.vip/black-technology/cgfw/trojan-server-building-and-using-tutorial.html)有更详细的知道，购买了域名之后，通常域名服务商会提供域名解析服务，当然也可以使用诸如[](https://dash.cloudflare.com/sign-up)专业的CDN服务。

之后就参照[](https://iyideng.vip/black-technology/cgfw/trojan-go.html)一步一步来：

1）安装curl

```
yum -y install curl #CentOS
apt -y install curl #Debian/Ubuntu
```

2）执行脚本并选择1，安装过程中出现了很多提示文件不存在的告警

```
bash -c "$(curl -fsSL https://raw.githubusercontent.com/JeannieStudio/all_install/master/trojan-go_install.sh)"
```

[Sun Feb 13 15:34:28 CST 2022] Your cert is in: /root/.acme.sh/everydaynote.xyz_ecc/everydaynote.xyz.cer
[Sun Feb 13 15:34:28 CST 2022] Your cert key is in: /root/.acme.sh/everydaynote.xyz_ecc/everydaynote.xyz.key
[Sun Feb 13 15:34:28 CST 2022] The intermediate CA cert is in: /root/.acme.sh/everydaynote.xyz_ecc/ca.cer
[Sun Feb 13 15:34:28 CST 2022] And the full chain certs is there: /root/.acme.sh/everydaynote.xyz_ecc/fullchain.cer
[信息] TLS 证书测试签发成功，开始正式签发
[Sun Feb 13 15:34:31 CST 2022] Using CA: https://acme.zerossl.com/v2/DV90
[Sun Feb 13 15:34:31 CST 2022] Standalone mode.
[Sun Feb 13 15:34:31 CST 2022] Create account key ok.
[Sun Feb 13 15:34:31 CST 2022] No EAB credentials found for ZeroSSL, let's get one
[Sun Feb 13 15:34:31 CST 2022] acme.sh is using ZeroSSL as default CA now.
[Sun Feb 13 15:34:31 CST 2022] Please update your account with an email address first.
[Sun Feb 13 15:34:31 CST 2022] acme.sh --register-account -m my@example.com
[Sun Feb 13 15:34:31 CST 2022] See: https://github.com/acmesh-official/acme.sh/wiki/ZeroSSL.com-CA
[Sun Feb 13 15:34:31 CST 2022] Please add '--debug' or '--log' to check more details.
[Sun Feb 13 15:34:31 CST 2022] See: https://github.com/acmesh-official/acme.sh/wiki/How-to-debug-acme.sh
[错误] TLS 证书生成失败

按照上面的提示访问https://github.com/acmesh-official/acme.sh/wiki/ZeroSSL.com-CA，没有看出所以然干脆直接安装了acme再重新尝试成功：

```
git clone https://github.com/acmesh-official/acme.sh.git
cd ./acme.sh
./acme.sh --install -m my@example.com
```

3) 加速（暂时没有使用）

4) 选择6开启服务

```
/etc/trojan_mgr.sh
```

之后在[Trojan-Qt5各平台客户端下载汇总

](https://ssrvps.org/archives/7656)下载客户端，但是链接超时，搜索之下回到[Trojan-Go](https://iyideng.vip/black-technology/cgfw/trojan-go.html)发现Trojan-GO在PC端暂不支持CDN，于是到Cloudflare去把CDN取消之后就可以了（设置让小云朵变为灰色）。

参考：

- [Trojan-Go 安装配置教程](https://qoant.com/2020/06/vps-with-trojan-go/)
