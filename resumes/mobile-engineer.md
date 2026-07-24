# Miracle Apata — Mobile Engineer

[GitHub](https://github.com/prmpsmart) • [LinkedIn](https://linkedin.com/in/prmpsmart) • [Email](mailto:prmpsmart@gmail.com)

---

## Summary

Mobile Engineer specializing in building scalable cross-platform applications using **Flutter and React Native**. Experienced in designing production-ready mobile systems from concept to deployment, with strong focus on **clean architecture, performance optimization, and real-time mobile features**. Proven ability to collaborate with product teams, backend engineers, and designers to deliver reliable user-focused applications.

---

## Technical Skills

**Languages**  
Dart, Kotlin, JavaScript, TypeScript

**Mobile Development**  
Flutter, React Native, Android SDK, iOS SDK

**Architecture & Patterns**  
Clean Architecture, BLoC, MVVM, MVC, OOP, Modular Architecture

**Backend & APIs**  
REST APIs, GraphQL, Secure API Integration

**Databases**  
SQLite, PostgreSQL, MongoDB, Firebase Realtime DB, Cloud Firestore

**DevOps & CI/CD**  
Git, GitHub, GitHub Actions

**Testing & Performance**  
Unit Testing, Integration Testing, Performance Optimization

**Concepts**  
Push Notifications, Background Services, State Management, Mobile Security, Real-time Data Synchronization

---

## Experience

### [Jodna Technologies](https://jodnatechnologies.com/) — Senior Mobile Engineer

Port Harcourt, Nigeria  
December 2024 – Present

- Led mobile development for **three production Flutter apps** — Vaultify (estate management), Sentinel (access management), and Tywn (real-time safety & location sharing) — from architecture through App Store/Play Store release.
- Improved application startup and screen rendering performance by **reducing load times by ~40%** through UI refactoring and optimized API interactions.
- Architected a **shared real-time and push notification infrastructure** (Socket.IO, Firebase Cloud Messaging) reused across the team's apps for live chat, alerts, and status sync.
- Built robust integrations with **RESTful APIs** to enable reliable real-time data synchronization.
- Collaborated closely with designers, backend engineers, and product stakeholders during sprint cycles to deliver production-ready features.
- Mentored junior engineers and introduced **clean architecture practices** to improve maintainability and scalability.
- Maintained and enhanced existing mobile applications, improving stability and user experience.

---

### [Zent Technologies Limited](https://joinzent.com/) — Mobile Engineer (Contract)

Lagos, Nigeria  
March 2025 – July 2025

- Developed and maintained the **Zent mobile application** using Flutter for Android and iOS.
- Built interactive UI components from product design prototypes with **smooth animations and responsive layouts**.
- Integrated backend services supporting **real-time order tracking, inventory management, and payment workflows**.
- Improved application responsiveness by optimizing **state management and API request handling**.
- Collaborated with cross-functional teams to deliver high-quality product features within tight deadlines.

**Product:**  
Play Store: <https://play.google.com/store/apps/details?id=pro.zent.zent_mobile_app>

---

### [Sofgo](https://sofgo.io) — Mobile Engineer

Ondo, Nigeria  
September 2023 – September 2024

- Built and maintained production mobile applications using **Flutter for Android and iOS**.
- Collaborated with backend engineers and product teams to deliver features aligned with business goals.
- Maintained modular codebases and implemented **integration testing strategies** to ensure application reliability.
- Contributed to feature development, debugging, and UI improvements across multiple client projects.

---

## Featured Projects

### [OxyTrack](https://healthportafrica.com) — Oxygen Cylinder Inventory & Facility Management Platform

Built for **HealthPort Africa**, a health-tech company digitizing oxygen access and distribution to hospitals and facilities, OxyTrack is an internal operations app that lets facility staff and biomedical equipment technicians (BMETs) **track medical oxygen cylinders through their full lifecycle** — from fill to dispatch, inspection, and audit.

> Key Contributions

- Built a **cylinder lifecycle tracking system** covering fill status, serial numbers, purity, pressure, inspection due dates, and overdue/urgency flags across multiple facilities.
- Implemented **QR and NFC-based cylinder identification**, letting staff scan physical cylinder tags for instant lookup and status updates.
- Developed **facility and inventory management modules** with role-based access for admins and BMET technicians.
- Built **cylinder audit and inspection workflows** with a dashboard for inventory and usage visualization.
- Architected the app with clean domain/module separation (BLoC + Hydrated BLoC), Dio-based networking, and secure token storage.

**Technologies**  
Flutter, BLoC / Hydrated BLoC, Dio, QR Code Scanning, NFC, Secure Storage, Clean Architecture

---

### [Vaultify](https://vaultify.africa) — Smart Estate Management App

Developed while working at **Jodna Technologies**, Vaultify helps residential estates run smoothly in one app — letting residents **generate visitor access codes, receive announcements, send one-tap emergency alerts to estate security, book vetted service providers, and pay estate dues**.

> Key Contributions

- Built resident-facing **wallet, bill payment (airtime, data, cable, electricity), and estate service charge** features integrated with Paystack.
- Implemented **QR-based virtual ID and access code verification**, enabling security personnel to validate visitor passes at the gate.
- Developed a **real-time private chat between residents and estate security** using Socket.IO.
- Integrated **Firebase Cloud Messaging push notifications** for announcements, alerts, and transaction updates.
- Led an in-progress **architectural refactor** of the app from a legacy controller structure into a modular per-feature repository/controller pattern to improve maintainability.

**Technologies**  
Flutter, GetX, Socket.IO, Paystack, Firebase Cloud Messaging, QR Code Generation/Scanning, Secure Storage

**Link**  
App Store: <https://apps.apple.com/ng/app/vaultify-estate-app/id6751677794>

---

### [Sentinel](https://sentinelsoftware.live) — Smart Community Access Management Platform

Developed while working at **Jodna Technologies**, Sentinel is a digital access management platform used by estates, offices, and schools to **digitize visitor entry, security checkpoints, and resident-security coordination**.

> Key Contributions

- Developed **digital visitor registration and multi-step check-in/check-out workflows**, including resident-approval and security-verification handoffs for guest access.
- Implemented **QR code scanning and barcode-based access verification**, letting security check guests in and out in real time.
- Built **sub-profile management**, letting residents grant scoped access permissions to dependents and household members.
- Added **real-time announcements, broadcasts, and activity logs** synchronized via Socket.IO across resident and security roles.
- Integrated **Firebase Cloud Messaging push notifications** for visit requests, alerts, and estate announcements.

**Technologies**  
Flutter, BLoC / Hydrated BLoC, Socket.IO, Firebase Cloud Messaging, QR Code Scanning, Secure API Integration

**Link**  
App Store: <https://apps.apple.com/us/app/sentinel-acess-management/id6758545811>

---

### [Tywn](https://home.twynapp.org/) (formerly TrackWeNg) — Real-Time Safety & Social Location-Sharing Platform

Developed while working at **Jodna Technologies**, Tywn (rebranded from TrackWeNg) is a real-time location-sharing and safety app that lets users **share their live location with trusted contacts, coordinate with groups, and send one-tap emergency alerts** — without calls or texts.

> Key Contributions

- Architected a **real-time geolocation tracking system** with continuous background location updates via native Android/iOS background modes.
- Implemented **battery-optimized background services and a home-screen widget** that can trigger and manage live location sharing without opening the app.
- Built **"Cliques" (group) and real-time chat functionality** over Socket.IO, combining direct/group messaging with location sharing.
- Developed a **one-tap emergency alert system** that broadcasts live location to trusted contacts during safety incidents.
- Designed privacy-focused permission handling and secure transmission of location and messaging data, including iOS App Tracking Transparency compliance.

**Technologies**  
Flutter, BLoC / Hydrated BLoC, Socket.IO, Google Maps, Firebase Cloud Messaging, Background Location Services, Home Screen Widgets

**Links**  
App Store: <https://apps.apple.com/us/app/tywn-formerly-trackweng/id6741412135>  
Play Store: <https://play.google.com/store/apps/details?id=com.wetrack.ng>

---

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
