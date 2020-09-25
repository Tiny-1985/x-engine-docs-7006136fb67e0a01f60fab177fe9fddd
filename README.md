![cooltext363596337964428](assets/cooltext363596337964428.png)

# X-engine 简介

x-engine 是一个跨端应用框架，它的定位就是是客户端的 spring，管理 bean（模块）。并实现模块的自动发现，注入。以及生命周期。

x-engine 的目的并不是做“另一个跨平台”框架，因为这样的框架做的不错的太多了，如 flutter，react-native ，weex。 但这些框架都有一个"特性", 绑定 UI 框架。业务上为了追求性能，为了追求能发多端，这是可以理解的。 

而 x-engine 要能完整的应用开发，当然也必须有 UI 框架， 这套 UI 框架任你选择， 比如 Taro，那你的 UI 定位就是 react 栈，且支持发布小程序，h5， react-native。

x-engine 的目标就是怎么高效的原生模块化管理，开发，与维护。 打造一套拿来即用的企业级开源方案。



其中的许多 hybrid 方案中耳熟能详的功能都以官方的模块存在。

- 支持微应用，支持以任何前端框架开发微应用
- 支持业务热更新
- 支持原生网络代理
- 。。

你也可以非常快速的自定义模块，比如将 react-native，weex 作为模块引入。这样你就拥有了 react-native 所有的能力。



所以：

x-engine 并不会试图再去造一套 “小程序” DSL，而是全力拥抱 H5 / SPA 标准。 这也意味着 Vue，React，Angular 任何 H5 / SPA 的开发框架都是我们服务对象。 

x-engine 也可以支持小程序, 比如你的微应用使用 taro 编写。则可以直接输出到小程序。h5 输出到应用使用。

x-engine 将会全面开源，包括核心源码。在出问题时，你能跟踪到任何一端直到不属于我们的源码。 

 



# 工程地址

引擎: [iOS](https://github.com/zkty-team/x-engine-module-engine/tree/master/iOS) [android](https://github.com/zkty-team/x-engine-module-engine/tree/master/android)

业务模板:[hybrid-tempalte](https://github.com/zkty-team/x-engine-hybrid-template)

组件模板:[module-template](https://github.com/zkty-team/x-engine-module-template)

# 项目管理

https://zktyfe.worktile.com/tasks/projects/5f164ffa478dbd1d67107712

