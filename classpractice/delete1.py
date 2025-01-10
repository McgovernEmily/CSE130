def display_grade(grade):

    # Pre-condition checks
    assert type(grade) == str
    assert 1 <= len(grade) <= 2
    assert grade[0] in {"A", "B", "C", "D", "F"}
    assert grade not in ("F-", "A+", "F+")

    letter = grade[0]
    if len(grade) == 2:
        assert grade[1] == "+" or grade[1] == "-"
        sign = grade[1]
    else:
        sign = ""

    # Post-condition checks.
    assert letter in {"A", "B", "C", "D", "F"}
    assert sign in {"+", "-", ""}

    print("Your letter grade is", letter, "add your sign is", sign)