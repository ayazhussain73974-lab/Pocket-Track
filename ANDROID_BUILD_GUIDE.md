# PocketTrack - Android Build Guide 📱

This guide explains how to convert and package the PocketTrack web application into a native Android APK or Google Play Store Android App Bundle (AAB) using **Capacitor**.

---

## 🛠️ Prerequisites

Before building for Android, ensure you have the following installed on your machine:

1. **Node.js** (v18 or higher) and **npm**
2. **Android Studio** (Electric Eel, Flamingo, Giraffe, Iguana, or later)
   - Download from: [developer.android.com/studio](https://developer.android.com/studio)
3. **Android SDK & Build-Tools** (Installed automatically via Android Studio SDK Manager):
   - Android SDK Platform 34 (or 33+)
   - Android SDK Command-line Tools
   - Android SDK Build-Tools
4. **Java Development Kit (JDK)**: JDK 17 or JDK 21 (Bundled directly within Android Studio)

---

## 🚀 Quick Step-by-Step Android Build

### Step 1: Install Project Dependencies
Open your terminal in the unzipped `pockettrack` directory:
```bash
npm install
```

### Step 2: Build the Web Distribution Assets
Compile the React frontend into the `dist/` directory:
```bash
npm run build
```

### Step 3: Initialize the Android Native Project
Run the following Capacitor command to generate the native Android Studio project files in the `android/` directory:
```bash
npx cap add android
```
*(If the `android/` directory already exists, simply run `npm run cap:sync`)*

### Step 4: Sync Web Assets to Android
Whenever you modify your React code or styles, re-sync the build to your Android folder:
```bash
npm run cap:sync
```

---

## 📲 Building & Running the APK

### Option A: Open Directly in Android Studio (Recommended)
Launch Android Studio with the generated project:
```bash
npm run cap:open
```
Inside Android Studio:
1. Wait for **Gradle Sync** to finish (1-2 minutes on first run).
2. Connect your Android phone via USB (with **USB Debugging** enabled in Developer Options) OR start an Android Virtual Device (AVD Emulator).
3. Click the green **Run (▶)** button in the top toolbar to build and install PocketTrack directly on your device.

### Option B: Build a Debug APK from Terminal (Command Line)
If you have `ANDROID_HOME` configured in your PATH:
```bash
cd android
./gradlew assembleDebug
```
The output APK will be located at:
```
android/app/build/outputs/apk/debug/app-debug.apk
```
Transfer this file to any Android device to install!

---

## 🛡️ Building a Production Signed APK / AAB for Google Play Store

1. In Android Studio, click **Build** > **Generate Signed Bundle / APK**.
2. Select **Android App Bundle** (for Google Play) or **APK** (for direct distribution).
3. Choose or create a new KeyStore (`.jks`).
4. Select `release` build variant and check `V1 (Jar Signature)` & `V2 (Full APK Signature)`.
5. Click **Finish**. Your optimized release build is ready for the Play Store!

---

## ⚙️ App Configurations

- **App ID**: `com.pockettrack.app` (configured in `capacitor.config.json`)
- **App Name**: `PocketTrack`
- **Theme Color**: Emerald Green (`#059669`)
- **Icons**: Located in `public/icon.svg` & `android/app/src/main/res/mipmap/`
- **Offline Storage**: Uses HTML5 LocalStorage, fully persistent on Android without requiring server infrastructure.
