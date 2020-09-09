

# todo 
generate api markdown
# 需知
1. git pull 最新 x-engine-module-engine
1. npm update @zk4/xengine

#  安装
```
make install
```

# 使用
```
x-cli model.ts
```

# 模型
在 x-engine-module-template 下有示例,  model.ts 都应该放在相应路径
```
# 命名空间
const moduleID = "com.zkty.module.xxxx";

# dto
interface SheetDTO {
    title: string;
    itemList?: Array<Map<string,string>>;
    content?: string;
}
  
# 函数定义与默认参数
function showActionSheet(sheetDTO:SheetDTO={title:"title",itemList:["a","b","c"],content:"content"}){

# 测试方法
window.showActionSheet=()=>{
  xxxx.showActionSheet(
  )
  .then(res=>{
    document.getElementById("debug_text").innerText= res;
  })
}

window.showActionSheet()

}

```
# reference
https://github.com/microsoft/TypeScript/wiki/Using-the-Compiler-API

support mutli language AST
https://astexplorer.net/

https://ts-morph.com/details/classes



# api



# iOS


# android


