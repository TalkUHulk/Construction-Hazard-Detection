🇬🇧 [English](./README.md) | 🇹🇼 [繁體中文](./README-zh-tw.md)

<img width="100%" src="./assets/images/project_graphics/banner.gif" alt="AI-Driven Construction Safety Banner">

<div align="center">
   <a href="examples/YOLO_server_api">模型伺服器</a> |
   <a href="examples/streaming_web">串流網頁</a> |
   <a href="examples/user_management">用戶管理</a> |
   <a href="examples/YOLO_data_augmentation">YOLO 數據增強</a> |
   <a href="examples/YOLO_evaluation">YOLO 評估</a> |
   <a href="examples/YOLO_train">YOLO 訓練</a>
</div>

<br>

<div align="center">
   <a href="https://www.python.org/downloads/release/python-3127/">
      <img src="https://img.shields.io/badge/python-3.12.7-blue?logo=python" alt="Python 3.12.7">
   </a>
   <a href="https://github.com/ultralytics/ultralytics">
      <img src="https://img.shields.io/badge/YOLO11-ultralytics-blue?logo=yolo" alt="YOLO11">
   </a>
   <a href="https://scikit-learn.org/stable/modules/generated/sklearn.cluster.HDBSCAN.html">
      <img src="https://img.shields.io/badge/HDBSCAN-sklearn-orange?logo=scikit-learn" alt="HDBSCAN sklearn">
   </a>
   <a href="https://flask.palletsprojects.com/en/3.0.x/">
      <img src="https://img.shields.io/badge/flask-3.0.3-blue?logo=flask" alt="Flask 3.0.3">
   </a>
   <a href="https://github.com/pre-commit/pre-commit">
      <img src="https://img.shields.io/badge/pre--commit-4.0.1-blue?logo=pre-commit" alt="Pre-commit 4.0.1">
   </a>
   <a href="https://docs.pytest.org/en/latest/">
      <img src="https://img.shields.io/badge/pytest-8.3.3-blue?logo=pytest" alt="pytest 8.3.3">
   </a>
   <a href="https://codecov.io/github/yihong1120/Construction-Hazard-Detection" >
      <img src="https://codecov.io/github/yihong1120/Construction-Hazard-Detection/graph/badge.svg?token=E0M66BUS8D"/>
   </a>
</div>

<br>

"建築工地危險檢測系統" 是一款以人工智慧驅動的工具，旨在提升工地的安全性。該系統利用 YOLO 模型進行物件偵測，能夠識別以下潛在危險：

- 未佩戴安全帽的工人
- 未穿著安全背心的工人
- 靠近機械或車輛的工人
- 進入限制區域的工人，透過安全錐座標的計算和分群，限制區域將自動產生。

後處理算法進一步提高了偵測的準確性。該系統專為即時部署而設計，能夠對檢測到的危險進行即時分析並發出警報。

此外，該系統可通過網頁介面即時整合 AI 辨識結果，並通過 LINE、Messenger、微信和 Telegram 等即時通訊應用程式發送通知及現場實時影像，及時提醒和通知相關人員。系統還支援多種語言，允許用戶接收通知並以其首選語言與介面互動。支援的語言包括：

- 🇹🇼 繁體中文（台灣）
- 🇨🇳 簡體中文（中國大陸）
- 🇫🇷 法文
- 🇬🇧 英文
- 🇹🇭 泰文
- 🇻🇳 越南文
- 🇮🇩 印尼文

多語言支援使該系統在全球範圍內的使用者都能方便使用，提升了不同地區的可用性。

> **待辦事項**：新增對 WhatsApp 通知的支援，使用Line Message API。

<br>
<br>

<div align="center">
   <img src="./assets/images/hazard-detection.png" alt="diagram" style="width: 100%;">
</div>

<br>

## 內容

- [危險偵測範例](#hazard-detection-examples)
- [操作說明](#操作說明)
- [附加信息](#附加信息)
- [數據集信息](#數據集信息)
- [貢獻](#貢獻)
- [開發路線圖](#開發路線圖)
- [授權](#授權)

## 危險偵測範例

以下是系統實時危險偵測的範例：

<div style="display: flex; justify-content: space-between; flex-wrap: wrap;">
  <!-- 範例 1: 未佩戴安全帽或安全背心的工人 -->
  <div style="text-align: center; flex-basis: 33%;">
    <img src="./assets/images/demo/person_did_not_wear_safety_vest.png" alt="未佩戴安全帽或安全背心的工人" style="width: 300px; height: 200px; object-fit: cover;">
    <p>未佩戴安全帽或安全背心的工人</p>
  </div>

  <!-- 範例 2: 工人接近機具或車輛 -->
  <div style="text-align: center; flex-basis: 33%;">
    <img src="./assets/images/demo/person_near_machinery.jpg" alt="工人接近機具或車輛" style="width: 300px; height: 200px; object-fit: cover;">
    <p>工人接近機具或車輛</p>
  </div>

  <!-- 範例 3: 工人在限制區域內 -->
  <div style="text-align: center; flex-basis: 33%;">
    <img src="./assets/images/demo/persons_in_restricted_zones.jpg" alt="工人在限制區域內" style="width: 300px; height: 200px; object-fit: cover;">
    <p>工人在限制區域內</p>
  </div>
</div>

## 操作說明

在運行應用程式之前，您需要配置系統，指定視頻流的詳細信息和其他參數，這些信息需要在 YAML 配置文件中進行設置。示例配置文件 `configuration.yaml` 應該看起來像這樣：

```yaml
# 這是一個視訊配置的列表
- video_url: "rtsp://example1.com/stream"  # 視訊串流的 URL
  site: "建築工地"  # 監控系統的位置
  stream_name: "前門"  # 監視器的名稱或編號
  model_key: "yolo11n"  # 視訊所使用的模型鍵
  notifications:  # LINE 通知的令牌列表及對應的語言
    line_token_1: language_1
    line_token_2: language_2
  detect_with_server: True  # 使用伺服器進行物件偵測
  expire_date: "2024-12-31T23:59:59"  # 到期日期，使用 ISO 8601 格式
- video_url: "串流 URL"  # 視訊串流的 URL
  site: "工廠1"  # 監控系統的位置
  stream_name: "相機1"  # 監視器的名稱或編號
  model_key: "yolo11n"  # 用於偵測的模型鍵
  notifications:  # LINE 通知的令牌列表及對應的語言
    line_token_3: language_3
    line_token_4: language_4
  detect_with_server: False  # 在本地進行物件偵測
  expire_date: "無到期日期"  # 無到期日期的字串
```

數組中的每個對象代表一個視頻流配置，包含以下字段：

- `video_url`：視訊串流的 URL，可能包括：
   - 監控流
   - RTSP
   - 副流
   - YouTube 視頻或直播
   - Discord
- `site`：監控系統的位置（例如：建築工地、工廠）。
- `stream_name`：指派給監視器或串流的名稱（例如：「前門」、「相機1」）。
- `model_key`：機器學習模型的識別鍵（例如：「yolo11n」）。
- `notifications`：LINE 通知的 API 令牌和對應語言的列表。
   - `line_token_1`, `line_token_2` 等：這些是 LINE API 令牌。
   - `language_1`, `language_2` 等：通知的語言（例如：「en」表示英文，「zh-TW」表示繁體中文）。有關如何獲取 LINE 令牌的資訊，請參閱  [Line Notify教學](docs/zh/line_notify_guide_zh.md)。
- `detect_with_server`：布林值，指示是否使用伺服器 API 進行物件偵測。如果為 `True`，系統將使用伺服器進行物件偵測。如果為 `False`，物件偵測將在本地機器上執行。
- `expire_date`：視訊串流配置的到期日期，使用 ISO 8601 格式（例如：「2024-12-31T23:59:59」）。如果沒有到期日期，可以使用類似「無到期日期」的字串。

<br>

<details>
   <summary>Docker</summary>

   ### 使用 Docker

   要運行危險檢測系統，您需要在機器上安裝 Docker 和 Docker Compose。按照以下步驟來啟動系統：

   1. 將存儲庫克隆到本地機器。
      ```bash
      git clone https://github.com/yihong1120/Construction-Hazard-Detection.git
      ```
   2. 進入克隆的目錄。
      ```bash
      cd Construction-Hazard-Detection
      ```
   3. 使用 Docker Compose 構建並運行服務：
      ```bash
      docker-compose up --build
      ```

   4. 使用特定的配置文件運行主應用程序，使用以下命令：
      ```bash
      docker-compose run main-application python main.py --config /path/in/container/configuration.yaml
      ```
      將 `/path/in/container/configuration.yaml` 替換為容器內配置文件的實際路徑。

   5. 停止服務，使用以下命令：
      ```bash
      docker-compose down
      ```

</details>

<details>
   <summary>Python</summary>

   ### 使用 Python

   要在終端運行危險檢測系統，您需要在機器上安裝 Python。按照以下步驟來啟動系統：

   1. 將存儲庫克隆到本地機器。
      ```bash
      git clone https://github.com/yihong1120/Construction-Hazard-Detection.git
      ```

   2. 進入克隆的目錄。
      ```bash
      cd Construction-Hazard-Detection
      ```

   3. 安裝所需的軟體包：
      ```bash
      pip install -r requirements.txt
      ```

   4. 安裝並啟動 MySQL 服務：

      Linux 使用者：
      ```bash
      sudo apt install mysql-server
      sudo systemctl start mysql.service
      ```

      對於其他人，您可以在此[連結](https://dev.mysql.com/downloads/)下載並安裝適用於您的作業系統的MySQL。

   5. 設置用戶帳戶和密碼。使用以下命令啟動用戶管理 API：
      ```bash
      gunicorn -w 1 -b 0.0.0.0:8000 "examples.user_management.app:user-managements-app"
      ```
      建議使用 Postman 應用程式與 API 進行互動。

   6. 要運行物體檢測 API，使用以下命令：
      ```bash
      gunicorn -w 1 -b 0.0.0.0:8001 "examples.YOLO_server_api.app:YOLO-server-api-app"
      ```

   7. 使用特定的配置文件運行主應用程序，使用以下命令：
      ```bash
      python3 main.py --config /path/to/your/configuration.yaml
      ```
      將 `/path/to/your/configuration.yaml` 替換為您的配置文件的實際路徑。

   8. 要啟動串流 Web 服務，執行以下命令：

      對於 Linux 使用者：
      ````bash
      gunicorn -w 1 -k eventlet -b 127.0.0.1:8002 "examples.streaming_web.app:streaming-web-app"
      ````

      對於 Windows 使用者：
      ````
      waitress-serve --host=127.0.0.1 --port=8002 "examples.streaming_web.app:streaming-web-app"
      ````

</details>

## 附加信息

- 系統日誌可在 Docker 容器內部訪問，可用於調試目的。
- 如果啟用，檢測到的輸出圖像將保存到指定的輸出路徑。
- 如果檢測到危險，將在指定小時通過 LINE 消息 API 發送通知。

### 注意事項
- 確保 `Dockerfile` 存在於項目的根目錄中，並根據您的應用程序的要求進行了正確配置。
- `-p 8080:8080` 標誌將容器的 8080 端口映射到主機機器的 8080 端口，允許您通過主機的 IP 地址和端口號訪問應用程序。

有關 Docker 使用和命令的更多信息，請參閱 [Docker 文檔](https://docs.docker.com/)。

## 數據集信息
訓練此模型的主要數據集是 [Roboflow 的建築工地安全圖像數據集](https://www.kaggle.com/datasets/snehilsanyal/construction-site-safety-image-dataset-roboflow/data)。我們已經用額外的註釋豐富了這個數據集，並在 Roboflow 上公開訪問。增強的數據集可以在這裡找到：[Roboflow 上的建築危險檢測](https://universe.roboflow.com/side-projects/construction-hazard-detection)。此數據集包括以下標籤：

- `0: '安全帽'`
- `1: '口罩'`
- `2: '無安全帽'`
- `3: '無口罩'`
- `4: '無安全背心'`
- `5: '人'`
- `6: '安全錐'`
- `7: '安全背心'`
- `8: '機械'`
- `9: '車輛'`

<details>
   <summary>檢測模型</summary>

   | Model   | size<br><sup>(pixels) | mAP<sup>val<br>50 | mAP<sup>val<br>50-95 | params<br><sup>(M) | FLOPs<br><sup>(B) |
   | ------- | --------------------- | ------------------ | ------------------ | ----------------- | ----------------- |
   | YOLO11n | 640                   | 54.1               | 31.0               | 2.6               | 6.5               |
   | YOLO11s | 640                   | //                 | //                 | 9.4               | 21.6              |
   | YOLO11m | 640                   | //                 | //                 | 20.1              | 68.0              |
   | YOLO11l | 640                   | //                 | //                 | 25.3              | 86.9              |
   | YOLO11x | 640                   | 76.8               | 52.5               | 56.9              | 194.9             |

</details>

<br>

我們的全面數據集確保模型能夠識別建築環境中常見的各種潛在危險。

## 貢獻
我們歡迎對此項目的貢獻。請按照以下步驟操作：
1. 分叉存儲庫。
2. 進行更改。
3. 提交一個清晰描述您改進的拉取請求。

## 開發路線圖
- [x] 數據收集和預處理。
- [x] 使用建築工地數據訓練 YOLO 模型。
- [x] 開發後處理技術以提高準確性。
- [x] 實施實時分析和警報系統。
- [x] 在模擬環境中進行測試和驗證。
- [x] 在實際建築工地進行現場測試。
- [x] 根據用戶反饋進行持續維護和更新。

## 待辦事項

- 新增對 WhatsApp 通知的支援，
- 在 server_api 和 streaming_web 中從 Flask 切換到 Fastapi

## 授權
此項目根據 [AGPL-3.0](LICENSE.md) 授權。
