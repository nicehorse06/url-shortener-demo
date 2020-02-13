## 建構虛擬環境
python3 -m venv vir_env

## 可額外新增的功能
* 用hash來縮網址
* 給予超連結
* 複製網址功能
* 加上縮網址密碼
* 新增錯誤網址(4XX)的提示訊息
* 更多單元測試

## ref
* [django-short-urls](https://github.com/mouradmourafiq/django-short-urls)

## docker 指令
### docker compose
建置docker內容，todo功能
* docker volume inspect nginx-gunicorn-flask_postgres_data

#### 開發環境
##### 重啟指令，建立新的containers
docker-compose up -d --build
* build為建立container，docker-compose build
* up -d為背景執行container，docker-compose up -d
##### 關閉指令，移除之前建立的containers
docker-compose down -v
##### 在container中下建立admin的指令
docker-compose exec web python manage.py admin

#### 正式環境
##### 重啟指令，建立新的containers
docker-compose -f docker-compose.prod.yml up -d --build

##### 關閉指令，移除之前建立的containers
docker-compose -f docker-compose.prod.yml down -v

##### 在container中下建立admin的指令
* docker-compose exec web python manage.py createsuperuser

##### 查看log
docker-compose -f docker-compose.prod.yml logs -f 