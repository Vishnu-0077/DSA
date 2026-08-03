def formatting_date(str):
    months = {
        'january': '01', 'jan': '01',
        'february': '02', 'feb': '02',
        'march': '03', 'mar': '03',
        'april': '04', 'apr': '04',
        'may': '05',
        'june': '06', 'jun': '06',
        'july': '07', 'jul': '07',
        'august': '08', 'aug': '08',
        'september': '09', 'sep': '09',
        'october': '10', 'oct': '10',
        'november': '11', 'nov': '11',
        'december': '12', 'dec': '12'
    }

    # Normalize input
    data_str = str.replace("-", " ")
    data_str = data_str.replace(",", " ")
    data_str = data_str.replace("/", " ")
    data_str = data_str.replace("   ", "  ")
    data_str = data_str.replace("  ", " ")
    data_str = data_str.strip()
    parts = data_str.split()

    # Check if first part is a month name
    if parts[0].isalpha():
        month = months[parts[0].lower()]
        day = parts[1].zfill(2)
        year = parts[2].zfill(4)
    else:
        # Assume format: MM DD YYYY
        month = parts[0].zfill(2)
        day = parts[1].zfill(2)
        year = parts[2].zfill(4)
    return f"{year} {month} {day}"

print(formatting_date("january-1,2023"))  # Output: "2023 01 01"