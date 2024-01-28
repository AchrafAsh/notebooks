#!/bin/bash

VENV_DIR="env"
PYTHON="$VENV_DIR/bin/python"
PIP="$VENV_DIR/bin/pip"

add_package() {
    local package_name="$1"
    if [ -z "$package_name" ]; then
        echo "Error: Please provide a package name."
        exit 1
    fi
    echo "Installing and updating package: $package_name"
    $PIP install "$package_name"
    $PIP freeze > requirements.txt
    echo "Package $package_name installed and requirements.txt updated."
}

install_packages() {
    echo "Installing packages from requirements.txt..."
    $PIP install -r requirements.txt
    echo "Packages installed."
}

# Main script logic
case "$1" in
    add)
        shift
        add_package "$@"
        ;;
    install)
        install_packages
        ;;
    *)
        echo "Usage: $0 {add|install|clean}"
        exit 1
        ;;
esac
