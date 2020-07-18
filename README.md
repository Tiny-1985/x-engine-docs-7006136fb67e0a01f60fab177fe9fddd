## 概述

为适应需求的快速变化, 节省开发成本. 应用架构将主要分为两块, 引擎+业务.

引擎将服务于多个 app. 业务将针对特点项目而定制开发.

通用的技术功能将以逐步组件化下沉到引擎集成.

整体架构将基于 native + SPA(h5).

技术细节文档: 参看 [应用架构-技术细节.md](./%E5%BA%94%E7%94%A8%E6%9E%B6%E6%9E%84-%E6%8A%80%E6%9C%AF%E7%BB%86%E8%8A%82.md)

## 架构

 ![image-20200713230142933](././assets/75a77b34-5499-4a80-bd59-0350a72ee9e0.png)

## 产品

### 引擎标准模板

适合从 0 起项目, 不需要再自己配置工程.  直接按微应用文件规范写业务就行. 

通用组件已经集成到引擎, js 直接调用.

可选组件通过原生工程引包, 并且集成相应 js 即可调用.



### 引擎 SDK

适合已存在的原生项目, 将 xengine 集成到原生项目. 可以快速为客户提供类似微信小程序的能力.

有可能出现第三方包冲突的问题, 以引擎版本为准. 



### H5 标准模板

一套适合引擎的 h5 最佳开发实践.



## 版本管理

版本管理分为 3 个层次.

### 平台

根据 apple 和 google 走. 平台版本决定了引擎是否能够支持那些本地功能.

### 引擎

引擎版本决定了容器能够用到哪些平台接口.引擎版本与平台版本强相关.

### 微应用

与业务**紧密相关**, 通过在服务端的配置应用容器版本与应用的关系. 应用容器有可能涉及到容器间的共享

> 在服务端, 版本应该具有以下依赖约束.
> 
> 容器版本 -依赖-> 最低引擎版本 -依赖-> 最低平台版本
> 
> 在发布到应用市场时, 以 引擎版本+ app 标识 作为最终版本号.

## 引擎开发

### 核心机制

#### web 容器选型

*android 各平台 web 引擎差异太大, android 将统一基于 X5 web 引擎.*

*iOS 端将统一使用 WkWebview*

#### h5 与 native 交互

初期会使用 dsbridge 统一 iOS 和 android 的 js 与原生的交互. 

js <-> java / oc ,可同步, 可异步. 数据仅为简单数据的传递.

涉及到视频, 音频的处理. h5 不方便处理.

需要 js 层调用原生层的 view . 由原生层直接处理所有交互. 

### 

#### webview 离线渲染

离线渲染保证了平滑的页面切换, 达到与原生基本一样的体验. 

可根据不同性能的机型, 使用双缓冲渲染, 三缓冲渲染, 以及 池化 webview .

三者都支持无限制下一页.

|            | 原生动画 | 性能           | 历史页面状态保持                       | 无缝后退 | 无缝前进 |
| ---------- | -------- | -------------- | -------------------------------------- | -------- | -------- |
| 双缓冲     | 支持     | 很高           | 能通过 url 复现界面,仅中间状态无法保持 | 支持     | 不支持   |
| 三缓冲     | 支持     | 高             | 能通过 url 复现界面,仅中间状态无法保持 | 支持     | 支持     |
| 无限渲染池 | 支持     | 随页面层级而定 | 支持                                   | 支持     | 支持     |

双缓冲渲染:

![2 buffer](././assets/96d545a3-f590-4702-af05-81333fb828f2.gif)

三缓冲渲染: 

与双缓冲的区别在于, forward buffer 永远是空, 这样不会出现闪历史界面的问题.

![3webview-version 3](././assets/045e984e-7bab-4181-95d2-b031f8b7ce56.gif)

池化 webview 渲染池:

通用技术. 模拟线程池, 预加载 n 个, 根据需求自动收缩增长. 实现最简单, 效果最好, 唯一的缺点, 吃内存.



#### app 引擎更新

引擎更新只支持正常渠道发包更新. 无计划支持热更新.

#### 离线包更新

##### 离线包服务器部署

- 支持无逻辑部署, 也就是直接扔到资源服务器下即可.  
- 支持带逻辑部署
  - 将根据权限是否返回更新包
  - 支持灰度发布更新包



##### 客户端更新流程图

![image-20200709011208082](././assets/d65ed34b-9e53-447f-b5e3-72306496349a.png)



##### 微应用存储的位置

各平台表现不一, 假设可持久化存储位置为 X

{X}/microApps/{microAppId}/{version}/index.html

{X}/microApps/{microAppId}/{version}/icon.png

{X}/microApps/{microAppId}/{version}/...



microApps 做为一个统一的 microApp 入口.

```
- {X}
	- microApps
		-	com.zkty.xiaoqu.opendoor.1
				- index.html
				- icon.png
		- com.zkty.xiaoqu.opendoor.2
				- index.html
				- icon.png
		-	com.zkty.xiaoqu.shequ.1
				- index.html
				- icon.png
```







##### zip 离线包格式



```
- {microAppId}.{version}.zip
	- {microAppId}.{version}
    - index.html
    - icon.png   // 128*128
    - ...
```

举例:

``` json
- com.zkty.xiaoqu.opendoor.1.zip
	- com.zkty.xiaoqu.opendoor.1
    - index.html
    - icon.png
    - ...
```

> 之所以要多一层, 用户测试与压缩方便,  直接将离线包的文件夹压缩即可.
>
> 客户端解压也方便, 不同的解压库有时在解压单个文件与多个文件时, 表现不一, 代码好改, 但不方便日后升级.
> 但当包内是文件夹时, 基本都是统一的解压.



##### version 定义

version = microApp 所有 version的数字之和. 

当本地 version 不能从配置文件读取到时, 客户端应该根据初始打包的微应用自己算出来.

##### 引擎应用配置

xengine_config.json:

``` json
{
  "appId": "com.zkty.xiaoqu",    // 建议直接设置为应用的 Bundle Identifier
  "appSecret": "8b387ca3ebdd412e9c97ef81ed352ee7",  //随机 md5 值.
  "offlineServerUrl": "https://3rd-public-file.oss-cn-beijing.aliyuncs.com"  //服务器地址
}
```

 

##### app 微应用集合地址

请求地址:

GET: {offlineServerUrl}/app/{appId}/microApps.json?key=md5(appSecret+appId)&version=12



```
key 由  md5 算出. 
key = md5(appSecret+appId)
```





返回:

有新版本

http status: 200

microApps.json:

``` json
{
  "code":0,
  "version":3,     // microApps.json 版本标识
  "forceUpdate" true,  // 是否强制更新
  "data":
        [
          {
            "microAppName":"开门",
            "microAppId":"com.zkty.xiaoqu.opendoor",
            "microAppVersion":2
          },
          {
            "microAppName":"物业",
            "microAppId":"com.zkty.xiaoqu.realstate"
            "microAppVersion":1
          }
        ]
  }
```



没新版本:

http status: 200

``` json
{
  "code":304,
  "version":1,
 
  }
```

 

> microApps.json 应该持久化在手机应用本地. 用来对比. 
>
> 如果不持久化到本地, 那就需要扫描本地 microApps 来对比是否需要更新版本.



打开微应用

```
xEngine.showMicroApp({microAppId},{version},{args},{microAppName})
```



##### 微应用 zip 下载地址

GET: {offlineServerUrl}/app/{appId}/{microAppId}.{version}.zip?key=md5(appSecret+microAppId+version)&engine_build=1

返回: zip 包

示例:

http://192.168.3.129:8000/app/com.zkty.xiaoqu/com.zkty.xiaoqu.opendoor.1.zip?key=1f2414c23a7d55dddc11caa32a8e9a4a&engine_build=1

 

engine_build 为引擎 build 号. 由引擎 sdk 暴露获取方法. engine_build 为一个数字.





##### 更新是否影响应用上架

应用市场为了防止开发者不经市场审核许可，给用户提供违法内容，对热更新大多持排斥态度。

但实际上热更新使用非常普遍，不管是原生开发中还是跨平台开发。

使用热更新需要注意：

- 上架审核期间不要弹出热更新提示
- 热更新内容使用https下载，避免被三方网络劫持
- 不要更新违法内容、不要通过热更新破坏应用市场的利益，比如iOS的虚拟支付要老老实实给Apple分钱

如果你的应用没有犯这些错误，应用市场是不会管的。





#### 统一 header

header 用原生的做,这样, 可以一定程度上提高用户体验, 如果页面无响应, 用户可以返回. 不至于只能杀死进程.

需要改进 vue 里的路由. 在 js / vue 里路由跳转界面时. 通知原生层. 创建新 web 引擎.

注意: 新的路由地址必须唯一.



![2020-07-13 22.34.15](././assets/c7be7afb-5977-4051-a7fb-723bc3c9eb27.gif)

#### 统一网络

网络是除缓存外最核心的一块功能. 

需要将 h5 的网络统一由 native 做一层代理, 来解决 cookie 共享, 安全, 跨域, 缓存, 路由等问题.

浏览器本身自带的网络请求功能, 只做加载第三方链接的标签资源用. 要达到如微信小程序的感觉, 可直接屏蔽.

其他请求全必须走本地网络.

方案会基于异步封装 native 网络请求.



![image-20200615183020656](././assets/d1bea368-81fb-4ef3-b069-5695c2a61fc9.png)

#### 白名单

本地网络出口要设白名单， 防止xss。

白名单配置在服务器上。在下载离线包时，读入配置。

配置做签名，防止篡改。



### xengine.api

JS API 将抹平 ios 与 android 等其他平台的调用差异. 

主要包含路由, 网络,存储, 硬件调用, 等.



* API约束（包括调用格式，传参格式，回调格式）
* 功能规划（约定这个框架应该提供什么样的功能）
* 权限校验（校验后才能调用，包括权限校验的代码格式，校验一些什么内容，以及哪些API无需校验）
* 模块化的API（按照模块划分，每一个模块可以作为单独的组件，便于拓展）
* 其它优化（如在PC端调试API的页面，部分API支持Promise等）

#### API 约束

约定所有API统一采用如下调用方式

``` js
xengine.模块名.方法({
    参数1: "",
    参数2: "",
    success: fucntion(result) {
        // 成功回调
    },
    error: fucntion(error) {
        // 失败回调
    }
});
// 或者使用 promise 
xengine.模块名.方法({
    参数1: "",
    参数2: "")
.then(result=>{})
.catch(error=>{})

```

**约束说明**

* 所有接口都为异步调用
* 接收一个`object`类型的参数
* 成功回调`success`
  * 通过`result`获取成功数据
  * 回调函数的触发时机由具体的API决定，有的API是调用时即可回调（短期），有的是某个事件触发后才被回调（长期）
* 失败回调`error`，所有的API调用错误都会走失败回调



> promise 一样.



#### 功能规划

``` js
xengine   
		|- net
		|   |- request  post get put head
    |   |- fileupload  
		|- ui               // 系统ui组件
    |   |- toast
    |   |- alert
    |   |- confirm
    |   |- prompt
    |   |- showWaiting
    |   |- closeWaiting
    |   |- actionSheet
    |   |- pickDate
    |   |- pickTime
    |   |- pickDateTime
    |   |- popWindow
    |- page             // 页面（webview）管理
    |   |- open
    |   |- openLocal
    |   |- close
    |   |- reload
    |- navigator        // 导航栏控制
    |   |- setTitle
    |   |- setMultiTitle
    |   |- hookSysBack
    |   |- hookBackBtn
    |   |- setRightBtn
    |   |- setLeftBtn
    |   |- setRightMenu
    |- auth             // 权限认证相关
    |   |- getToken
    |- device           // 设备相关
    |   |- setOrientation
    |   |- getDeviceId
    |   |- getNetWorkInfo
    |   |- getVendorInfo
    |   |- closeInputKeyboard
    |   |- vibrate
    |   |- callPhone
    |   |- sendMsg
    |- runtime          // 运行环境
    |   |- launchApp
    |   |- getAppVersion
    |   |- getxengineVersion
    |   |- getGeolocation
    |   |- clearCache
    |   |- clipboard
    |   |- openUrl
    |- util             // 其它工具
    |   |- scan
    |   |- selectImage
    |   |- cameraImage
    |   |- selectFile
    |   |- openFile
```



> 详情见日后 xengine.api 文档.md.

#### 权限校验(可选)

根据不同需求，可以划分以下等级。

* 平台级别的（像钉钉、微信这类对外开放的），需要配合后台，有完整的授权，签名，校验机制
* 项目级别的（N个项目同一个框架，但业务各不相同），简单的应用内部配置，直接校验一些域名白名单信息即可

``` js
xengine.error(function(error) {
    // 全局错误处理
});

xengine.config({
    ...
});
xengine.ready(function() {
    // TODO: 处理验证成功后的事情，例如调用api
});
```

如果`config`失败或者没有校验，那么敏感API都无法调用

**无需校验就可用的API**

并不是所有API都需校验后才能用，我们约定以下API默认就可用（这里是一个粗糙的划分，实际上可以精确到每一个API）

``` js
ui模块的所有API
page模块的所有API
navigator模块的所有API
```



####  模块化

有一个全局变量`xengine`，但API并不是直接绑定在全局变量下，而是按模块划分，譬如

``` js
xengine.ui
xengine.device
xengine.page
...
```



**组件API的拓展机制**

默认情况下，框架会注册以下组件

``` js
ui
page
navigator
auth
device
runtime
util
```

但是假设某项目中突然遇到了一个需求，要新增一个支付功能，并且要以API的形式提供给H5页面调用，该如何实现呢？

各个项目可以拓展自己的组件,如下

``` js
// 1.前端config时，传入需要注册的组件别名
xengine.config({
   user_modules: ['pay', 'speech']
});
// 2.原生框架中，接收到config后，基于传入的别名，去对应项目配置文件中查询路径，然后将对应路径的API实现类注册
// 对应的组件的API实现类不是放框架中的，而是由各自的项目管理的，到时候框架就是一个固定的库，给各个项目引用
// 3.前端中，通过一个固定的方法，调用刚注册的组件API中的功能
xengine.callApi({
    funcName: 'xxx',
    muduleName: 'pay',
    ...
    data: {},
    success: function(result) {},
    error: function(error) {},
});
```

通过这一套机制，可以保持框架的可拓展性，就算应用不同的项目中，N多的功能，也能通过这种方法拓展，保持一致的使用

如果组件已完善, 可以将组件合并归类到正式引擎模块. 调用方法改为

```
xengine.<muduleName>.<funcName>
```



### 组件

组件的主要作用就是提供 h5 到本地的 adapter. 组件的加载主要有两种方案.

* 通用组件:直接集成到应用引擎.直接集成到应用引擎从开发速度与稳定性来讲, 都是最优.
* 可选组件:动态加载, 主要解决的问题是, 引擎打包后过于膨胀.
二进制的更新在 android 上有非常成熟的解决方案. 而 ios 相对来说都是些厂商的黑科技. 开源的已全被封了. 如jspatch, rollout.io

*在引擎 1.0 阶段. 组件将会直接集成到引擎一起发布.*

 

> 组件详细文档见组件 1.0 规范文档. *重点是统一 android 与 iOS 的接口。*

#### 基本组件

* toast
* 消息推送
* 统计埋点
* 统一存储与读取
* 调用摄像头 / 相册
* 社交分享
* 定位
* 设备标识

参考 dcloud apicloud https://www.html5plus.org/doc

#### 权限申请

iOS: 按本地应用申请即可.

android: https://developer.android.google.cn/training/permissions/usage-notes#dont-overwhelm

权限询问的时机:

|  | CRITICAL | CRITICAL |  |
| --- | -------- | -------- | --- |
| UNCLEAR | 启动时,告诉用户为什么需要,弹出 | 启动时,直接弹出 | CLEAR |
| UNCLEAR | 在使用时,告诉用户为什么需要,弹出 | 在使用时,直接弹出 | CLEAR |
|  | NON-CRITICAL | NON-CRITICAL |  |

#### 测试与运维

##### 兼容性测试

使用岩鼠平台(付费): https://yanshu.effirst.com/product/real-devices/overview

可在引擎 ship 前,对市面上的常用机型做兼容性测试.

##### 性能测试

dokit http://xingyun.xiaojukeji.com/docs/dokit/#/intro

xcode 自带 instrument

* 重点: 内存加载

#### 线上错误日志管理

native 错误可以使用市面上成熟的方案,如 bugly, 友盟.

h5 相关错误. 可使用 sentry 自行搭建. 也可使用成熟方案(未研究).

### 引擎 1.0 产品方向

* [x] 统一 header。
* [x] 统一网络。
    * [ ] 网络白名单。
* [x] 基于离线包。
    * [ ] 差分包。
* [ ] 组件标准。
    * [ ] android /iOS / h5
* [ ] 组件文档 - docsify。
* [ ] 业务模板 h5 标准范式。

### 引擎 2.0 产品方向

* 支持发布 web 版.
* 组件模块动态化. (可选)
* 提升安全性

android virtualAPK: https://didi.github.io/virtual-apk.html

## 业务开发

### h5 工程化

可参考: [mobile-web-best-practice](https://github.com/mcuking/mobile-web-best-practice) , 形成开发标准模板, 与开发规范.

### h5 UI 组件

h5 UI 组件可使用现在已存任何移动前端库. 

比如 [cube-ui](https://didi.github.io/cube-ui/#/zh-CN/docs/create-api) ,[mand-mobile](https://didi.github.io/mand-mobile/), 等, 并无要求.

![image-20200622120457790](././assets/46aa07da-53a6-4a41-a716-78c438030b29.png)

*但基于任何 UI 库都必须做几件事：*

1. *加载 dsbridge， fly.js*
2. *注册需要使用的原生接口。*



### 调试

#### h5

业务代码, 可直接使用 chrome 调度试.

#### native + h5

* 可以打开 safri 选择相应 device. 会 attach 到对应的 web 引擎渲染的内容.

![image-20200614172828808](././assets/8acd51d8-b061-4ab1-b3ac-2fbcec9f60ba.png)



### 实时加载

任何可以实时加载 http 的工具都支持.比如利用 [livehttp](https://github.com/zk4/livehttp)

![13.30.36.gif](././assets/1684a4ea-d67f-43d6-917b-a4e9cade97a6.gif)





## 同类产品

区别: dcloud 不开源, 但组件丰富.

https://nativesupport.dcloud.net.cn/README

h5+

http://rayproject.applinzi.com/doc.web.crossPlatformGroup/html/frameworkDoc/index.html#page=doc_frameworkDoc_simple_webviewOptimized