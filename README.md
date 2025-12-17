# 🏆 TuVision Studio: AI-ISP Tuning & Analysis Platform

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![PyQt5](https://img.shields.io/badge/GUI-PyQt5-green.svg)
![Status](https://img.shields.io/badge/Status-Phase%201%20Prototype-orange)
![Focus](https://img.shields.io/badge/Focus-ISP%20Algorithm%20%7C%20SoC%20Architecture-red)

> **Next-Generation ISP Toolchain: From Analysis to AI-Assisted Tuning.**
>
> 專為 ISP 演算法開發與 SoC 架構驗證打造的智慧化調校平台。

---

## 📸 Project Showcase (目前進度)

**Current Version: v0.1.0 (Phase 1 Analysis)**

![Phase 1 Screenshot](./assets/screenshot_phase1.png)
*(▲ Phase 1 介面展示：支援 Splitter 響應式佈局、深色暗房模式、ROI 選取與即時 AWB 數據分析)*

---

## 📖 Project Overview (專案願景)

**TuVision Studio** 是一套通用的 **ISP (Image Signal Processing)** 開發驗證工具。

在晶片設計 (SoC) 與演算法開發流程中，往往缺乏一套能整合「客觀畫質分析 (IQ Analysis)」、「流程模擬 (Pipeline Simulation)」與「參數調校 (Tuning)」的統一平台。

本專案旨在解決此斷層，透過 Python 全端開發，打造一個**可擴充 (Scalable)** 的架構。不僅提供畫質檢測功能，更作為 **Soft-ISP** 載體，協助演算法工程師加速 IP 模組的驗證與落地。

### 核心能力 (Key Capabilities):
1.  **Modular GUI Architecture:** 採用 PyQt5 建構響應式介面，模擬專業級 EDA/Tuning Tool 的操作體驗 (Splitter, Docking layout)。
2.  **Algorithm Validation:** 提供 "Research-to-Engineering" 的驗證環境，支持 MATLAB/Python 演算法的移植與視覺化。
3.  **AI Integration:** 實驗性導入 LLM (Google Gemini)，探索 "Text-to-Parameter" 的智慧調校可能性。

---

## 🛠 Features & Roadmap (功能路線圖)

### 🔴 Phase 1: IQ Analysis Module (已完成 v0.1.0)
建立穩定的影像輸入與分析基礎，作為 ISP Pipeline 的 Input/Output 檢測端。
- [x] **Professional UI:** 實作左側固定寬度、右側自適應延伸 (Responsive) 的專業佈局。
- [x] **Advanced Viewer:** 支援 Keep Aspect Ratio (等比縮放)、Anti-aliasing (平滑渲染) 與深色模式。
- [x] **ROI Inspection:** 支援 Region of Interest 選取與局部細節檢視。
- [x] **Statistics Monitor:** 即時計算 RGB 平均值與 AWB Gain 相關數據。
- [x] **Media Support:** 支援多種影像格式讀取與 Frame 序列播放控制。

### 🟡 Phase 2: Tuning & Simulation (開發中)
模擬 ISP Pipeline 的參數調校過程。
- [ ] **Tuning Interface:** 實作傳統 ISP 模組 (BLC, CCM, Gamma) 的參數滑桿控制。
- [ ] **AI Copilot:** 整合 Google Gemini API，輔助使用者進行直覺式的參數調整。
- [ ] **Pipeline Switching:** 模擬 SoC 內部切換 Hard-ISP 與 Neural-ISP 路徑的架構。

### 🟢 Phase 3: Algorithm R&D Lab (規劃中)
專注於前瞻演算法的開發、移植與驗證 (Post-Processing Unit)。
- [ ] **Legacy Code Porting (重點):**
    -   將開發者發表的 **Image Fusion (影像融合)** 期刊論文演算法，從 **MATLAB 移植至 Python**。
    -   驗證其在 Python 環境下的效能與畫質表現。
- [ ] **Computational Module:** 模擬 SoC 後端的 Multi-Exposure HDR 或 Multi-Sensor Fusion 加速單元。

---

## 💻 Tech Stack (技術堆疊)

*   **Language:** Python 3.9
*   **GUI Framework:** PyQt5 (Qt Designer, Custom GraphicsView)
*   **Image Processing:** OpenCV, NumPy
*   **Version Control:** Git / GitHub

---

## 👨‍💻 About the Developer

**Benny Tu**
*   **Focus:** ISP Algorithm Design, SoC Architecture, Toolchain Development
*   **Background:** 具備影像融合 (Image Fusion) 之學術研究背景，致力於將演算法理論轉化為工程落地應用。

---