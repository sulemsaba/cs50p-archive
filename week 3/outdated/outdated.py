# outdated.py on week 3 the final in this week
# outdated.py

MONTHS = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

def main():
    while True:
        date_input = input("Date: ").strip()
        
        # Numeric format: 9/8/1636
        try:
            if "/" in date_input:
                month, day, year = map(int, date_input.split("/"))
            # Textual format: September 8, 1636
            elif any(month in date_input for month in MONTHS) and "," in date_input:
                parts = date_input.split()
                # Validate that second part ends with a comma
                if not parts[1].endswith(","):
                    continue
                month = MONTHS.index(parts[0]) + 1
                day = int(parts[1].replace(",", ""))
                year = int(parts[2])
            else:
                continue
            
            if 1 <= month <= 12 and 1 <= day <= 31:
                print(f"{year}-{month:02}-{day:02}")
                break
        except (ValueError, IndexError):
            continue

if __name__ == "__main__":
    main()
