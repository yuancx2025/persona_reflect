.PHONY: help install dev backend frontend docker-up docker-down clean test lint

# Default target
help:
	@echo "PersonaReflect - AI Self-Reflection Coach"
	@echo ""
	@echo "Available commands:"
	@echo "  make install      - Install all dependencies (backend + frontend)"
	@echo "  make dev          - Run both backend and frontend in dev mode"
	@echo "  make backend      - Run backend server only"
	@echo "  make frontend     - Run frontend dev server only"
	@echo "  make docker-up    - Start all services with Docker Compose"
	@echo "  make docker-down  - Stop all Docker services"
	@echo "  make test         - Run backend tests"
	@echo "  make lint         - Lint and format code"
	@echo "  make clean        - Clean build artifacts"

# Install dependencies
install:
	@echo "📦 Installing backend dependencies..."
	cd backend && pip install -r requirements.txt
	@echo "📦 Installing frontend dependencies..."
	cd frontend && npm install
	@echo "✅ All dependencies installed!"

# Development mode (both services)
dev:
	@echo "🚀 Starting development servers..."
	@make -j2 backend frontend

# Run backend only
backend:
	@echo "🐍 Starting backend server..."
	@if [ ! -f backend/.env ]; then \
		echo "⚠️  No .env file found. Copying from .env.example..."; \
		cp backend/.env.example backend/.env; \
		echo "⚠️  Please edit backend/.env with your API keys!"; \
	fi
	cd backend && uvicorn persona_reflect.main:app --reload --host 0.0.0.0 --port 8000

# Run frontend only
frontend:
	@echo "⚛️  Starting frontend dev server..."
	cd frontend && npm run dev

# Docker commands
docker-up:
	@echo "🐳 Starting Docker containers..."
	@if [ ! -f backend/.env ]; then \
		echo "⚠️  No .env file found. Copying from .env.example..."; \
		cp backend/.env.example backend/.env; \
		echo "⚠️  Please edit backend/.env with your API keys!"; \
	fi
	docker-compose up --build

docker-down:
	@echo "🛑 Stopping Docker containers..."
	docker-compose down

# Testing
test:
	@echo "🧪 Running backend tests..."
	cd backend && pytest -v

# Linting
lint:
	@echo "🔍 Linting and formatting backend code..."
	cd backend && black persona_reflect/
	cd backend && isort persona_reflect/
	@echo "🔍 Linting frontend code..."
	cd frontend && npm run lint

# Clean build artifacts
clean:
	@echo "🧹 Cleaning build artifacts..."
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name "node_modules" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name "dist" -exec rm -rf {} + 2>/dev/null || true
	@echo "✅ Cleaned!"

# Quick start (install + run)
start: install dev
