# Переменные
PYTHON = uv run
RUFF = uv run ruff

# Проверка кода
lint:
	$(RUFF) check .

# Автоисправление ошибок
fix:
	$(RUFF) check . --fix

# Форматирование кода
format:
	$(RUFF) format .

# Запуск всех игр (по отдельности)
brain-games:
	$(PYTHON) brain-games

brain-even:
	$(PYTHON) brain-even

brain-calc:
	$(PYTHON) brain-calc

brain-gcd:
	$(PYTHON) brain-gcd

brain-progression:
	$(PYTHON) brain-progression

brain-prime:
	$(PYTHON) brain-prime

# Установка зависимостей
install:
	uv sync

# Очистка кэша
clean:
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	rm -rf .ruff_cache .pytest_cache

# Всё сразу: проверка, формат, фикс
check:
	make lint
	make format
	make fix

# Подсказка по командам
help:
	@echo "Доступные команды:"
	@echo "  make install    - установить зависимости"
	@echo "  make lint       - проверить код"
	@echo "  make format     - отформатировать код"
	@echo "  make fix        - исправить ошибки"
	@echo "  make check      - всё сразу"
	@echo "  make clean      - очистить кэш"
	@echo ""
	@echo "Запуск игр:"
	@echo "  make brain-games"
	@echo "  make brain-even"
	@echo "  make brain-calc"
	@echo "  make brain-gcd"
	@echo "  make brain-progression"
	@echo "  make brain-prime"

.PHONY: lint fix format install clean check help
.PHONY: brain-games brain-even brain-calc brain-gcd brain-progression brain-prime