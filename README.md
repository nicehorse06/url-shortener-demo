# Django URL Shortener demo

* python版本為3.6.8
* Django版本為2.2.10

## 功能敘述
* 輸入合法的網址轉成帶有ID的縮網址
* 目前不支持網址回收功能，待新增
* 目前不支持相同網址對應到同一縮網址功能

## docker 指令
#### 開發環境部屬

##### 重啟指令，建立新的containers
docker-compose up -d --build
`執行於 http://0.0.0.0:8000/`
##### 關閉指令，移除之前建立的containers
docker-compose down -v

#### 正式環境部屬

##### 重啟指令，建立新的containers
docker-compose -f docker-compose.prod.yml up -d --build
`執行於 http://0.0.0.0:8000/`

##### 關閉指令，移除之前建立的containers
docker-compose -f docker-compose.prod.yml down -v

##### 查看log
docker-compose -f docker-compose.prod.yml logs -f 

## 可額外新增的功能
* 用hash來縮網址
* 給予超連結
* 複製網址功能
* 加上縮網址密碼
* 新增錯誤網址(4XX)的提示訊息
* 更多單元測試