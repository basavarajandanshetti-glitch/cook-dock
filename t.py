import pytest
from chef import evaluate_chef


def test_master_chef(capsys):
    evaluate_chef("Ravi", "Royal Kitchen", "Biryani", 95, 92, 93)
    captured = capsys.readouterr()
    assert "Master Chef" in captured.out


def test_expert_chef(capsys):
    evaluate_chef("Anita", "Spice Hub", "Paneer Butter Masala", 85, 82, 80)
    captured = capsys.readouterr()
    assert "Expert Chef" in captured.out


def test_skilled_chef(capsys):
    evaluate_chef("Suresh", "Home Kitchen", "Dosa", 70, 68, 66)
    captured = capsys.readouterr()
    assert "Skilled Chef" in captured.out


def test_beginner_chef(capsys):
    evaluate_chef("Meena", "Street Food", "Pav Bhaji", 55, 52, 50)
    captured = capsys.readouterr()
    assert "Beginner Chef" in captured.out


def test_needs_improvement(capsys):
    evaluate_chef("Arjun", "Mini Kitchen", "Sandwich", 40, 45, 42)
    captured = capsys.readouterr()
    assert "Needs Improvement" in captured.out
