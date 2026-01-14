import express from "express";
import fetch from "node-fetch";
import path from "path";
import { fileURLToPath } from "url";

const app = express();

// Fix __dirname for ES modules
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// View engine setup
app.set("view engine", "ejs");
app.set("views", path.join(__dirname, "views"));

// Backend API URL
const URL = process.env.BACKEND_URL || "http://localhost:8000/api";

app.get("/", async (req, res) => {
  const options = {
    method: "GET",
  };

  try {
    // Fetch data from backend
    const response = await fetch(URL, options);
    const data = await response.json();

    console.log("RENDER DATA:", data);
    res.render("index", { data: data });
  } catch (err) {
    console.error(err);
    res.status(500).json({ msg: "Internal Server Error" });
  }
});

app.listen(3000, () => {
  console.log("Ares listening on port 3000!");
});
