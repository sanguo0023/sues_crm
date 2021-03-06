企业部署指南
============================

>
> 注意：课程作业托管，未完全版，请勿作为商业项目使用，继续开发时间预计，二〇一四年九月份之后，多谢理解。
>

## 环境配置
开发环境为`Ubuntu 13.10`，开发组建议您使用相近似的服务器环境配置，其中各项参数如下：

 1. 必要环境
     - `Linux`服务器一台
     - `Python2.7`以上版本（建议Python3）
     - `Django1.5`以上（建议1.6.2）
     - `源代码`一份（获取最新版请移步[Github][1]）
     - `Apache`或其他服务器环境（相关知识请参考各自的配置手册）
 2. 可选环境
     - `PIL`（开启图片存储，详情请见开发者文档）

下面以Ubuntu发行版为例讲解平台部署步骤，其他Linux发行版请使用各自的包管理软件

## 安装Python
通常情况下，Ubuntu默认安装Python开发环境，如果没有安装，请使用：

    sudo apt-get install python

执行安装

## 配置数据库和服务器环境
Ubuntu可以使用集成的LAMP开发环境，使用如下命令获取最新版的`Apache`和`Mysql`：
    
    sudo apt-get install lamp-server
    sudo apt-get install python-mysqldb —— 数据库连接器
    
同时我们也推荐`MariaDB`和`PostgreSQL`这两种优秀的开源产品，以及MongoDB（暂未支持）作为未来的发展方向，我们并不提供服务器端详细配置方法，详情请参考各自的服务器手册

数据库配置文件存在于源码包的crm/settings.py文件中，请将DATABASE字典修改为您的环境配置参数

## 安装Django
请点击[这里][2]下载`Django1.6.2`安装包，执行解压和安装操作

    tar xzvf Django-1.6.2.tar.gz
    cd Django-1.6.2
    sudo python setup.py install

## 有经验的企业管理员
如果您是有技术经验的企业管理员，可以使用Python的专用包管理器`pip`来管理您的`SUES——CRM`，使用

    pip install django
    
安装`Django`并用

    which django-admin.py

测试安装的有效性，在Github上拉取最新的源码包

    git clone git@github.com:sanguo0023/sues_crm.git
    
## 同步数据模型
数据库转储文件在源码包的根目录下，名为`crm.sql`，通常情况下您不需要对此进行变动，如果您希望对数据库模型进行改动，请执行如下命令手动导出：
    
    python manage.py sqlall main > crm.sql

  [1]: https://github.com/sanguo0023/sues_crm
  [2]: https://www.djangoproject.com/download/1.6.2/tarball/

用户说明文档
============================

## 企业用户
### 对外公开信息平台
有需要展示的产品，或是公司的基本信息，我们开发了一个简单的静态CMS进行管理，如果需要图片展示，需要安装PIL及其依赖库，这里时间实在太仓促，就没有进行接下来的开发。

### 客户关系管理
能够读取已注册或管理员已导入的用户数据，形成一张Excel表格展示出来并导出表格文件

### 管理员入口
企业管理人员可以以管理员身份登入，建立职工用户组并且分配权限，以便工作人员进行信息录入操作

## 个人用户

### 初次登录
注册新的用户信息，填写：

 - 姓名
 - 固定电话（选填）
 - 移动电话（选填）
 - 邮件地址（选填）
 - 帐号
 - 密码

帐号作为用户的唯一标识，请妥善保管

### 产品展示

登录成功后，页面跳转到产品展示区
在这里可以提交订单，所有的订单将保存在后台数据库

### 公司简介

在这里展示公司的简介、宣传幻灯片和想法
让我们共同创造一个有气质的企业和产品信息平台

开发人员文档
============================

## 目录结构
    ├── crm
    │   ├── __init__.py
    │   ├── settings.py
    │   ├── templates
    │   │   ├── 404.html
    │   │   ├── base.html
    │   │   ├── crm.html
    │   │   ├── doc.html
    │   │   ├── index.html
    │   │   ├── info.html
    │   │   ├── login.html
    │   │   ├── register.html
    │   │   ├── show.html
    │   │   └── sns.html
    │   ├── urls.py
    │   └── wsgi.py
    ├── crm.sql
    ├── main
    │   ├── admin.py
    │   ├── forms.py
    │   ├── __init__.py
    │   ├── models.py
    │   ├── tests.py
    │   └── views.py
    ├── manage.py
    ├── requirements.txt
    ├── static
    │   ├── images
    │   │   ├── bg1.jpg
    │   │   ├── bg2.jpg
    │   │   ├── bg3.jpg
    │   │   ├── bg4.jpg
    │   │   └── bg5.jpg
    │   └── json
    │       └── info.json
    └── 商品信息0.csv


## 功能模块
目前的功能模块有：

 - 产品展示
 - 公司简介
 - 通讯录
 - 数据录入管理

如果没有接触过Django框架，着手修改会比较困难，开发组建议从一下几个角度进行开发：

 - 数据模型重定义
 - 表单模型和用户提交业务
 - 对现有的数据模型补充式开发

### 数据模型重定义

现有的数据模型定义是

     1. 物品信息表（名称，价格，描述，图片[未开启，需PIL支持]）
     2. 库存表（数量，关联1）
     3. 客户表（姓名，固定电话，移动电话，E-Mail，地址，帐号，密码）
     4. 操作员表（已废弃）
     5. 出库记录（数量，时间，关联1，关联4）
     6. 入库记录（数量，时间，关联1，关联4）
     7. 订单表（数量，关联3，关联1）
     
可以看出，时间仓促，且又是学习新的框架，对框架自有的用户验证体系不熟悉，数据模型表4成为了冗余的定义，课业较忙，一直到6月之前都暂时没有时间进行继续开发，只能先暂且搁置，请使用此项目的开发者自行重定义数据模型。

### 表单模型和用户提交业务
这个部分本来是有时间做的，但是开发对微博进行情感挖掘的部分消耗了接近三天的时间，算法和语料都有了，但是api的数据一直拉不下来，只好放弃，导致这个系列的功能也没有时间开发了，希望开发者能够注意这个部分的缺憾。

### 对现有的数据模型补充式开发
可以看到，这个数据模型中，有一部分表没有被使用，是设计的时候预留的ERP库存管理模块的表，需要注意的是，这个表的开发需要自建的数据模型与Django子框架的auth模型之间的用户体系对接，即同时关联表1和表3。

## 获取开发支持
    请发邮件至sues_crm@163.com

希望您开发愉快！
