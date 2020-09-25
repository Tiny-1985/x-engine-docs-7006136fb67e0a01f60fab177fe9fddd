

x-engine 理论上只负责管理模块， 但因为当前业务需求，我们提供了一些具体功能。比如支持类似小程序的 MicroApp。

## 架构图



![image-20200925134159522](assets/image-20200925134159522.png)





## 组件化

组件分为[通用组件](./docs/modules/组件-规范.md#组件分类),与[可选组件](./docs/modules/组件-规范.md#组件分类)

通用组件示例:[引擎](./docs/modules/common/组件-引擎.md)  [统一网络](./docs/modules/common/组件-统一网络.md)  [原生导航](./docs/modules/common/组件-原生导航.md) ...

可选组件示例: [蓝牙](./docs/modules/optional/组件-蓝牙.md)  ...

通用组件与可选组件并没有本质差别， 只是通用组件会集成到 hybrid-template  中， 官方保证了组件间的兼容性。 

引擎本身就有有可能会依赖某些组件，如 network， 被依赖的组件会以接口的形式被引用，用户如果需要自定义自己的 network 组件，则必须实现相应的接口，在 iOS 里表现为 protocol 接口，在 android 里则是 interface接口， 接口定义在引擎里。

这样做的原因是： 

当引擎所依赖的组件与用户组件相冲突时， 用户可以替换引擎组件，又不影响引擎的功能。

![image-20200810124830254](assets/image-20200810124830254.png)



## 离线机制
见 [离线包](./docs/microApp/微应用-离线服务器.md)

