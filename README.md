<h2 align="center">AutoApiTesting</h2>

## About The Project
AutoApiTesting 是自動化測試 API 的腳本，使用 Python 和 Pytest，程式會讀取 json 寫的測試資料生成 .py 檔，並自動執行測試生成報告。

## Usage
```cmd
$ git clone https://github.com/wilson8299/AutoApiTesting.git

$ pip3 install -r requirements.txt

$ pytest
```

## Data
```json
{
    "test_some_endpoint_success": {
        "url": "https://api.github.com/some/endpoint",
        "method": "get",
        "desc": "Test github endpoint api",
        "param": "",
        "assert": {
            "message": "Not Found",
            "documentation_url": "https://docs.github.com/rest"
        }
    },
    "test_some_endpoint_fail": {
        "url": "https://api.github.com/some/endpoint",
        "method": "get",
        "desc": "Test github endpoint api",
        "param": "",
        "assert": {
            "message": "Not Found Error",
            "documentation_url": "https://docs.github.com/rest"
        }
    }
}
```
| Ke        | Value               |
| :-------- |:------------------- |
| url       | 測試網址             |
| method    | 請求方法 (GET、POST) |  
| desc      | 測試描述             |   
| param     | 網址參數             | 
| assert    | 斷言條件             |

## License
[MIT License](./LICENSE).
