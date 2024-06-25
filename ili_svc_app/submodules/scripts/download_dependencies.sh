#!/bin/bash

# Note: the version of ili2db must be the same as the one used in the source code
# iliservices/libs/modelbaker/iliwrapper/ili2dbtools.py
ILI2DB_VERSION="5.1.0"

# Target directory
DEST_DIR="iliservices/modelbaker/iliwrapper/bin"

# Create the target directory if it doesn't exist
mkdir -p "$DEST_DIR"

# Elimina las librerías existentes para hacer una descarga limpia
# rm -rf "$DEST_DIR/*"

# Download ili2pg
echo "Downloading ili2pg..."
wget https://downloads.interlis.ch/ili2pg/ili2pg-${ILI2DB_VERSION}.zip -P "$DEST_DIR"

# Download ili2gpkg
echo "Downloading ili2gpkg..."
wget https://downloads.interlis.ch/ili2gpkg/ili2gpkg-${ILI2DB_VERSION}.zip -P "$DEST_DIR"

# Unzip files into the target directory
echo "Unzipping files..."
unzip -o "$DEST_DIR/ili2pg-5.1.0.zip" -d "$DEST_DIR/ili2pg-${ILI2DB_VERSION}"
unzip -o "$DEST_DIR/ili2gpkg-5.1.0.zip" -d "$DEST_DIR/ili2gpkg-${ILI2DB_VERSION}"

# Clean up downloaded ZIP files
echo "Cleaning up downloaded files..."
rm "$DEST_DIR/ili2pg-5.1.0.zip"
rm "$DEST_DIR/ili2gpkg-5.1.0.zip"

echo "Process completed."
