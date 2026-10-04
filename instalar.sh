#!/bin/bash
# Instalador automático do AssetsHunter-ptBR

echo "======================================"
echo "  Instalando AssetsHunter-ptBR"
echo "======================================"

echo ""
echo "[1/3] Atualizando pip..."
pip install --upgrade pip

echo ""
echo "[2/3] Instalando dependências do Python..."
pip install netaddr ipwhois python-whois lxml dnspython pymysql beautifulsoup4 requests censys

echo ""
echo "[3/3] Instalando dependências do sistema (Termux)..."
# Só funciona no Termux; se não for, ignora o erro
pkg install -y libxml2 libxslt openssl libffi 2>/dev/null || true

echo ""
echo "======================================"
echo "  Instalação concluída!"
echo "  Agora rode: python menu.py"
echo "======================================"
