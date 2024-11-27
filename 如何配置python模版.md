### 如何配置python的模版
- 配置模版如下操作
文件-》首选项-》配置代码片段-》python.json

```json
"Python Template": {
		"prefix": "pt",
		"body": [
			"# -*- coding:utf-8 -*-",
			"# coding=utf-8",
			"'''",
			"@Author: fat_joe",
			"@Date: $CURRENT_YEAR/$CURRENT_MONTH/$CURRENT_DATE $CURRENT_HOUR:$CURRENT_MINUTE",
			"@Desc: ...",
			"'''",
			"",
			"",
			"if __name__ == '__main__':",
			"    pass"
		],
		"description": "Python Template"
	}

```