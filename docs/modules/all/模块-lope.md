


 
gradle read version from config file 
https://stackoverflow.com/questions/47492210/react-native-automatic-version-name-from-package-json-to-android-build-manifes
``` groovy 
// On top of your file import a JSON parser
import groovy.json.JsonSlurper

// Create an easy to use function
def getVersionFromNpm() {
    //  Read and parse package.json file from project root
    def inputFile = new File("$rootDir/../package.json")
    def packageJson = new JsonSlurper().parseText(inputFile.text)

    // Return the version, you can get any value this way
    return packageJson["version"]
}

android {
    defaultConfig {
        applicationId "your.app.id"
        versionName getVersionFromNpm()
    }
}
```

pod  config file 
https://stackoverflow.com/questions/21405457/autoincrement-versioncode-with-gradle-extra-properties


# api


`
com.zkty.module.lope
`



## customOpenDoor

 function openDoor(){
     window.openDoor = (...args) => {
     lope
       .openDoor(...args)
       .then((res) => {
         document.getElementById("debug_text").innerText = "ret:"+res;
       });
   };
 }

	
**无参数**




## lightLift



	
**无参数**




## haveArgRetPrimitive

 have args ret primitive

	
**参数说明**

| name                        | type      | optional | default   | comment  |
| --------------------------- | --------- | -------- | --------- |--------- |
| title | string |  | "abc" |  标题 |
| itemList | Array\<string\> | true |  |  子标题? |
| content | string | true |  |  内容 |
| __event__ |  |  |  |  点击子标题回调函数 |


## openDoor

 have args ret Object

	
**参数说明**

| name                        | type      | optional | default   | comment  |
| --------------------------- | --------- | -------- | --------- |--------- |
| title | string |  | "abc" |  标题 |
| itemList | Array\<string\> | true |  |  子标题? |
| content | string | true |  |  内容 |
| __event__ |  |  |  |  点击子标题回调函数 |

    

# iOS
介绍在引入模块时,iOS 方面要做的事.如工程权限配置等.

```
pod install x-engine-module-lope
```


# android
介绍在引入模块时,android 方面要做的事.如工程权限配置等.

gradle
```
implementation x-engine-module-lope
```


