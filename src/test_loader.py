from data_loader import load_pdf

pdf_path = "data/raw/cpa_2019.pdf"

text = load_pdf(pdf_path)
print(text[:1000])   # print first 1000 characters
print("\nLength:", len(text))
