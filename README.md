# YouTube 下载器

这是一个基于PyQt5和yt-dlp的YouTube视频下载器，提供了简单易用的图形界面。

## 功能特点

- 下载YouTube视频和音频
- 支持选择下载质量
- 显示下载进度、速度和预计剩余时间
- 支持使用Cookies文件进行身份验证
- 简洁直观的用户界面

## 安装要求

- Python 3.6+
- PyQt5
- yt-dlp

## 安装步骤

1. 克隆此仓库：

   ```
   git clone https://github.com/yourusername/youtube-downloader.git
   ```

2. 进入项目目录：

   ```
   cd youtube-downloader
   ```

3. 安装依赖：

   ```
   pip install -r requirements.txt
   ```

## 使用方法

1. 运行主程序：

   ```
   python main.py
   ```

2. 在输入框中粘贴YouTube视频URL。

3. 点击"加载视频信息"按钮获取视频详情。

4. 选择下载路径。

5. （可选）设置Cookies文件。

6. 点击"开始下载"按钮开始下载。

## Cookies 处理

本项目支持使用Cookies文件进行身份验证，以下载需要登录的视频。我们提供了一个脚本来将JSON格式的Cookies转换为Netscape格式，这是yt-dlp所需的格式。

### 从Firefox获取Cookies

1. 安装 "Cookie Quick Manager" 插件：

   - 访问 [Firefox Add-ons 网站](https://addons.mozilla.org/en-US/firefox/addon/cookie-quick-manager/)
   - 搜索 "Cookie Quick Manager" 并安装插件

2. 登录到YouTube

3. 导出Cookies：

   - 点击Firefox工具栏中的 "Cookie Quick Manager" 图标
   - 在插件界面中，找到并选择 youtube.com 域名
   - 点击 "Export" 按钮
   - 在导出选项中，选择 "JSON"格式
   - 选择保存位置并命名文件（例如 `cookies.json`）

4. 使用 `changejson.py` 脚本将JSON格式转换为Netscape格式：

   ```
   python changejson.py
   ```

5. 脚本会生成 `cookies.txt` 文件，该文件将在另一个 Python 脚本中使用 GUI 会提示选择该文件，这个文件可以在YouTube下载器中使用。

注意：请勿分享您的Cookies文件，因为它包含敏感的登录信息。

### 自定义Cookies转换

如果您需要自定义Cookies的转换过程，可以编辑 `changejson.py` 文件：

- 修改 `json_file` 变量来更改输入的JSON文件名。
- 修改 `output_file` 变量来更改输出的Netscape格式文件名。

## 如何获取Firefox的Cookies文件

要使用Firefox的Cookies进行身份验证，请按照以下步骤操作：

1. 安装 "Export Cookies" 插件：
   - 访问 [Firefox Add-ons 网站](https://addons.mozilla.org/en-US/firefox/addon/export-cookies-txt/)
   - 搜索 "Export Cookies" 并安装插件

2. 登录到YouTube

3. 导出Cookies：
   - 点击Firefox工具栏中的 "Export Cookies" 图标
   - 选择 "Export to file"
   - 选择保存位置并命名文件（例如 `youtube_cookies.txt`）

4. 在YouTube下载器中使用Cookies文件：
   - 点击 "设置 Cookies" 按钮
   - 选择刚才保存的Cookies文件

注意：请勿分享您的Cookies文件，因为它包含敏感的登录信息。

## 贡献

欢迎提交问题报告和拉取请求。对于重大更改，请先开issue讨论您想要改变的内容。

## 许可证

[MIT](https://choosealicense.com/licenses/mit/)

# YouTube Downloader

This is a YouTube video downloader based on PyQt5 and yt-dlp, providing a simple and user-friendly graphical interface.

## Features

- Download YouTube videos and audio
- Support for selecting download quality
- Display download progress, speed, and estimated remaining time
- Support for authentication using Cookies file
- Clean and intuitive user interface

## Requirements

- Python 3.6+
- PyQt5
- yt-dlp

## Installation

1. Clone this repository:

   ```
   git clone https://github.com/yourusername/youtube-downloader.git
   ```

2. Enter the project directory:

   ```
   cd youtube-downloader
   ```

3. Install dependencies:

   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the main program:

   ```
   python main.py
   ```

2. Paste the YouTube video URL in the input box.

3. Click the "Load Video Info" button to get video details.

4. Choose the download path.

5. (Optional) Set up the Cookies file.

6. Click the "Start Download" button to begin downloading.

## Cookies Handling

This project supports using a Cookies file for authentication to download videos that require login. We provide a script to convert Cookies from JSON format to Netscape format, which is required by yt-dlp.

### Getting Cookies from Firefox

1. Install the "Cookie Quick Manager" add-on:

   - Visit the [Firefox Add-ons website](https://addons.mozilla.org/en-US/firefox/addon/cookie-quick-manager/)
   - Search for "Cookie Quick Manager" and install the add-on

2. Log in to YouTube

3. Export Cookies:

   - Click on the "Cookie Quick Manager" icon in the Firefox toolbar
   - In the add-on interface, find and select the youtube.com domain
   - Click the "Export" button
   - In the export options, select "JSON" format
   - Choose a save location and name the file (e.g., `cookies.json`)

4. Use the `changejson.py` script to convert JSON format to Netscape format:

   ```
   python changejson.py
   ```

5. The script will generate a `cookies.txt` file, which will be used in another Python script. The GUI will prompt you to select this file, which can be used in the YouTube downloader.

Note: Do not share your Cookies file as it contains sensitive login information.

### Custom Cookies Conversion

If you need to customize the Cookies conversion process, you can edit the `changejson.py` file:

- Modify the `json_file` variable to change the input JSON filename.
- Modify the `output_file` variable to change the output Netscape format filename.

## How to Get Firefox Cookies File

To use Firefox Cookies for authentication, follow these steps:

1. Install the "Export Cookies" add-on:
   - Visit the [Firefox Add-ons website](https://addons.mozilla.org/en-US/firefox/addon/export-cookies-txt/)
   - Search for "Export Cookies" and install the add-on

2. Log in to YouTube

3. Export Cookies:
   - Click on the "Export Cookies" icon in the Firefox toolbar
   - Select "Export to file"
   - Choose a save location and name the file (e.g., `youtube_cookies.txt`)

4. Use the Cookies file in the YouTube downloader:
   - Click the "Set Cookies" button
   - Select the Cookies file you just saved

Note: Do not share your Cookies file as it contains sensitive login information.

## Contributing

Issue reports and pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)

# YouTube ダウンローダー

これはPyQt5とyt-dlpに基づいたYouTubeビデオダウンローダーで、シンプルで使いやすいグラフィカルインターフェースを提供します。

## 機能

- YouTubeの動画と音声のダウンロード
- ダウンロード品質の選択をサポート
- ダウンロードの進捗、速度、推定残り時間の表示
- Cookiesファイルを使用した認証をサポート
- クリーンで直感的なユーザーインターフェース

## 要件

- Python 3.6+
- PyQt5
- yt-dlp

## インストール

1. このリポジトリをクローンします：

   ```
   git clone https://github.com/yourusername/youtube-downloader.git
   ```

2. プロジェクトディレクトリに入ります：

   ```
   cd youtube-downloader
   ```

3. 依存関係をインストールします：

   ```
   pip install -r requirements.txt
   ```

## 使用方法

1. メインプログラムを実行します：

   ```
   python main.py
   ```

2. 入力ボックスにYouTubeビデオのURLを貼り付けます。

3. "動画情報を読み込む"ボタンをクリックして動画の詳細を取得します。

4. ダウンロードパスを選択します。

5. （オプション）Cookiesファイルを設定します。

6. "ダウンロード開始"ボタンをクリックしてダウンロードを開始します。

## Cookiesの処理

このプロジェクトは、ログインが必要な動画をダウンロードするために、Cookiesファイルを使用した認証をサポートしています。JSONフォーマットのCookiesをyt-dlpが必要とするNetscapeフォーマットに変換するスクリプトを提供しています。

### FirefoxからCookiesを取得する

1. "Cookie Quick Manager"アドオンをインストールします：

   - [Firefox Add-onsウェブサイト](https://addons.mozilla.org/en-US/firefox/addon/cookie-quick-manager/)にアクセスします
   - "Cookie Quick Manager"を検索してアドオンをインストールします

2. YouTubeにログインします

3. Cookiesをエクスポートします：

   - FirefoxツールバーのCookie Quick Managerアイコンをクリックします
   - アドオンインターフェースで、youtube.comドメインを見つけて選択します
   - "Export"ボタンをクリックします
   - エクスポートオプションで、"JSON"フォーマットを選択します
   - 保存場所を選択し、ファイルに名前を付けます（例：`cookies.json`）

4. `changejson.py`スクリプトを使用してJSONフォーマットをNetscapeフォーマットに変換します：

   ```
   python changejson.py
   ```

5. スクリプトは`cookies.txt`ファイルを生成します。このファイルは別のPythonスクリプトで使用され、GUIがこのファイルの選択を促します。このファイルはYouTubeダウンローダーで使用できます。

注意：Cookiesファイルには機密のログイン情報が含まれているため、共有しないでください。

### カスタムCookies変換

Cookiesの変換プロセスをカスタマイズする必要がある場合は、`changejson.py`ファイルを編集できます：

- `json_file`変数を変更して、入力JSONファイル名を変更します。
- `output_file`変数を変更して、出力Netscapeフォーマットファイル名を変更します。

## FirefoxのCookiesファイルを取得する方法

Firefox Cookiesを認証に使用するには、以下の手順に従ってください：

1. "Export Cookies"アドオンをインストールします：
   - [Firefox Add-onsウェブサイト](https://addons.mozilla.org/en-US/firefox/addon/export-cookies-txt/)にアクセスします
   - "Export Cookies"を検索してアドオンをインストールします

2. YouTubeにログインします

3. Cookiesをエクスポートします：
   - FirefoxツールバーのExport Cookiesアイコンをクリックします
   - "Export to file"を選択します
   - 保存場所を選択し、ファイルに名前を付けます（例：`youtube_cookies.txt`）

4. YouTubeダウンローダーでCookiesファイルを使用します：
   - "Cookiesを設定"ボタンをクリックします
   - 保存したCookiesファイルを選択します

注意：Cookiesファイルには機密のログイン情報が含まれているため、共有しないでください。

## 貢献

問題報告とプルリクエストを歓迎します。大きな変更については、まず問題を開いて変更したい内容について議論してください。

## ライセンス

[MIT](https://choosealicense.com/licenses/mit/)
