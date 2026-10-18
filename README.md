# PocketTrack 🚀
> Minimum Viable Product (MVP) Expense & Pocket Money Tracker for Students

PocketTrack is a lightweight, mobile-first student budgeting application designed to solve one core problem: **students spending pocket money without tracking and running out before the end of the month**.

---

## 🌟 Core Features

- **Balance Dashboard**: Real-time remaining pocket money, cycle countdown, and monthly burn pace indicator.
- **Daily Spending Limit Progress Bar**: Automatically calculates your safe daily spending limit (`Remaining Balance ÷ Days Remaining`) with a real-time progress bar and status warnings.
- **Student 1-Tap Quick Spends**: Rapidly log campus chai/coffee, canteen lunches, metro bus passes, and notebook printing.
- **Custom Expense & Top-Up Modal**: Specialized categories for students (*Canteen & Snacks*, *Books & Stationery*, *Bus & Commute*, *Phone Data*, *Hangouts*, *Emergency*).
- **Searchable Pocket History**: Search transactions in real-time by note keyword or category name with 1-click filter clearing.
- **Export Data to CSV**: Download your full transaction history anytime as a formatted `.csv` file.
- **Broke-Defense Tips**: Practical strategies and student lifehacks for stretching pocket money.
- **Global Currencies**: Full support for `$`, `₹`, `£`, `€`, `₨`, `₱`, `¥`, and more.
- **Offline-First & Local Storage**: Automatically saves all changes locally in the browser/app.

---

## 💻 Local Development Setup

### 1. Install Dependencies
```bash
npm install
```

### 2. Start Local Development Server
```bash
npm run dev
```
Open your browser at `http://localhost:3000`.

### 3. Build for Production Web
```bash
npm run build
```

---

## 📱 Building as an Android App

PocketTrack is pre-configured with **Capacitor** to build directly into an Android native APK or Google Play App Bundle:

```bash
# 1. Compile web assets
npm run build

# 2. Add Android native project (first time only)
npx cap add android

# 3. Sync assets
npm run cap:sync

# 4. Open in Android Studio to build APK
npm run cap:open
```

See [ANDROID_BUILD_GUIDE.md](./ANDROID_BUILD_GUIDE.md) for full Android Studio build and signing steps.

---

## 📁 Project Structure

```
├── android/               # Native Android project (generated via Capacitor)
├── capacitor.config.json  # Capacitor native app configuration
├── public/                # Static assets, SVG app launcher icon & manifest.json
│   ├── icon.svg
│   └── manifest.json
├── src/
│   ├── components/        # UI components
│   │   ├── BalanceDashboard.tsx       # Hero balance, safe daily limit progress
│   │   ├── BudgetSettingsModal.tsx    # Allowance setup & CSV export
│   │   ├── ExpenseModal.tsx           # Expense/top-up modal
│   │   ├── Header.tsx                 # Top navigation bar
│   │   ├── SpendingBreakdown.tsx      # Category breakdown & insights
│   │   ├── StudentBrokeDefenseTips.tsx# Campus money-saving tips
│   │   └── TransactionList.tsx        # Searchable transaction ledger
│   ├── constants/         # Student categories, currencies & quick presets
│   ├── types/             # TypeScript definitions
│   ├── utils/             # Calculation logic & demo student datasets
│   ├── App.tsx            # Root application component
│   ├── index.css          # Tailwind CSS styling
│   └── main.tsx           # App entry point
├── ANDROID_BUILD_GUIDE.md # Detailed Android build guide
└── package.json           # Dependencies and build scripts
```
