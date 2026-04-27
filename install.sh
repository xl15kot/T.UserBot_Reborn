#!/bin/bash

# T.UserBot Reborn v0.3 Beta - Linux Installer
# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

echo "============================================================"
echo "  T.UserBot Reborn v0.3 Beta - Linux Installer"
echo "============================================================"

# Detect distribution
detect_distro() {
    if [ -f /etc/os-release ]; then
        . /etc/os-release
        case $ID in
            ubuntu|debian)
                echo "debian"
                ;;
            linuxmint)
                echo "mint"
                ;;
            arch|manjaro)
                echo "arch"
                ;;
            *)
                echo "unknown"
                ;;
        esac
    else
        echo "unknown"
    fi
}

echo ""
echo "Select your distribution:"
echo "  1) Linux Mint"
echo "  2) Debian/Ubuntu"
echo "  3) Arch Linux/Manjaro"
echo "  4) Auto-detect"
echo ""
read -p "Enter choice (1-4): " distro_choice

case $distro_choice in
    1)
        DISTRO="mint"
        ;;
    2)
        DISTRO="debian"
        ;;
    3)
        DISTRO="arch"
        ;;
    4)
        DISTRO=$(detect_distro)
        echo -e "${GREEN}Detected: $DISTRO${NC}"
        ;;
    *)
        echo -e "${RED}Invalid choice${NC}"
        exit 1
        ;;
esac

echo ""
echo -e "${BLUE}[1/4] Installing system dependencies...${NC}"

case $DISTRO in
    mint|debian)
        echo "  Updating package list..."
        sudo apt update
        echo "  Installing Python3 and pip..."
        sudo apt install -y python3 python3-pip python3-pyqt5
        ;;
    arch)
        echo "  Updating system..."
        sudo pacman -Syu --noconfirm
        echo "  Installing Python3 and pip..."
        sudo pacman -S --noconfirm python python-pip python-pyqt5
        ;;
    *)
        echo -e "${RED}Unknown distribution. Please install manually:${NC}"
        echo "  Debian/Ubuntu: sudo apt install python3 python3-pip python3-pyqt5"
        echo "  Arch: sudo pacman -S python python-pip python-pyqt5"
        exit 1
        ;;
esac

echo -e "${GREEN}✓ System dependencies installed${NC}"

echo ""
echo -e "${BLUE}[2/4] Installing Python libraries...${NC}"

echo "  Installing telethon..."
python3 -m pip install telethon --break-system-packages 2>/dev/null || python3 -m pip install telethon

echo "  Installing requests..."
python3 -m pip install requests --break-system-packages 2>/dev/null || python3 -m pip install requests

echo "  Installing Pillow..."
python3 -m pip install Pillow --break-system-packages 2>/dev/null || python3 -m pip install Pillow

echo -e "${GREEN}✓ Python libraries installed${NC}"

echo ""
echo -e "${BLUE}[3/4] Creating run script...${NC}"

cat > run.sh << 'EOF'
#!/bin/bash
cd "$(dirname "$0")"
python3 main.py
EOF

chmod +x run.sh
echo -e "${GREEN}✓ run.sh created${NC}"

echo ""
echo -e "${BLUE}[4/4] Creating desktop entry...${NC}"

cat > ~/.local/share/applications/tuserbot.desktop << EOF
[Desktop Entry]
Name=T.UserBot Reborn v0.3 Beta
Comment=Telegram UserBot
Exec=$(pwd)/run.sh
Icon=utilities-terminal
Terminal=true
Type=Application
Categories=Network;
StartupNotify=true
EOF

chmod +x ~/.local/share/applications/tuserbot.desktop
echo -e "${GREEN}✓ Desktop entry created${NC}"

echo ""
echo "============================================================"
echo -e "${GREEN}✅ Installation complete!${NC}"
echo "============================================================"
echo ""
echo "Run the bot with: ./run.sh"
echo "Or find 'T.UserBot Reborn v0.3 Beta' in your applications menu"
echo ""