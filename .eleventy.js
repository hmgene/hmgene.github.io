// .eleventy.js
const fetch = require("node-fetch"); // node-fetch v2
require("dotenv").config();

module.exports = function(eleventyConfig) {

  // Add global data for GitHub repos
  eleventyConfig.addGlobalData("repos", async () => {
    const owner = "hmgene";            // <-- your GitHub username
    const repos = ["fossil-c"];            // <-- list of repo names

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

      // Remove any failed fetches
      return results.filter(Boolean);

    } catch (err) {
      console.error("Fetch failed:", err);
      return [];
    }
  });

  // Copy static assets
  eleventyConfig.addPassthroughCopy("assets");

  return {
    dir: {
      input: "",
      output: "_site"
    }
  };
};
