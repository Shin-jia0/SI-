def convert_unit(value, from_unit):
    conversions = {
        "inch": ("meter", value * 0.0254),
        "foot": ("meter", value * 0.3048),
        "mile": ("meter", value * 1609.34),
        "pound": ("kilogram", value * 0.453592),
        "ounce": ("kilogram", value * 0.0283495),
        "gallon": ("liter", value * 3.78541),
        "fahrenheit": ("celsius", (value - 32) * 5 / 9)
    }

    from_unit = from_unit.lower()
    if from_unit in conversions:
        to_unit, result = conversions[from_unit]
        return f"{value} {from_unit} = {result:.4f} {to_unit}"
    else:
        return "지원하지 않는 단위입니다."

# 실행 부분
if __name__ == "__main__":
    print("단위 변환기 (비-SI → SI)")
    try:
        value = float(input("값을 입력하세요: "))
        unit = input("단위를 입력하세요 (예: inch, foot, pound, fahrenheit 등): ")
        print(convert_unit(value, unit))  # <-- unit은 문자열이므로 OK!
    except:
        print("올바른 숫자를 입력해주세요.")