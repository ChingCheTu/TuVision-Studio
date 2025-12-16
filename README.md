# 🏆 TuVision Studio: AI-ISP Tuning & Analysis Platform

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![PyQt5](https://img.shields.io/badge/GUI-PyQt5-green.svg)
![Status](https://img.shields.io/badge/Status-Prototype%20v0.1.0-orange)
![Focus](https://img.shields.io/badge/Focus-Automotive%20%7C%20SoC%20Architecture-red)

> **Bridging Classic Computer Vision with Generative AI for Automotive Excellence.**
>
> 結合傳統 ISP 影像處理與 Google Gemini LLM 的下一代畫質調校平台。

---

## 📺 Demo Preview (成品展示)

<!-- 之後錄好 YouTube 影片或做好 GIF，把連結貼在這裡 -->
<!-- 範例寫法：[![Watch the video](https://img.youtube.com/vi/你的影片ID/maxresdefault.jpg)](https://youtu.be/你的影片ID) -->

*目前版本展示 (Phase 1 Analysis):*
*(建議這裡放一張軟體介面的截圖，檔案放在 assets 資料夾內)*
`![Main Interface](./assets/screenshot_main.png)`

---

## 📖 Project Overview (專案簡介)

**TuVision Studio** 是一套針對車用影像 (Automotive Imaging) 與高階 SoC 架構設計的一站式開發工具。旨在解決傳統 ISP 調校過於依賴人工試誤 (Trial-and-Error) 的痛點，並整合學術界的影像融合演算法。

### 核心能力 (Key Capabilities):
1.  **Automated IQ Analysis:** 自動化分析圖表與數據 (Delta E, SNR)。
2.  **AI-Assisted Tuning:** 利用 LLM (Google Gemini) 實現 "Text-to-Parameter" 的直覺式調校。
3.  **Research-to-Engineering:** 將學術發表的 Image Fusion 演算法落地整合至 GUI 平台。

---

## 🛠 Features (功能模組)

### 🔴 Phase 1: IQ Analysis Bot (智慧畫質檢測) - *Current v0.1.0*
- [x] 支援 DNG/RAW/JPG 影像讀取與 EXIF 解析。
- [x] 自動偵測 Macbeth ColorChecker (24色卡)。
- [x] 計算 **Delta E (76/2000)** 色準數據。
- [x] 視覺化 CIE Lab 色度圖與 SNR 分析。

### 🟡 Phase 2: AI-ISP Tuning Copilot (開發中)
- [ ] **Soft-ISP Pipeline:** 模擬 BLC -> Demosaic -> CCM -> Gamma 流程。
- [ ] **Generative AI Integration:** 串接 Google Gemini API，提供畫質診斷報告。
- [ ] **Natural Language Tuning:** 輸入「讓膚色暖一點」，自動轉換為 CCM 矩陣參數。

### 🟢 Phase 3: R&D Lab (研發實驗室)
- [ ] **Advanced Sensor Fusion:** 整合開發者發表的兩篇期刊論文演算法。
- [ ] **Algorithm Validation:** 比較傳統 ISP 與自研 Fusion 算法的差異 (Split View)。
- [ ] **HDR & Dehazing:** 車用場景的特殊影像增強。

---

## 💻 Tech Stack (技術堆疊)

*   **Core:** Python 3.9
*   **GUI:** PyQt5 (Qt Designer)
*   **Computer Vision:** OpenCV (cv2), NumPy, Pillow, Rawpy
*   **Color Science:** colour-science, Matplotlib
*   **AI Engine:** Google Generative AI (Gemini API)
*   **Version Control:** Git / GitHub

---

## 🚀 Getting Started (如何執行)

### Prerequisites (環境需求)
請確保安裝 Anaconda 或 Python 3.9+。

### Installation (安裝步驟)

1. Clone the repository:
   ```bash
   git clone https://github.com/ChingCheTu/TuVision-Studio.git
   cd TuVision-Studio