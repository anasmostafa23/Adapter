# Adapter Pattern Implementation

## What is the Adapter Pattern?

The **Adapter Pattern** is a structural design pattern that allows objects with incompatible interfaces to work together. It acts as a bridge between two incompatible interfaces.

### Our Example

This project demonstrates the classic "round peg in square hole" problem:

- **Circle** - has a `get_radius()` method
- **SquareHole** - expects objects with a `get_width()` method  
- **CircleAdapter** - adapts Circle to work with SquareHole by converting radius to diameter

```python
circle = Circle(radius=3)           # diameter = 6
adapter = CircleAdapter(circle)     # adapts circle to square interface
hole = SquareHole(width=8)         # square hole
print(hole.fits(adapter))          # True - circle fits!
```

## Running the Tests

### Prerequisites
```bash
pip install pytest
```

### Run all tests
```bash
pytest tests_pattern.py -v
```

### Run the demo
```bash
python pattern_impl.py
```

## Files
- `pattern_impl.py` - Main implementation
- `tests_pattern.py` - Comprehensive test suite
- `README.md` - This documentation

---

# Реализация паттерна Адаптер

## Что такое паттерн Адаптер?

**Паттерн Адаптер** — это структурный паттерн проектирования, который позволяет объектам с несовместимыми интерфейсами работать вместе.

### Наш пример

Проект демонстрирует классическую проблему "круглый колышек в квадратном отверстии":

- **Circle** - имеет метод `get_radius()`
- **SquareHole** - ожидает объекты с методом `get_width()`
- **CircleAdapter** - адаптирует Circle для работы с SquareHole, преобразуя радиус в диаметр

## Запуск тестов

### Установка зависимостей
```bash
pip install pytest
```

### Запуск всех тестов
```bash
pytest tests_pattern.py -v
```

### Запуск демонстрации
```bash
python pattern_impl.py
```