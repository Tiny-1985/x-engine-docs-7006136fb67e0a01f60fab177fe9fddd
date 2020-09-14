讲 vue 源码的文章很多， 但一个沉淀了多年的框架，一上来就讲源码是不妥的。容易扯着蛋。 我想顺着以下思路弄。

1. 最简单的 mvvm
2. virtual DOM Vs. DOM
3. 最简单的 vue
4. 为何要组件化
5. patch 与 diff 的作用
6. 完整 vue

# 最简单的 mvvm

mvvm 在于双向绑定数据。 model -> view    view --> model 

## js 通知 html

对于 textnode: this.data => innerHTML  => html

对于 elementNode: this.data => element.value => html 等。

## demo

``` js
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <div id="app">
    {{name}} 
    <input id="input" v-model="name"></input></div>
</body>
  <script>
    var data ={
      name:"zk"
    }
    var _data ={
      ...data
    }

  var el = document.getElementById("input")
  // todo if v-mode attribute exist, then set the value with the value of v-mode
  input.value = _data.name

  var root = document.getElementById("app")

  var textNode = root.childNodes[0]
  var inputNode = root.childNodes[1]

  var reg = /\{\{(.*)\}\}/;
  var text = textNode.textContent;
  if(reg.test(text))
    {
      // extract the value from {{xxx}} 
      // set the value with  data.xxx
    textNode.textContent=_data.name
    }

  inputNode.addEventListener('input', function(e) {
  console.log(e.target.value)
  textNode.textContent=e.target.value
  })
  
  Object.defineProperty(data,'name',{
    set:function(val){
      console.log("haha.........")
      _data['name']=val;
      // todo notify all the listener who is interesting on 'name' changed
      textNode.textContent=_data.name
      input.value = _data.name
    }
  })
  </script>
</html>

```



在 console 里输入 

```
this.data.name='haha'
```

会发现双向数据已经支持了。



# virtual DOM Vs. DOM

virtual DOM 概念是一个又简单又难的东西。 

可见这篇文章， [网上都说操作真实 DOM 慢，但测试结果却比 React 更快，为什么？](https://www.zhihu.com/question/31809713/answer/53544875)



最出名的 vnode 库莫过于 https://github.com/snabbdom 了。 

里面的 vnode.js 就很直白了

```js
module.exports = function(sel, data, children, text, elm) {
  var key = data === undefined ? undefined : data.key;
  return {sel: sel, data: data, children: children,
          text: text, elm: elm, key: key};
};
```

将 DOM 里的 node 摘出些有用的东西。。就是 vnode。





