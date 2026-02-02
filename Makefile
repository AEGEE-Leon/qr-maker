PY ?= py -3
PYTHON ?= python3

OUTPUT_DIR := output
IMG_DIR := img

.PHONY: help setup deps dirs build full all clean check

help:
	@echo "Makefile commands:"
	@echo "  build      - Build QR code image with basic settings"
	@echo "  full       - Build QR code image with full settings"
setup: 
	pip install qrcode[pil] pillow
build: setup
	@$(PYTHON) QR_buildImage.py 

full: setup
	@$(PYTHON) QR_fullImage.py
