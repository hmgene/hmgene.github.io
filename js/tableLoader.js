fetch("/_data/projects.json")
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
  .catch(err => console.error("Error loading project data:", err));