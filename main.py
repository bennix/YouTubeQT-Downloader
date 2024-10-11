import os
import sys
import time
import subprocess
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
                             QLineEdit, QPushButton, QLabel, QProgressBar, QFileDialog, QMessageBox)
from PyQt5.QtCore import Qt, QThread, pyqtSignal, QMetaObject, Q_ARG, Qt
import yt_dlp as youtube_dl
import re

class DownloadThread(QThread):
    progress = pyqtSignal(dict)
    finished = pyqtSignal(bool, str)

    def __init__(self, url, download_path, ydl_opts, cookies_file=None):
        super().__init__()
        self.url = url
        self.download_path = download_path
        self.ydl_opts = ydl_opts
        self.ydl_opts['no_color'] = True
        self.ydl_opts['progress_hooks'] = [self.progress_hook]
        if cookies_file:
            self.ydl_opts['cookiefile'] = cookies_file

    def progress_hook(self, d):
        self.progress.emit(d)

    def run(self):
        try:
            with youtube_dl.YoutubeDL(self.ydl_opts) as ydl:
                ydl.download([self.url])
            self.finished.emit(True, "下载完成")
        except Exception as e:
            self.finished.emit(False, str(e))

class YouTubeDownloader(QMainWindow):
    update_progress_signal = pyqtSignal(dict)

    def __init__(self):
        super().__init__()
        self.initUI()
        self.update_progress_signal.connect(self.update_progress)

    def initUI(self):
        self.setWindowTitle('YouTube 下载器')
        self.setGeometry(100, 100, 600, 200)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # URL输入
        url_layout = QHBoxLayout()
        self.url_input = QLineEdit()
        self.url_input.setPlaceholderText("在此输入视频URL")
        url_layout.addWidget(self.url_input)
        self.load_button = QPushButton("加载视频信息")
        self.load_button.clicked.connect(self.load_video_info)
        url_layout.addWidget(self.load_button)
        layout.addLayout(url_layout)

        # 视频标题
        self.title_label = QLabel("视频标题：")
        layout.addWidget(self.title_label)

        # 下载按钮
        button_layout = QHBoxLayout()
        self.browse_button = QPushButton("选择下载路径")
        self.browse_button.clicked.connect(self.browse_path)
        button_layout.addWidget(self.browse_button)
        self.download_button = QPushButton("开始下载")
        self.download_button.clicked.connect(self.start_download)
        button_layout.addWidget(self.download_button)
        
        # Cookies 设置按钮
        self.cookies_button = QPushButton("设置 Cookies")
        self.cookies_button.clicked.connect(self.set_cookies_file)
        button_layout.addWidget(self.cookies_button)
        
        layout.addLayout(button_layout)

        # 进度显示
        progress_layout = QHBoxLayout()
        self.progress_bar = QProgressBar()
        progress_layout.addWidget(self.progress_bar)
        self.progress_label = QLabel("0%")
        progress_layout.addWidget(self.progress_label)
        layout.addLayout(progress_layout)

        # 下载速度和预计剩余时间
        self.speed_label = QLabel("下载速度: --")
        layout.addWidget(self.speed_label)
        self.eta_label = QLabel("预计剩余时间: --")
        layout.addWidget(self.eta_label)

        self.download_path = ""
        self.cookies_file = None

    def load_video_info(self):
        url = self.url_input.text().strip()
        if not url:
            QMessageBox.warning(self, "错误", "请输入有效的视频URL。")
            return

        try:
            ydl_opts = {'quiet': True}
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
                title = info.get('title', 'Unknown Title')
                self.title_label.setText(f"视频标题：{title}")
        except Exception as e:
            QMessageBox.warning(self, "错误", f"加载视频信息失败：{str(e)}")

    def browse_path(self):
        self.download_path = QFileDialog.getExistingDirectory(self, "选择下载路径")
        if self.download_path:
            self.setWindowTitle(f"YouTube 下载器 - 下载路径: {self.download_path}")

    def set_cookies_file(self):
        cookies_file, _ = QFileDialog.getOpenFileName(self, "选择 Cookies 文件", "", "Text Files (*.txt)")
        if cookies_file:
            self.cookies_file = cookies_file
            QMessageBox.information(self, "Cookies 设置", f"Cookies 文件已设置: {cookies_file}")

    def start_download(self):
        url = self.url_input.text().strip()
        if not url:
            QMessageBox.warning(self, "错误", "请输入有效的视频URL。")
            return
        if not self.download_path:
            QMessageBox.warning(self, "错误", "请选择下载路径。")
            return

        ydl_opts = {
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
            'outtmpl': os.path.join(self.download_path, '%(title)s.%(ext)s'),
            'progress_hooks': [self.show_progress],
            'postprocessors': [
                {'key': 'FFmpegVideoConvertor', 'preferedformat': 'mp4'},
            ],
            'keepvideo': True,
        }

        if self.cookies_file:
            ydl_opts['cookiefile'] = self.cookies_file

        self.progress_bar.setValue(0)
        self.progress_label.setText("0%")
        self.speed_label.setText("下载速度: --")
        self.eta_label.setText("预计剩余时间: --")

        self.download_thread = DownloadThread(url, self.download_path, ydl_opts, self.cookies_file)
        self.download_thread.progress.connect(self.safe_update_progress)
        self.download_thread.finished.connect(self.download_finished)
        self.download_thread.start()

        self.download_button.setEnabled(False)

    def safe_update_progress(self, d):
        self.update_progress_signal.emit(d)

    def show_progress(self, d):
        if d['status'] == 'downloading':
            percent = d.get('_percent_str')
            speed = d.get('_speed_str')
            eta = d.get('_eta_str')
            
            if percent:
                match = re.search(r'(\d+\.\d+)%', percent)
                if match:
                    percent_float = float(match.group(1))
                    self.progress_bar.setValue(int(percent_float))
                    self.progress_label.setText(f"{percent_float:.1f}%")
            
            if speed:
                self.speed_label.setText(f"下载速度: {speed}")
            
            if eta:
                self.eta_label.setText(f"预计剩余时间: {eta}")

    def update_progress(self, d):
        if d['status'] == 'downloading':
            percent = d.get('_percent_str', '')
            speed = d.get('_speed_str', '')
            eta = d.get('_eta_str', '')
            
            if percent:
                match = re.search(r'(\d+\.\d+)%', percent)
                if match:
                    percent_float = float(match.group(1))
                    self.progress_bar.setValue(int(percent_float))
                    self.progress_label.setText(f"{percent_float:.1f}%")
            
            if speed:
                self.speed_label.setText(f"下载速度: {speed}")
            
            if eta:
                self.eta_label.setText(f"预计剩余时间: {eta}")

    def download_finished(self, success, message):
        self.download_button.setEnabled(True)
        if success:
            self.progress_bar.setValue(100)
            self.progress_label.setText("100%")
            self.speed_label.setText("下载速度: --")
            self.eta_label.setText("预计剩余时间: --")
            QMessageBox.information(self, "下载完成", message)
        else:
            QMessageBox.warning(self, "下载失败", message)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = YouTubeDownloader()
    ex.show()
    sys.exit(app.exec_())