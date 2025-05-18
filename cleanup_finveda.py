import os
import re

# Set updated project directory
project_path = r"/mnt/data/shesecured hackathon"

# Patterns and replacements
email_pattern = r"[a-zA-Z0-9_.+-]+@(gmail|hotmail)\.com"
linkedin_pattern = r"(linkedin\.com\/[^\s\"']+|LinkedIn:\s?.*)"
youtube_pattern = r"(youtube\.com\/[^\s\"']+|YouTube:\s?.*)"
website_pattern = r"(https?:\/\/[^\s\"']+|Website:\s?.*)"

# Replacement values
my_email = "shreerakshagourayya@gmail.com"
my_linkedin = "LinkedIn: Shriraksha Gourayya"
my_location = "Mangaluru"

# File extensions to process
file_extensions = [".html", ".js", ".css", ".py", ".txt", ".md"]

# Contributor section keywords
contributor_keywords = ["Contributor", "Contributors", "Created by", "Made by", "Developed by", "Author", "Maintainer"]

# Track changed files
changed_files = []

for root, dirs, files in os.walk(project_path):
    for file in files:
        if any(file.endswith(ext) for ext in file_extensions):
            file_path = os.path.join(root, file)
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()

            original_content = content

            # Remove full contributor sections
            content = re.sub(r"<section[^>]*id=[\"']?contributors?[\"']?[^>]*>.*?</section>", "", content, flags=re.DOTALL | re.IGNORECASE)

            # Replace emails
            content = re.sub(email_pattern, my_email, content)

            # Replace LinkedIn info
            content = re.sub(linkedin_pattern, my_linkedin, content, flags=re.IGNORECASE)

            # Remove YouTube and Website links
            content = re.sub(youtube_pattern, "", content, flags=re.IGNORECASE)
            content = re.sub(website_pattern, "", content, flags=re.IGNORECASE)

            # Replace Delhi with Mangaluru
            content = content.replace("Delhi", my_location)

            if content != original_content:
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(content)
                changed_files.append(file_path)

changed_files
