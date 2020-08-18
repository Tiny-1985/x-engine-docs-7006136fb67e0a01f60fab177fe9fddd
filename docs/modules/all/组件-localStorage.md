
**localStorage**

### 文档示例

- 以actionSheet为例

```json
{
  "modules":[
    {
      "module_id":"com.zkty.ui",
      "name":"UI",
      "tag": "1.0.0",
      "engine_version": "1.0.0",
      "minimal_os_version":{
        "ios": "11.1.0",
        "android_api": 20
    }  
  }
}

```



### showActionSheet

- 显示操作菜单

- 函数声明

  - ui.showActionSheet(Object)

  - Object参数说明

| 参数     | 类型         | 必填 | 默认值 | 说明                     |
| -------- | ------------ | ---- | ------ | ------------------------ |
| itemList | Arra<string> | 是   | ---    | 按钮的文字数组,最大长度6 |
| title    | string       | 否   | ---    | 提示的标题               |
| content  | string       | 否   | ---    | 提示的内容               |
| success  | function     | 否   | ---    | 接口成功的回调函数       |
| Fail     | function     | 否   | ---    | 接口失败的回调函数       |



- 示例

```javascript
xengine.ui.showActionSheet({ 
  title: 'title',
  content: 'content',
  itemList : ['测试1','测试2','测试3','测试4','测试5']
});
```


# h5


# iOS


# android


