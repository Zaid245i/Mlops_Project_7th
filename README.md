<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Weather Prediction System</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      line-height: 1.6;
      margin: 0;
      padding: 0;
      background-color: #f4f4f4;
      color: #333;
    }
    header {
      background: #007BFF;
      color: white;
      padding: 1.5em;
      text-align: center;
    }
    nav {
      background: #333;
      color: white;
      padding: 1em;
    }
    nav ul {
      list-style: none;
      padding: 0;
    }
    nav ul li {
      margin: 0.5em 0;
    }
    nav ul li a {
      color: white;
      text-decoration: none;
    }
    section {
      padding: 2em;
      margin: 1em auto;
      background: white;
      border-radius: 8px;
      box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
      width: 80%;
    }
    h1, h2 {
      color: #007BFF;
    }
    pre {
      background: #f4f4f4;
      padding: 1em;
      border-radius: 5px;
    }
    footer {
      text-align: center;
      padding: 1em;
      background: #333;
      color: white;
    }
    img {
      display: block;
      margin: 1em auto;
      max-width: 100%;
    }
    .chart {
      text-align: center;
      margin: 1em auto;
    }
    .chart img {
      max-width: 100%;
      height: auto;
      margin-top: 1em;
    }
  </style>
</head>
<body>
  <header>
    <h1>🌦️ Weather Prediction System with MLOps Integration</h1>
    <p>Welcome to the <strong>Weather Prediction System</strong>, a state-of-the-art MLOps-driven application designed to predict temperatures based on weather conditions.</p>
  </header>

  <nav>
    <h2>📜 Table of Contents</h2>
    <ul>
      <li><a href="#introduction">🔍 Introduction</a></li>
      <li><a href="#overview">🧭 Project Overview</a></li>
      <li><a href="#tech-stack">🛠️ Tech Stack</a></li>
      <li><a href="#workflow">⚙️ Application Workflow</a></li>
      <li><a href="#features">✨ Features</a></li>
      <li><a href="#setup">⚡ Setup and Installation</a></li>
      <li><a href="#frontend">🌐 Frontend Interface</a></li>
      <li><a href="#backend">🔗 Backend API</a></li>
      <li><a href="#visualizations">📊 Visualizations and Analytics</a></li>
      <li><a href="#branches">🌳 Branch-Based Workflow</a></li>
      <li><a href="#testing">✅ Testing and Deployment</a></li>
      <li><a href="#learnings">📚 Learnings and Conclusion</a></li>
    </ul>
  </nav>

  <section id="introduction">
    <h2>🔍 Introduction</h2>
    <p>The <strong>Weather Prediction System</strong> is a practical implementation of <strong>MLOps</strong> concepts applied to a real-world problem. It leverages tools like <strong>DVC</strong> for data versioning, <strong>MLFlow</strong> for model management, and <strong>CI/CD pipelines</strong> for efficient, scalable machine learning development.</p>
  </section>

  <section id="overview">
    <h2>🧭 Project Overview</h2>
    <h3>🎯 Objectives</h3>
    <ul>
      <li>Develop an end-to-end machine learning pipeline for weather prediction.</li>
      <li>Automate data preprocessing, model training, and deployment.</li>
      <li>Provide a user-friendly application for easy interaction with the model.</li>
    </ul>
    <h3>🛤️ Workflow Diagram</h3>
    <div class="chart">
      <p>Here's the architecture of the system:</p>
      <img src="workflow-diagram.png" alt="Workflow Diagram">
    </div>
  </section>

  <section id="tech-stack">
    <h2>🛠️ Tech Stack</h2>
    <h3>Machine Learning</h3>
    <ul>
      <li><strong>Python 🐍:</strong> The backbone of the project.</li>
      <li><strong>Scikit-learn:</strong> For implementing Linear Regression.</li>
      <li><strong>MLFlow:</strong> Model tracking, versioning, and registry.</li>
    </ul>
    <h3>MLOps Tools</h3>
    <ul>
      <li><strong>DVC:</strong> Data versioning and reproducibility.</li>
      <li><strong>Airflow:</strong> Task workflow automation.</li>
      <li><strong>Kubernetes + Minikube:</strong> Deployment and orchestration.</li>
      <li><strong>Docker:</strong> Containerization for scalability.</li>
    </ul>
    <h3>Full-Stack Application</h3>
    <ul>
      <li><strong>Frontend:</strong> React/Angular or plain HTML + JS for UI.</li>
      <li><strong>Backend:</strong> FastAPI for creating RESTful APIs.</li>
      <li><strong>Database:</strong> SQLite/MySQL for user authentication.</li>
    </ul>
  </section>

  <section id="visualizations">
    <h2>📊 Visualizations and Analytics</h2>
    <p>The system provides advanced analytics and visualizations, including:</p>
    <div class="chart">
      <p><strong>Temperature Trends Over Time</strong></p>
      <img src="temperature-trends.png" alt="Temperature Trends">
    </div>
    <div class="chart">
      <p><strong>Humidity Levels Across Different Cities</strong></p>
      <img src="humidity-chart.png" alt="Humidity Chart">
    </div>
    <div class="chart">
      <p><strong>Wind Speed Distribution</strong></p>
      <img src="wind-speed-distribution.png" alt="Wind Speed Distribution">
    </div>
  </section>

  <footer>
    <p>Thank you for exploring the Weather Prediction System! 🚀</p>
  </footer>
</body>
</html>
