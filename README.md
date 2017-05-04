# 运维自动化平台

#### 部分目录结构说明
```python
OpsAutomationPlatform/      # 程序主目录
├── cmdb                        # 资产管理
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── models.py               # 关于资产的一堆表
│   ├── templatetags
│   │   ├── cmdb_asset.py
│   │   └── __init__.py
│   ├── tests.py
│   ├── urls.py
│   ├── views_func
│   │   └── asset.py
│   └── views.py
├── db.sqlite3
├── index                       # 主页(登录,运维平台首页)
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── models.py               # 包含用户和用户组两张表
│   ├── tests.py
│   └── views.py
├── manage.py
├── OpsAutomationPlatform
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── README.md
├── statics
│   ├── css
│   ├── imgs
│   ├── js
│   │   └── cmdb
│   └── plugins
│       ├── bootstrap
│       │   ├── css
│       │   ├── fonts
│       │   └── js
│       ├── font-awesome
│       │   ├── css
│       │   ├── fonts
│       │   ├── less
│       │   └── scss
│       └── sb-admin
│           ├── css
│           └── js
└── templates
    ├── cmdb                    # cmdb中用到的模板
    │   ├── asset.html
    │   ├── asset_select.html
    │   ├── include
    │   │   └── page_temp.html
    │   └── index.html
    ├── include                   # 可以被嵌套的模板
    │   ├── asset_basic.html
    │   ├── asset_log.html
    │   ├── asset_network_hardware.html
    │   ├── asset_server_hardware.html
    │   ├── header.html
    │   └── header_menu.html
    └── index                      # 主页和登录页模板
        ├── index.html
        └── login.html

```

#### 页面展示
- 登录页
![](https://github.com/crazy-zhangcong/OpsAutomationPlatform/blob/master/images/login.png)

- 运维平台首页
![](https://github.com/crazy-zhangcong/OpsAutomationPlatform/blob/master/images/index.png)

- 资产管理-资产展示页面
![](https://github.com/crazy-zhangcong/OpsAutomationPlatform/blob/master/images/cmdb_asset.png)