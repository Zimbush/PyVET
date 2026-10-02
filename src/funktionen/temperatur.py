"""
Modul: temperatur.py
Funktionen zur Umrechnung zwischen Celsius und Fahrenheit.
"""

def celsius_to_fahrenheit(celsius: float) -> float:
    return celsius * 9 / 5 + 32

def fahrenheit_to_celsius(fahrenheit: float) -> float:
    return (fahrenheit - 32) * 5 / 9
