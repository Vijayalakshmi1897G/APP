import re


def extract_emails(text: str) -> list[str]:
  pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
  return re.findall(pattern, text)


if __name__ == "__main__":
  sample_text = """
    Contact support at helpdesk@mitadt.edu.in or reach out to
    vj.student2026@gmail.com and admissions_cell@university.org.
    Invalid strings like user@.com or plain_text should be ignored.
    """

  found_emails = extract_emails(sample_text)
  print("Extracted Emails:")
  for email in found_emails:
    print(" -", email)