# Miracle Apata — Backend Engineer

[GitHub](https://github.com/prmpsmart) • [LinkedIn](https://linkedin.com/in/prmpsmart) • [Email](mailto:prmpsmart@gmail.com) • [Portfolio](https://prmpsmart.github.io) • +234 816 852 4477  
Akure, Nigeria (WAT, UTC+1) · Remote · Open to remote roles

## Summary

Backend engineer building secure, real-time APIs in **Python (FastAPI, Django) and TypeScript (Node.js, NestJS)** for mobile and web products in commerce, logistics, estate management, and safety. Experienced with RBAC and JWT/OAuth2 auth, WebSocket and push infrastructure, multi-tenant design, and Docker/CI pipelines. Early member of a young software company, where I owned all backend work before also leading mobile, so I design APIs with the client developer in mind.

## Technical Skills

- **Languages:** Python, TypeScript, JavaScript, SQL, C# · _Familiar:_ C, C++, OCaml
- **Frameworks:** FastAPI, Django, Flask, Node.js, Express, NestJS, ASP.NET
- **Databases:** PostgreSQL, MongoDB, MySQL, Redis
- **Architecture:** RESTful APIs, microservices, WebSockets, serverless, multi-tenant systems
- **Auth & Security:** JWT, OAuth2, session auth, RBAC
- **DevOps:** Docker, Docker Compose, GitHub Actions, AWS (CodePipeline), Nginx, Linux, PM2
- **Testing:** Pytest, Jest, Postman, unit and integration testing

## Experience

_All engagements are remote and held concurrently._

**Backend Engineer (Contract)** · [Jorly](https://dev.flyjorly.com) · Canada (Remote) · _May 2026 – Present_

- Building the Jorly travel-booking API in FastAPI and PostgreSQL: Sabre-backed flight, hotel and car search, Paystack/Flutterwave payments, group travel, JWT auth, and Celery background jobs. In development.

**Backend Engineer** · [Jodna Technologies](https://jodnatechnologies.com) · Port Harcourt, Nigeria (Remote) · _Dec 2024 – Present_

- Early member of a young software company delivering client projects; initially owned all backend work.
- Led backend architecture for mobile and web platforms on **FastAPI and Node.js**: authentication, RBAC, analytics.
- Built a notification microservice (FastAPI + Socket.IO) with device-token FCM support; integrated cloud storage and push notifications.
- Mentored junior backend engineers and enforced coding standards.

**Freelance Software Developer** · Remote · _2020 – Present_

- Delivered backend APIs and automation scripts for clients in Nigeria and internationally.

**Backend Engineer** · [Sofgo](https://sofgo.io) · Ondo, Nigeria (Remote) · _Sep 2023 – Sep 2024_

- Built RESTful APIs (Django, Node.js) for logistics and e-commerce platforms, with authentication, payment gateways, and deployment pipelines, working closely with mobile engineers.

## Projects

**piXeval rebuild — engine & API (DINATEN)** _(in progress, sole developer)_ — _Python, FastAPI, WebSockets, pytest_

- Designed a Qt-free service layer (database, codecs, exams, formula evaluation without `eval`, reports, exports) and a FastAPI HTTP/WebSocket backend with background jobs, typed results, progress events, and mirrored error codes.
- Documented the design, conventions, and phased plan; 79 test files; rewrote legacy sheet-generation scripts supplied by the product owner into a modular pipeline.

**Multi-Tenant Mobile API Backend (Jodna)** — _FastAPI, MongoDB, Redis, JWT, PM2_

- Scalable role-based APIs with real-time notifications and analytics tracking for a mobile commerce app.

**Jorly API** _(in development)_ — _Python 3.13, FastAPI, SQLModel, PostgreSQL, Redis, Celery, Docker_

- REST API for a travel booking platform that searches and books through Sabre (domestic and international flights alike, Nigerian market first) behind swappable provider adapters, takes payment (Paystack, Flutterwave), and only then creates the booking; in-progress searches live in Redis with a TTL.
- Layered architecture (routes, services, repositories), own JWT access/refresh auth, Celery beat jobs, FCM push, group-travel state, Alembic migrations, and pytest suite; documented as a handover reference.

**[Tywn](https://home.twynapp.org/) backend** — _Node.js, TypeScript, PostgreSQL, JWT_

- Live location logging, alert dispatch, and personnel monitoring for security agents; private fleet tracking and subscriptions.

**[PriceGrid](https://github.com/prmpsmart/price-grid)** _(personal)_ — _FastAPI, SQLModel, PostgreSQL, Redis, Alembic, Docker, pytest_

- Price-intelligence API for informal markets: append-only price records, cross-market comparison, Redis-cached hot reads invalidated on write.
- Spike detection as a decoupled Redis pub/sub pipeline; JWT and RBAC; unit and integration tests; one-command Docker Compose setup.

## Education, Recognition & Certifications

- **B.Eng. Electrical & Electronics Engineering**, Federal University of Technology, Akure — 2024
- **Outstanding Technical Contribution**, TrackWeNg (now Tywn) — Certificate of Recognition, Dec 2025
- **Python Developer Certification**, freeCodeCamp — Jul 2026 ([verify](https://www.freecodecamp.org/certification/prmpsmart/python-v9))
- **Languages:** English (fluent, C1), Spanish (conversational, B1)
