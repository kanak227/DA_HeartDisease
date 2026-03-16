# Heart Disease Analysis

A small, focused Flask site that embeds two Tableau Public visualisations (a Dashboard and a Story) and provides a clean, responsive landing page to explore heart disease analysis.

Key features
 - Lightweight Flask app with three routes: home, dashboard and story
 - Responsive hero landing page with clear CTAs
 - Embedded Tableau Public visualisations for interactive exploration

Live demo
 - https://da-heartdisease.onrender.com/

Tableau visualisations
 - Dashboard: https://public.tableau.com/views/final_17734236838190/Dashboard1
 - Story: https://public.tableau.com/views/final_17734236838190/Story1

If an embedded view does not load, each page includes a direct link to open the visualisation on Tableau Public.

Repository structure

```
app.py                  # Flask application (routes: /, /dashboard, /story)
README.md               # This file
templates/
  index.html            # Landing page (hero + nav)
  dashboard.html        # Embedded Tableau dashboard
  story.html            # Embedded Tableau story
static/
  styles.css            # Page styles and responsive iframe layout
```

Requirements
 - Python 3.8 or newer
 - pip
 - (recommended) virtual environment

Quick setup (recommended)

1. Create and activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install dependencies

```bash
python3 -m pip install --upgrade pip
python3 -m pip install flask
```

3. Run the application

```bash
python3 app.py
```

4. Open in your browser

 - Home: http://127.0.0.1:5000/
 - Dashboard: http://127.0.0.1:5000/dashboard
 - Story: http://127.0.0.1:5000/story

Notes & troubleshooting
- Embeds depend on Tableau Public availability. If a view is unpublished or restricted the iframe will be blank — use the direct link on the page to open the view on Tableau Public.
- If styles are not applied, confirm the static file is served from `/static/styles.css` and the Flask server shows no startup errors.
- For development, keep Flask in debug mode for auto reloads (already enabled in `app.py` via `app.run(debug=True)`).

Recommended next steps
- Add a `requirements.txt` if you add more Python dependencies (run `pip freeze > requirements.txt`).
- Replace the decorative SVG with a brand illustration or logo in `static/` and reference it from `index.html`.
- Add small accessibility improvements (ARIA attributes and skip links) and automated smoke tests.

Contributing

Feel free to open issues or submit pull requests to improve the UI, accessibility, or embed handling. Keep changes small and include screenshots for visual updates.

License

This project currently has no specified license — add one if you plan to share or publish the repository.
