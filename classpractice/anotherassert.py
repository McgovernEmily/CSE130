def compute_tx (income):
    tax = -1.0

    if 0 <= income < 15100:
        tax = income * 0.10
    elif 15100