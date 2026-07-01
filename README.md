# Authentication FRMP

A full‑stack authentication system with username/password login, Google Sign‑In, and a secure JWT access + refresh‑token flow.

**Live app:** [Frontend Link](https://authentication-frmp.vercel.app/login)

**API docs (Swagger):** [Backend Docs](https://authenticationfrmp-production.up.railway.app/docs)

---

## Features

- **Register & Login** with username + password (passwords hashed with bcrypt).
- **Google Sign‑In** — Firebase popup on the frontend; the backend verifies the Google ID token with `google-auth` and auto‑creates a user (unique username generated on collision).
- **JWT access tokens** (short‑lived, 15 min) returned to the client.
- **Refresh tokens** (30 days) stored **hashed (SHA‑256)** in the database and delivered as a **secure, httpOnly cookie** — never exposed to JavaScript.
- **Token rotation** — every refresh issues a new refresh token and invalidates the old one.
- **Per‑device sessions** — refresh tokens are keyed by device (User‑Agent), so logging out / rotating on one device doesn't affect others.
- **Logout** — revokes the stored refresh token and clears the cookie.
- **Auto‑refresh on expiry** — an axios interceptor transparently refreshes an expired access token and retries the request.
- **Protected routes** on the frontend backed by an `/auth/me` check.
- **Dark‑themed** auth UI.

### Tech stack

| Layer | Tech |
|---|---|
| Frontend | React, TypeScript,Firebase Auth |
| Backend | FastAPI, SQLAlchemy, PostgreSQL, python‑jose (JWT), passlib + bcrypt, google‑auth |
| Hosting | Vercel (frontend) · Railway (backend) · Neon(Postgres) |

---

## Screenshots

### Authorization workflow
![Authorization workflow](screenshots/auth-workflow.png)

### Login page
![Login page](screenshots/login.png)

### Backend API docs
![Backend docs](screenshots/docs.png)

---

## How to use

### Try it live
1. Open the [live app](https://authentication-frmp.vercel.app/login).
2. Create an account, or click **Continue with Google**.
3. You'll be redirected to the protected home page once authenticated.

### Run locally

**Backend**
```bash
cd Backend
python -m venv .venv
.venv\Scripts\activate          # Windows  (use: source .venv/bin/activate on macOS/Linux)
pip install -r requirements.txt
python -m uvicorn main:app --reload --port 8000
```

Create a `Backend/.env`:
```env
DATABASE_URL=postgresql+psycopg://user:password@host:5432/dbname
JWT_SECRET_KEY=your-long-random-secret
GOOGLE_CLIENT_ID=your-google-web-client-id
```

**Frontend**
```bash
cd Frontend
npm install
npm run dev
```

`Frontend/.env.development` points the app at your local API:
```env
VITE_API_URL="http://localhost:8000"
```

> The backend's CORS `allow_origins` must include the frontend origin.

---

## Project structure

```
Authentication_FRMP/
├── Backend/
│   ├── auth/
│   │   ├── auth_router.py
│   │   └── auth_service.py
│   ├── database.py
│   ├── models.py
│   ├── main.py
│   └── requirements.txt
└── Frontend/
    └── src/
        ├── apis/api.ts
        ├── config/FirebaseConfig.ts
        ├── hooks/useUser.tsx
        ├── layouts/ProtectedRoute.tsx
        ├── pages/
        ├── App.tsx
        ├── main.tsx
        └── index.css
```

---

## Future improvements

- Email verification and password‑reset flow.
- "Active sessions" view with the ability to revoke individual devices.
- Rate limiting / lockout on repeated failed logins.
- Add a unique `jti` claim to refresh tokens for guaranteed uniqueness.
- More OAuth providers (GitHub, Microsoft).
- Automated tests (pytest for the API, component tests for the UI).

---

## Author

**Vedananda** — [GitHub @Vedananda-19](https://github.com/Vedananda-19)
