

# 原生导航

header 用原生的做,这样, 可以一定程度上提高用户体验, 如果页面无响应, 用户可以返回. 不至于只能杀死进程.

注意: 新的路由地址必须唯一.




![2020-07-13 22.34.15](assets/c7be7afb-5977-4051-a7fb-723bc3c9eb27.gif ':size=20%')

 


# api

## setNavTitle

- 设置导航栏中间名称

- 函数声明
  
  - nav.setNavTitle(Object)
  

**Object参数说明**	

|    参数    |  类型  | 必填 | 默认值  |       说明       |
| :--------: | :----: | :--: | :-----: | :--------------: |
|   title    | String |  是  |   ---   |   导航条的文字   |
| titleColor | String |  否  | #000000 | 16进制的颜色色值 |
| titleSize  | Number |  否  |   16    | 导航条文字的大小 |

**示例**	

```javascript
xengine.nav.setNavTitle({
  title:'导航条',
  titleColor : "#000000",
  titleSize  : 16
});
```



## setNavLeftBtn

- 设置导航条左边按钮
- 函数声明
  - nav.setNavLeftBtn(Object)



**Object参数说明**	

|    参数    |     类型      | 必填 |  默认值  |         说明         |
| :--------: | :-----------: | :--: | :------: | :------------------: |
|   title    |    String     |  是  |   ---    | 导航条右边按钮的文字 |
| titleColor |    String     |  否  | #000000  |   16进制的颜色色值   |
| titleSize  |    Number     |  否  |    16    |   导航条文字的大小   |
|    icon    |    String     |  是  |          |      见下方说明      |
|  iconSize  | Array<number> |  否  | [20, 20] |      图片的宽高      |

**warning:**

- title和icon必须选择一种存在, 效果为纯文字和纯图片的展示。
- Object中如果同时存在title和icon会默认显示文字。



**icon ** 

- 图片可分为2种传入方式

  - 本地图片:
    -  icon: /assets/图片名称.png
  - 网络图片: 
    - icon: 'https://图片地址'

**示例**

```javascript
xengine.nav.setNavLeftBtn({
	title: '右边按钮'
});

xengine.nav.setNavLeftBtn({
	icon:'https://图片地址'
});

xengine.nav.setNavLeftBtn({
	icon:'/assets/图片名称
});
```



## handleNavLeftBtn


- 点击导航条左上角按钮
- 函数声明
  - nav.handleNavRightBtn()

**示例**

```javascript
xengine.nav.handleNavLeftBtn({
  success:(res) => {
    // 业务逻辑
  },
  fail:(error) => {
    console.log(error) 
  }  
});
```



## setNavRightBtn

- 设置导航条右边按钮
- 函数声明
  - nav.setNavRightBtn(Object)



**Object参数说明**	

|    参数    |     类型      | 必填 |  默认值  |         说明         |
| :--------: | :-----------: | :--: | :------: | :------------------: |
|   title    |    String     |  是  |   ---    | 导航条右边按钮的文字 |
| titleColor |    String     |  否  | #000000  |   16进制的颜色色值   |
| titleSize  |    Number     |  否  |    16    |   导航条文字的大小   |
|    icon    |    String     |  是  |          |      见下方说明      |
|  iconSize  | Array<number> |  否  | [20, 20] |      图片的宽高      |

**warning:**

- title和icon必须选择一种存在, 效果为纯文字和纯图片的展示。
- Object中如果同时存在title和icon会默认显示文字。



**icon ** 

- 图片可分为2种传入方式

  - 本地图片:
    -  icon: /assets/图片名称.png
  - 网络图片: 
    - icon: 'https://图片地址'

**示例**

```javascript
xengine.nav.setNavRightBtn({
	title: '右边按钮'
});

xengine.nav.setNavRightBtn({
	icon:'https://图片地址'
});

xengine.nav.setNavRightBtn({
	icon:'/assets/图片名称
});
```



## handleNavRightBtn

- 点击导航条右上角按钮
- 函数声明
  - nav.handleNavRightBtn()

**示例**

```javascript
xengine.nav.handleNavRightBtn({
  success:(res) => {
    // 业务逻辑
  },
  fail:(error) => {
    console.log(error) 
  }  
});
```





## setNavRightMenuBtn

- 设置导航条右边菜单按钮
- 函数声明
  - nav.setNavRightBtn(Object)



**Object参数说明**	


|    参数     |     类型      | 必填 |  默认值  |         说明         |
| :---------: | :-----------: | :--: | :------: | :------------------: |
|    title    |    String     |  是  |   ---    | 导航条右边按钮的文字 |
| titleColor  |    String     |  否  | #000000  |   16进制的颜色色值   |
|  titleSize  |    Number     |  否  |    16    |   导航条文字的大小   |
|    icon     |    String     |  是  |    -     |      见下方说明      |
|  iconSize   | Array(number) |  否  | [20, 20] |      图片的宽高      |
|  itemList   | Array(Object) |  是  |    -     |   下拉列表中的内容   |
| showMenuImg |    Stirng     |  否  |  false   |      见下方说明      |
|  menuWidth  |    String     |  否  |   100    |       menu的宽       |

**warning:**

- title和icon必须选择一种存在, 效果为纯文字和纯图片的展示。
- Object中如果同时存在title和icon会默认显示文字。



**icon**

- 图片可分为2种传入方式

  - 本地图片:
    -  icon: /assets/图片名称.png
  - 网络图片: 
    - icon: 网络图片地址 cdn / 服务器 / 随你



showMenuImg

- 下拉列表内部样式
  - true: 显示图片+文字
  - false: 显示文字 (默认值)

**示例**

```javascript
xengine.nav.setNavRightMenuBtn({
  title:'menu',
  showMenuImg: 'true',
  itemList:[
    {title:'A',icon:'/assets/图片名称.png'},
    {title:'B',icon:'/assets/图片名称.png'},
    {title:'C',icon:'/assets/图片名称.png'},
    {title:'D',icon:'/assets/图片名称.png'},
    {title:'E',icon:'/assets/图片名称.png'},
  ]
});
```



## handleNavRightMenuBtn

- 点击导航条右上角menu按钮
- 函数声明
  - nav.handleNavRightMenuBtn()

**示例**

```javascript
xengine.nav.handleNavRightMenuBtn({
  success:(res) => {
    alert(res);
  },
  fail:(error) => {
    alert('error', error); 
  }
})
```



## setNavRightMoreBtn

- 设置导航条右边多个按钮
- 函数声明
  - nav.setNavRightMoreBtn(Object)



**Object参数说明**	


|    参数    |     类型      | 必填 |  默认值  |         说明         |
| :--------: | :-----------: | :--: | :------: | :------------------: |
|   title    |    String     |  是  |   ---    | 导航条右边按钮的文字 |
| titleColor |    String     |  否  | #000000  |   16进制的颜色色值   |
| titleSize  |    Number     |  否  |    16    |   导航条文字的大小   |
|    icon    |    String     |  是  |    -     |      见下方说明      |
|  iconSize  | Array(number) |  否  | [20, 20] |      图片的宽高      |

**warning:**

- title和icon必须选择一种存在, 效果为纯文字和纯图片的展示。
- Object中如果同时存在title和icon会默认显示文字。



**icon**

- 图片可分为2种传入方式

  - 本地图片:
    -  icon: /assets/图片名称.png
  - 网络图片: 
    - icon: 网络图片地址 cdn / 服务器 / 随你

**示例**

```javascript
xengine.nav.setNavRightMoreBtn([
  {
    title: 'A', icon: '/assets/search.png', iconSize: [20, 20]
  },
  {
    title: 'B', icon: '/assets/search.png', iconSize: [20, 20]
  }
]);
```



## handleNavRightMoreBtn

- 点击导航条右边多个按钮
- 函数声明
  - nav.handleNavRightMoreBtn()

**示例**

```javascript
xengine.nav.handleNavRightMoreBtn({
  success: (res) => {
    alert(res);
  },
  fail: (error) => {
    alert('error', error); 
  }  
});
```



## navigatorPush

- 通过原生导航进行下一页的跳转
- 函数声明
  - nav.navigatorPush(Object)

**Object参数说明**	

| 参数 |  类型  | 必填 | 默认值 |    说明    |
| :--: | :----: | :--: | :----: | :--------: |
| url  | String |  是  |  ---   | 见下方说明 |



**url参数说明**

- 以testA.vue为例.

-  需要传入的url的值为 `/`  +  `页面的名称`。 既: `/testA` 
- iOS / Android会去对应的微应用包的包中查找传入的文件名称放在下一页展示。
- 注意不能加`.vue`后缀



**示例**

```javascript
xengine.nav.navigatorPush({
  url: "/testB",
});
```




## navigatorBack

- 通过原生导航页面的返回
- 函数声明
  - nav.navigatorBack(Object)

**Object参数说明**	

| 参数 |  类型  | 必填 | 默认值 |    说明    |
| :--: | :----: | :--: | :----: | :--------: |
| path | String |  是  |  ---   | 见下方示例 |



**示例**

```javascript
// 返回上级页面
xengine.nav.navigatorBack();

// 返回微应用第一级页面
xengine.nav.navigatorBack({
	path: "/index",
});

// 返回iOS/Android根控制器页面
xengine.nav.navigatorBack({
   path: "0",
});
```



## setNavSearchBar

- 设置导航条搜索框
- 函数声明
  - xengine.nav.setNavSearchBar(Object)

**Object参数说明**	


|        参数         |     类型      | 必填 | 默认值 |          说明          |
| :-----------------: | :-----------: | :--: | :----: | :--------------------: |
|    searchBarSize    | Array(number) |  是  |  ---   |       搜索框大小       |
|    cornerRadius     |    Number     |  否  |  ---   |     搜索框圆角大小     |
|   backgroundColor   |    String     |  否  |  ---   |     搜索框背景颜色     |
|     iconSearch      |    String     |  否  |  ---   |    搜索框里搜索图片    |
|   iconSearchSize    | Array(number) |  否  |  ---   |  搜索框里搜索图片大小  |
|      iconClear      |    String     |  否  |  ---   |    搜索框里清空图片    |
|    iconClearSize    | Array(number) |  否  |  ---   |  搜索框里清空图片大小  |
|      textColor      |    String     |  否  |  ---   |     搜索框文本颜色     |
|      fontSize       |    Number     |  否  |  ---   |   搜索框文本字体大小   |
|     placeHolder     |    String     |  否  |  ---   |      搜索框占位符      |
| placeHolderFontSize |    Number     |  否  |  ---   |    搜索框占位符大小    |
|       isInput       |     Bool      |  否  |  true  | 搜索框是否添加点击事件 |

**isInput:**

- isInput默认为true。
- 当isInput传false时，表示搜索框添加点击响应方法handlerNavSearchBar（见下面）
- 当isInput传true时，表示搜索框不添加点击响应方法handlerNavSearchBar。

**iconSearch**

- 图片可分为2种传入方式

  - 本地图片:
    -  icon: /assets/图片名称.png
  - 网络图片: 
    - icon: 网络图片地址 cdn / 服务器 / 随你

**iconClear**

- 图片可分为2种传入方式

  - 本地图片:
    -  icon: /assets/图片名称.png
  - 网络图片: 
    - icon: 网络图片地址 cdn / 服务器 / 随你

**示例**

```javascript
xengine.nav.setNavSearchBar({               
  searchBarSize: [100, 30],              
  cornerRadius: 5,                
  backgroundColor: '#FFFF00',                
  iconSearch: '/assets/search.png',               
  iconSearchSize: [20, 20],              
  iconClear: '/assets/xxx.png',             
  iconClearSize: [15, 15],               
  textColor: '#FFA500',               
  fontSize: 13,               
  placeHolder: '请输入',               
  placeHolderFontSize: 12,              
  isInput: true          
});
```



## handlerNavSearchBar

- 点击搜索框响应事件(当setNavSearchBar里'isInput'参数传入'True'时)
- 函数声明
  - xengine.nav.handlerNavSearchBar()

**示例**

```javascript
xengine.nav.handlerNavSearchBar({
  success: (res) => {
    //业务逻辑
  },
  fail: (error) => {
    console.log('error', error); 
  }  
});
```



# iOS


# android
ODO


