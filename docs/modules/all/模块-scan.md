


 
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
undefined
`



## openScanView



	
**参数说明**

| name                        | type      | optional | default   | comment  |
| --------------------------- | --------- | -------- | --------- |--------- |
| __event__ | string |  |  | 扫码结果 xx(result) |

    lt) |

    

# iOS
介绍在引入模块时,iOS 方面要做的事.如工程权限配置等.

```
pod install x-engine-module-scan
```


# android
介绍在引入模块时,android 方面要做的事.如工程权限配置等.

gradle
```
implementation x-engine-module-scan
```


