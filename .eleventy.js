// .eleventy.js
const fetch = require("node-fetch"); // node-fetch v2
require("dotenv").config();

module.exports = function(eleventyConfig) {
  // -----------------------
  // 1️⃣ Blog collection
  // -----------------------
  eleventyConfig.addPassthroughCopy("src/styles.css"); // if in src/


  eleventyConfig.addCollection("blog", function(collectionApi) {
    return collectionApi.getFilteredByGlob("src/blog/*.md");
  });

  // -----------------------
  // 2️⃣ Global GitHub repo data
  // -----------------------
  eleventyConfig.addGlobalData("repos", async () => {
    const owner = "hmgene";            // <-- your GitHub username
    const repos = ["fossil-c"];        // <-- list of repo names

    try {
      const results = await Promise.all(
        repos.map(async (repo) => {
          const res = await fetch(`https://api.github.com/repos/${owner}/${repo}`, {
            headers: {
              Authorization: `Bearer ${process.env.GITHUB_TOKEN}`,
              "User-Agent": "11ty-dashboard"
            }
          });

          if (!res.ok) {
            console.log(`GitHub API error for ${repo}:`, res.status, res.statusText);
            return null;
          }

          return await res.json();
        })
      );

      return results.filter(Boolean);
    } catch (err) {
      console.error("Fetch failed:", err);
      return [];
    }
  });

  // -----------------------
  // 3️⃣ Passthrough copy
  // -----------------------
  eleventyConfig.addPassthroughCopy("assets");

  // -----------------------
  // 4️⃣ Directory config
  // -----------------------
  return {
    dir: {
      input: "src",
      output: "docs"
    }
  };
};
