


 
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
com.zkty.module.dcloud
`



## openUniMP

 启动小程序

	
**参数说明**

| name                        | type      | optional | default   | comment  |
| --------------------------- | --------- | -------- | --------- |--------- |
| appId | string |  | "__UNI__11E9B73" |  |


## preloadUniMP

 预加载后打开小程序

	
**参数说明**

| name                        | type      | optional | default   | comment  |
| --------------------------- | --------- | -------- | --------- |--------- |
| appId | string |  | "__UNI__11E9B73" |  |


## openUniMPWithArg



	
**参数说明**

| name                        | type      | optional | default   | comment  |
| --------------------------- | --------- | -------- | --------- |--------- |
| appId | string |  | "__UNI__11E9B73" |  |
| arguments | Map\<string,string\> |  | {"arguments":"Hello uni microprogram"} | 配置启动小程序时传递的参数 |
| redirectPath | string |  | "pages/component/view/view" |  路径 |
| enableBackground | bool |  | false |  开启后台运行 |
| showAnimated | bool | true |  | 是否开启 show 小程序时的动画效果 默认：true |
| hideAnimated | bool | true |  | 是否开启 hide 时的动画效果 默认：true |

    

# iOS
介绍在引入模块时,iOS 方面要做的事.如工程权限配置等.

```
pod install x-engine-module-dcloud
```


# android
介绍在引入模块时,android 方面要做的事.如工程权限配置等.

gradle
```
implementation x-engine-module-dcloud
```


