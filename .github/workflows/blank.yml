name: Build MAX AI APK

on:
  push:
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-22.04

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Set up Java
        uses: actions/setup-java@v4
        with:
          distribution: temurin
          java-version: "17"

      - name: Install build dependencies
        run: |
          sudo apt-get update
          sudo apt-get install -y \
            git zip unzip \
            python3-pip \
            python3-venv \
            build-essential \
            autoconf \
            automake \
            libtool \
            pkg-config \
            zlib1g-dev \
            libncurses-dev \
            libffi-dev \
            libssl-dev

      - name: Install Buildozer
        run: |
          python3 -m pip install --user --upgrade pip
          python3 -m pip install --user buildozer cython==0.29.36
          echo "$HOME/.local/bin" >> "$GITHUB_PATH"

      - name: Build APK
        run: |
          buildozer android debug

      - name: Upload APK
        uses: actions/upload-artifact@v4
        with:
          name: MAX-AI-APK
          path: bin/*.apk
          if-no-files-found: error
