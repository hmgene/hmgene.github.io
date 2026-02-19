import os
import zipfile

# Define folder structure and files
structure = {
    "_data": {"projects.json": '''[
  { "name": "Portfolio Site", "skills": ["JS", "HTML", "CSS", "Eleventy"], "year": 2025, "link": "https://github.com/yourname/portfolio" },
  { "name": "Data Viz Dashboard", "skills": ["D3.js", "Python", "Eleventy"], "year": 2024, "link": "https://github.com/yourname/dataviz" },
  { "name": "Machine Learning Tool", "skills": ["Python", "Scikit-learn", "Pandas"], "year": 2023, "link": "https://github.com/yourname/ml-tool" }
]'''},
    "downloads": {
        "CV_HyunminKim.pdf": b"",
        "example_code.zip": b"",
        "dataset.csv": b""
    },
    "js": {"tableLoader.js": '''fetch("/_data/projects.json")
  .then(res => res.json())
  .then(data => {
    const tbody = document.querySelector("#projects-table tbody");
    data.forEach(proj => {
      const row = document.createElement("tr");
      row.innerHTML = `
        <td>${proj.name}</td>
        <td>${proj.skills.join(", ")}</td>
        <td>${proj.year}</td>
        <td><a href="${proj.link}" target="_blank">Link</a></td>
      `;
      tbody.appendChild(row);
    });
    const filterInput = document.querySelector("#skill-filter");
    filterInput.addEventListener("input", (e) => {
      const val = e.target.value.toLowerCase();
      tbody.querySelectorAll("tr").forEach(tr => {
        const skills = tr.children[1].textContent.toLowerCase();
        tr.style.display = skills.includes(val) ? "" : "none";
      });
    });
  })
  .catch(err => console.error("Error loading project data:", err));'''},
    "css": {"style.css": '''body { font-family: Arial, sans-serif; margin: 2rem; }
input { margin-bottom: 1rem; padding: 0.5rem; width: 200px; }
table { width: 100%; border-collapse: collapse; margin-top: 1rem; }
th, td { border: 1px solid #aaa; padding: 0.5rem; }
th { background-color: #f0f0f0; }'''},
    "_includes": {"layout.njk": '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>{{ title | default("My Portfolio") }}</title>
  <link rel="stylesheet" href="/css/style.css">
</head>
<body>
  <header>
    <h1>{{ title | default("My Portfolio") }}</h1>
  </header>
  <main>
    {{ content | safe }}
  </main>
  <script src="/js/tableLoader.js"></script>
</body>
</html>'''},
    "index.njk": '''---
layout: layout.njk
title: "My Projects"
---

<h2>Projects</h2>
<input type="text" id="skill-filter" placeholder="Filter by skill...">

<table id="projects-table">
  <thead>
    <tr>
      <th>Project</th>
      <th>Skills</th>
      <th>Year</th>
      <th>Link</th>
    </tr>
  </thead>
  <tbody></tbody>
</table>

<h2>Downloads</h2>
<ul>
  <li><a href="/downloads/CV_HyunminKim.pdf" download>Download My CV</a></li>
  <li><a href="/downloads/example_code.zip" download>Download Example Code</a></li>
  <li><a href="/downloads/dataset.csv" download>Download Dataset</a></li>
</ul>''',
    ".eleventy.js": '''module.exports = function(eleventyConfig) {
  eleventyConfig.addPassthroughCopy("js");
  eleventyConfig.addPassthroughCopy("css");
  eleventyConfig.addPassthroughCopy("downloads");
  return { dir: { input: ".", output: "_site" } };
};'''
}

# Create folders and files
for folder, files in structure.items():
    if isinstance(files, dict):
        os.makedirs(folder, exist_ok=True)
        for filename, content in files.items():
            path = os.path.join(folder, filename)
            mode = 'wb' if isinstance(content, bytes) else 'w'
            with open(path, mode) as f:
                f.write(content)
    else:
        with open(folder, 'w') as f:
            f.write(files)

# Create ZIP
zip_filename = "11ty_portfolio_template.zip"
with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk("."):
        if root.startswith("./_site") or root.startswith("./.git"):  # skip output folder or git
            continue
        for file in files:
            zipf.write(os.path.join(root, file))

print(f"ZIP file created: {zip_filename}")

