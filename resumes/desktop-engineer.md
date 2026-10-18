# Miracle Apata — Desktop Software Engineer

[GitHub](https://github.com/prmpsmart) • [LinkedIn](https://linkedin.com/in/prmpsmart) • [Email](mailto:prmpsmart@gmail.com) • [Portfolio](https://prmpsmart.github.io) • +234 816 852 4477  
Akure, Nigeria (WAT, UTC+1) · Remote · Open to remote roles

## Summary

Experienced desktop software engineer specializing in cross-platform applications for **Windows** and **macOS** using **Python (PySide6)** and **SwiftUI**. Adept at building multilingual educational tools used by universities, academies, and institutions for standardized testing. Experienced in packaging with PyInstaller and Inno Setup and in delivering native desktop experiences. Python is my first language (self-taught from 2018/2019).

## Work Experience

**DINATEN** — Santa Cruz de Tenerife, Spain (Remote)  
[https://dinaten.com](https://dinaten.com)  
**Aug 2023 – Present**

- Developed and maintained [piXeval](https://dinaten.com/pixeval-v7/) and **pixEBAP**, two educational desktop applications for managing and correcting multiple-choice exams.
- Built apps using **PySide6** (Qt for Python), compiled with **PyInstaller**, and packaged installers with **Inno Setup**.
- Sole developer of the ground-up **rebuild of piXeval** (in progress): a Qt-free Python engine, a FastAPI HTTP/WebSocket backend, a React + TypeScript UI, and Qt WebEngine / pywebview desktop shells (40k+ lines of Python, 79 test files). Exams, documents, exports, and CAT3 answer-sheet generation (PDF, barcodes, print runs) are done, including a modular rewrite of the sheet-generation scripts supplied by DINATEN's owner.
- Created and maintained a **macOS-native version of piXeval** using **SwiftUI**, designed specifically for Apple users while ensuring feature parity with the Windows build.
- Ensured full cross-platform support across **Windows and macOS** with consistent UX.
- Supported multiple languages in the app interface: **Catalan**, **Spanish**, **English**, **Euskera**, and **French**.
- Integrated key features:
  - Bulk import from Word, Excel, and Moodle
  - Generation of up to 9 randomized models of the same exam
  - Scanning and automatic grading of answer sheets (up to 30 exams/minute) using OCR and OMR techniques implemented with OpenCV2, TensorFlow, and other supporting libraries
  - Delivery of student results via email
  - Advanced statistics and competency evaluation

## Skills

- **Languages:** Python, Swift (SwiftUI), SQL
- **Frameworks & Libraries:** PySide6, SwiftUI, OpenCV2, TensorFlow
- **Tools & Packaging:** PyInstaller, Inno Setup, Git, macOS development tools
- **Platforms:** Windows, macOS
- **App Languages:** Spanish, English, Catalan, Euskera, French
- **Tech Focus:** OCR/OMR, automated exam grading, cross-platform application development

## Projects

- **piXeval**

  - [Download](https://dinaten.com/pixeval-v7/)
  - Intelligent exam correction and evaluation tool for teachers and institutions.

- **pixEBAP**
  - Internal desktop application used for managing exam forms and student data.

- **piXeval rebuild** _(in progress, sole developer)_
  - Re-architected the Qt app into four layers: a Qt-free Python `engine` (database, codecs, exams, formulas, reports, CAT3 sheets), a FastAPI `backend` (routes, jobs, events), a React + TypeScript `frontend`, and swappable desktop `shell`s (Qt WebEngine and pywebview).
  - Wrote the design, conventions, and phased implementation plan; completed the exam engine, exam documents and exports, correction matrices, and sheet/barcode generation with 79 test files. Next: the rebuilt OMR and grading.
  - **Tech:** Python, FastAPI, WebSockets, React, TypeScript, Vite, PySide6, pywebview, pytest

## Personal Projects

- **[SnapGrade](https://github.com/prmpsmart/snapgrade)** _(solo project, in active development)_

  - Desktop app for generating, scanning, and grading multiple-choice exam sheets via OMR — no Scantron hardware, no proprietary format lock-in.
  - Built the sheet-generation pipeline: auto-computed bubble-grid layouts (never too small to fill, never overflowing the page), barcode/QR-encoded sheet identity, and print-ready PDF export for single sheets or full batches.
  - Built and calibrated the OMR grading engine with **OpenCV**: barcode/QR decoding resolves each sheet's identity and expected layout, bubbles are classified by measured ink-fill ratio rather than fixed guesses, and ambiguous answers are flagged for review instead of silently guessed.
  - Implemented Excel-based roster import (prefilled sheets, ID-matched grading) and results export (summary + per-question detail) with **openpyxl**.
  - Built the **PySide6** UI with a token-based theming system — five switchable themes generated from one shared QSS template.
  - Sheet generation, the grading engine, and Excel I/O are built and validated against a calibration fixture; wiring the UI to those engines is the one remaining piece.

  **Tech:** PySide6, OpenCV, pyzbar, qrcode, python-barcode, ReportLab, openpyxl, uv

## Certifications

- **Python Developer Certification** — freeCodeCamp, July 2026 — [verify](https://www.freecodecamp.org/certification/prmpsmart/python-v9)

## Education

**B.Eng. in Electrical & Electronics Engineering**  
Federal University of Technology, Akure — Graduated 2024

## Languages

- English (Fluent, C1)
- Spanish (Conversational, B1)

## Contact

- **Email:** [prmpsmart@gmail.com](mailto:prmpsmart@gmail.com)
- **LinkedIn:** [linkedin.com/in/prmpsmart](https://linkedin.com/in/prmpsmart)
- **GitHub:** [github.com/prmpsmart](https://github.com/prmpsmart)
