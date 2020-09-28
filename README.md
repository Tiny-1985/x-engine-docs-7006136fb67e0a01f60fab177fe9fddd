![cooltext363596337964428](assets/cooltext363596337964428.png)

# X-engine 简介

x-engine 是一个跨端模块管理框架，它的定位就是是客户端的 spring，管理 bean（模块）。

两个主要功能：

1. 多端模块管理。
2. 多端 api 与 DTO 的统一。

![image-20200929021827767](assets/image-20200929021827767.png)

x-engine 的目的并不是做“另一个跨平台”框架，

因为这样的框架太多了，从时间上，先是 cordova，到 react-native, 到 flutter。

总结下来就这几种模式：

native + web  : cordova

h5 -> native  : reactie-native  weex 

self-render   : flutter

native + web- : 小程序

除了 cordova 年久失修外，这些模式都有一个"特性", 绑定 UI 框架。这给某些已存在的 UI 技术栈的集成带来了一定的困难。 如果仅仅是尝尝鲜，那对他们的集成与扩展又会是一件非常麻烦的事。

基于 x-engine 的微应用（MicroApp）模块，则是为了解决这个问题而产生，x-engine 要能完整的应用开发，也必须有 UI 框架支持，但这套 UI 框架可以任你选择。比如， 使用 Taro。

如果你觉得 h5 性能不好，你甚至可以直接加入 react-native 模块， 将 Taro UI 打包成 react-native bundle 放在 x-engine 的 RN 模块里运行。



所以：

x-engine 并不会试图再去造一套 “小程序” DSL，而是利用独立模块的能力集合成一个支持小程序的产品--微应用，微应用全力拥抱 H5 / SPA 标准。 这也意味着 Vue，React，Angular 任何 H5 / SPA 的开发框架都可以是我们选型对象。 

x-engine 将会全面开源，包括核心源码。在出问题时，你能跟踪到任何一端直到不属于我们的源码。 





# 工程地址

引擎: [iOS](https://github.com/zkty-team/x-engine-module-engine/tree/master/iOS) [android](https://github.com/zkty-team/x-engine-module-engine/tree/master/android)

业务模板:[hybrid-tempalte](https://github.com/zkty-team/x-engine-hybrid-template)

组件模板:[module-template](https://github.com/zkty-team/x-engine-module-template)

# 项目管理

https://zktyfe.worktile.com/tasks/projects/5f164ffa478dbd1d67107712

